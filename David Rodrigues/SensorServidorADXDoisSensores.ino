/*
  Rui Santos
  Complete project details at https://RandomNerdTutorials.com/esp32-client-server-wi-fi/
  
  Permission is hereby granted, free of charge, to any person obtaining a copy
  of this software and associated documentation files.
  
  The above copyright notice and this permission notice shall be included in all
  copies or substantial portions of the Software.
*/

// Import required libraries
#include "WiFi.h"
#include "ESPAsyncWebServer.h"
#include <ADXL345_WE.h>
#include <SPI.h>

#define CS_PIN_1 5   // Chip Select Pin
#define CS_PIN_2 15   // Chip Select Pin

// Set your access point network credentials
const char* ssid = "ESP32-Access-Point";
const char* password = "123456789";
const long interval = 1000UL; // Tempo de Amostragem
const int int2Pin1 = 21;  // interrupt pin
const int int2Pin2 = 22;  // interrupt pin
volatile bool dataReady1 = false;
volatile bool dataReady2 = false;
bool spi = true;    // flag indicating that SPI shall be used

ADXL345_WE myAcc1 = ADXL345_WE(CS_PIN_1, spi);
ADXL345_WE myAcc2 = ADXL345_WE(CS_PIN_2, spi);
AsyncWebServer server(80);

String lerSensor1() {
  digitalWrite(CS_PIN_1, LOW);
  digitalWrite(CS_PIN_2, HIGH);
  // Leitura primeiro sensor
  long start = millis();
  String saida1 = "x1,y1,z1\n";
  while (millis() - start < interval) {
    if(dataReady1 == true){
      xyzFloat g = myAcc1.getGValues();
      dataReady1 = false; // uncomment, if you want capture next interrupts
      String output1 = String(String(g.x) + "," + String(g.y) + "," + String(g.z) + "\n");
      saida1.concat(output1);
    }
  }
  dataReady1 = true;
  return saida1;
}

String lerSensor2() {
  digitalWrite(CS_PIN_1, HIGH);
  digitalWrite(CS_PIN_2, LOW);
  // Leitura primeiro sensor
  long start = millis();
  String saida2 = "x2,y2,z2\n";
  while (millis() - start < interval) {
    if(dataReady2 == true){
      xyzFloat g = myAcc2.getGValues();
      dataReady2 = false; // uncomment, if you want capture next interrupts
      String output2 = String(String(g.x) + "," + String(g.y) + "," + String(g.z) + "\n");
      saida2.concat(output2);
    }
  }
  dataReady2 = true;
  return saida2;
}

void setup(){
  Serial.begin(9600); //Inicia o monitor serial

  // Inicialização do sensor 1
  pinMode(int2Pin1, INPUT); // Pino Interrupcao
  Serial.println("ADXL345 1");
  if(!myAcc1.init()){
    Serial.println("ADXL345 1 não conectado!");
  }
  myAcc1.setSPIClockSpeed(3000000);
  myAcc1.setDataRate(ADXL345_DATA_RATE_3200);
  delay(100);
  myAcc1.setRange(ADXL345_RANGE_8G);
  Serial.print("  /  g-Range: ");
  Serial.println(myAcc1.getRangeAsString());
  Serial.println();
  attachInterrupt(digitalPinToInterrupt(int2Pin1), dataReadyISR1, RISING);
  myAcc1.setInterrupt(ADXL345_DATA_READY, INT_PIN_2); 
  myAcc1.readAndClearInterrupts();

  // Inicialização do sensor 2
  pinMode(int2Pin2, INPUT); // Pino Interrupcao
  Serial.println("ADXL345 2");
  if(!myAcc2.init()){
    Serial.println("ADXL345 2 não conectado!");
  }
  myAcc2.setSPIClockSpeed(3000000);
  myAcc2.setDataRate(ADXL345_DATA_RATE_3200);
  delay(100);
  myAcc2.setRange(ADXL345_RANGE_8G);
  Serial.print("  /  g-Range: ");
  Serial.println(myAcc2.getRangeAsString());
  Serial.println();
  attachInterrupt(digitalPinToInterrupt(int2Pin2), dataReadyISR2, RISING);
  myAcc2.setInterrupt(ADXL345_DATA_READY, INT_PIN_2); 
  myAcc2.readAndClearInterrupts();
  
  // Setting the ESP as an access point
  Serial.print("Setting AP (Access Point)…");
  // Remove the password parameter, if you want the AP (Access Point) to be open
  WiFi.softAP(ssid, password);

  IPAddress IP = WiFi.softAPIP();
  Serial.print("AP IP address: ");
  Serial.println(IP);

  server.on("/sensor1", HTTP_GET, [](AsyncWebServerRequest *request){
    request->send_P(200, "text/plain", lerSensor1().c_str());
  });

  server.on("/sensor2", HTTP_GET, [](AsyncWebServerRequest *request){
    request->send_P(200, "text/plain", lerSensor2().c_str());
  });
  
  // Start server
  server.begin();
}
 
void loop(){
  
}

void dataReadyISR1() {
  dataReady1 = true;
}

void dataReadyISR2() {
  dataReady2 = true;
}