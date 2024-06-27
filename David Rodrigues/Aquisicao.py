import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

print('Aquisição de dados - Bancada 4.0')
print('ATENÇÃO: Verifique antes se o seu computador está conectado a rede do ESP-32.\n')

bool_continuar = True

def realizar_leituras(endpoint, nome_caso):
    leituras_raw = requests.get(f'http://192.168.4.1/{endpoint}')
    leituras = leituras_raw.text.split('\n')[:-2]
    dados = []
    for leitura in leituras:
        lista_leitura = leitura.split(',')
        dados.append(lista_leitura)
    df_raw = pd.DataFrame(data=dados[1:], columns=dados[0])
    df_raw = df_raw.astype(float)
    data = datetime.now().strftime("%d%m%Y_%H%M%S")
    df_raw.to_csv(f'DADOSBRUTOS_{data}_{nome_caso}_{endpoint}.csv', index=False)
    return df_raw
    
try:
    while bool_continuar:
        nome_caso = input('Digite o nome do caso: ')

        for sensor in ['sensor1', 'sensor2']:
            dados_brutos = realizar_leituras(sensor, nome_caso)
            N = len(dados_brutos)
            T = 1 / N
            f = np.fft.fftfreq(N, T) # Frequência
            freq_motor = 58
            hp = np.array([0 if freq < 10 else 1 for freq in f[f > 0]]) # Filtro passa alta de 10hz
            fft_acc_x = np.abs(np.fft.fft(dados_brutos.iloc[:, 0] * np.hanning(N)))[f > 0] * hp
            fft_acc_y = np.abs(np.fft.fft(dados_brutos.iloc[:, 1] * np.hanning(N)))[f > 0] * hp
            fft_acc_z = np.abs(np.fft.fft(dados_brutos.iloc[:, 2] * np.hanning(N)))[f > 0] * hp
            fft_vel_x = np.divide(fft_acc_x / np.pi, f[f > 0], out = np.zeros_like(fft_acc_x), where = fft_acc_x != 0)
            fft_vel_y = np.divide(fft_acc_y / np.pi, f[f > 0], out = np.zeros_like(fft_acc_y), where = fft_acc_y != 0)
            fft_vel_z = np.divide(fft_acc_z / np.pi, f[f > 0], out = np.zeros_like(fft_acc_z), where = fft_acc_z != 0)
            plt.figure(figsize=(21, 9))
            plt.suptitle(sensor)
            plt.subplot(1, 2, 1)
            plt.plot(f[f > 0], fft_acc_x, label='x')
            plt.plot(f[f > 0], fft_acc_y, label='y')
            plt.plot(f[f > 0], fft_acc_z, label='z')
            for harmonico in [1, 2, 3, 4]:
                plt.axvline(x = freq_motor * harmonico, color = 'tab:red', linestyle = '--')
            plt.xlabel('Frequência [hz]')
            plt.ylabel('Aceleração [g]')
            plt.subplot(1, 2, 2)
            plt.plot(f[f > 0], fft_vel_x, label='x')
            plt.plot(f[f > 0], fft_vel_y, label='y')
            plt.plot(f[f > 0], fft_vel_z, label='z')
            for harmonico in [1, 2, 3, 4]:
                plt.axvline(x = freq_motor * harmonico, color = 'tab:red', linestyle = '--')
            plt.xlabel('Frequência [hz]')
            plt.ylabel('Velocidade')
            plt.legend()
            plt.tight_layout()
            plt.savefig(f'{nome_caso}_{sensor}.png')
        
        str_continuar = input('Deseja realizar mais uma amostragem? Digite "s" e pressione ENTER para continuar. Para sair, pressione apenas ENTER. ')
        if str_continuar.upper() == 'S':
            bool_continuar = True
        else:
            bool_continuar = False
            
except Exception as e:
    print(e)