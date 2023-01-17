#%% exercício udemy de fazer dois números serem plotados e além disso fazer a soma, multiplicação divisão e subtração
# input = fazer uma pergunta
numero1 = int (input('Digite o primeiro número:'))
numero2 = int (input('Digite o segundo número:'))

print ('Adição:', numero1+numero2)
print ('Divisão:', numero1/numero2)
print ('Multiplicação:',numero1*numero2)
print ('Subtração:', numero1-numero2)

#%% viagem que a pessoa gasta 12 km por 
# round = mostrar onde colocar será o posição do décimal

tempo_de_viagem = float (input('Quanto tempo durou a viagem?'))
km_por_hora = float (input('Qual foi a média de km por hora?'))

print ('Foi gasto',round((tempo_de_viagem*km_por_hora)/12,1),'litros de combustivel')

#%% classificação das idade

idade = int (input('Qual é a sua idade?'))

if idade >=0 and idade <=12:
    print ('Criança')
    if idade >=13 and idade <=17:
        print ('Adolecente')
        if idade >=18 and idade <=100:
            print ('Adulto')
            if idade < 0:
                print ('Inválido')
                
#%% calcular a média de um aluno com 3 provas

n1 = float (input('Qual é a nota da 1ª prova?'))
n2 = float (input('Qual é a nota da 2ª prova?'))           
n3 = float (input('Qual é a nota da 3ª prova?'))

media = (n1+n2+n3)/3

if media >=0 and media <=4:
    print ('Reprovado')
elif media >=4.1 and media <=6:
        print ('Recuperação')
        if media >=6.1 and media <=10:
            print ('Aprovado')
            
#%% Ler 5 notas e informar a média
# range = faixa, usar o '_' economiza uma variável e consequêntemente economiza memoria

# fazendo o teste com for
nota = media = soma = 0
for _ in range (1,6):
    nota = float(input('Qqual é a nota? '))
    soma += nota
    media = soma/5
print('A media é', media )

#fazendo o teste com while
soma = nota = 0
numero = 1
while numero <= 5:
    nota = float (input('qual é a sua nota? '))
    soma += nota
    numero += 1
print('A média é', soma/5)
    

#%% Lendo a tabuada do 3 

# com for
multiplicação = 0
for numero in range (0,11):
    if numero < 30 :
        multiplicação *= numero
        numero *= 3
        print(numero)
        
# outra opção com for
for i in range(0,11):
    print('3 x {} = {}'.format(i, 3 * i))
      
# com while
numero = 1
while numero <= 10:
    print('3 x {} = {}'.format(numero, 3 * numero))
    numero += 1
    
#%% Crie uma estrutura de repetição para fazer a leitura de 5 números inteiros e os armazene dentro de uma lista. Após a leitura, crie outra estrutura de repetição para somar todos os valores digitados
lista = []
for _ in range (1,6):        
    valor = int (input('dígete um número: '))
    lista.append(valor)
    
print(lista)

soma = 0
for i in range (len(lista)):
    soma += lista[i]
    print('A soma é', soma)
    
#%% Dicionário: Crie um dicionário para armazenar o nome e a nota de 3 alunos, fazendo a leitura dos valores por meio de uma estrutura de repetição. Depois, crie uma nova estrutura de repetição para somar todas as notas e retornar a média
alunos = {}
for _ in range (1,4):        
    nome = input('dígete um nome: ')
    nota = float (input('dígete uma nota: '))
    alunos[nome] = nota
    
alunos

soma = 0
for nota in alunos.values():
    soma += nota
    print('A média é', soma/3)
    
    
#%%Matriz: Dada a matriz abaixo, construa uma estrutura de repetição para percorrer e somar todos os elementos da matriz

import numpy as np

matriz = np.array([[3, 4, 1],
                   [3, 1, 5]])

soma = 0
for i in range (matriz.shape[0]):
    for j in range (matriz.shape[1]):
        soma += matriz[i][j]
        print(soma)


#%%Ler uma temperatura em graus Celsius e apresentá-la convertida em graus Fahrenheit. A fórmula de conversão é F = (9 * C + 160) / 5, na qual F é a temperatura em Fahrenheit e C é a temperatura em graus Celsius
#- Função para ler e retorna o valor da temperatura (não recebe parâmetro)
#- Função para fazer o cálculo (recebe como parâmetro a temperatura em graus Celsius)
#- Função para mostrar o resultado, recebendo como parâmetro o valor e fazendo a impressão

def ler_temperatura():
    temperatura = float(input('Dígite uma temperatura em graus celsius: '))
    return temperatura

def converter(temperatura_celsius):
    fh = (9 * temperatura_celsius + 160)/5
    return fh

def mostrar (fh):
    print(fh)
    
temperatura_celsius = ler_temperatura()
fh = converter(temperatura_celsius)

#%%Efetuar o cálculo da quantidade de litros de combustível gasto em uma viagem, utilizando um automóvel que faz 12 Km por litro. Para obter o cálculo, o usuário deve fornecer o tempo gasto na viagem e a velocidade média durante ela. Desta forma, será possível obter a distância percorrida com a fórmula DISTANCIA = TEMPO * VELOCIDADE. Tendo o valor da distância, basta calcular a quantidade de litros de combustível utilizada na viagem, com a fórmula: LITROS_USADOS = DISTANCIA / 12. O programa deve apresentar os valores da velocidade média, tempo gasto na viagem, a distância percorrida e a quantidade de litros utilizada na viagem
#- Função para ler os valores (não recebe parâmetro e retorna os dois valores)
#- Função para calcular a distância (recebe como parâmetro o tempo e a velocidade e retorna a distância)
#- Função para calcular a quantidade de litros (recebe como parâmetro a distância e retorna os litros)
#- Função para apresentar o resultado (recebe como parâmetro os valores e somente imprime o resultado)

#DISTANCIA = TEMPO * VELOCIDADE
#LITROS_USADOS = DISTANCIA / 12

def leitura():
    velocidade = float(input('Qual foi a sua velocidade: '))
    tempo = float(input('Quanto tempo durou a sua viagem: '))
    return velocidade, tempo

def calcula_distancia(tempo, velocidade):
    return tempo * velocidade

def calcula_litros(distancia):
    return distancia/12


def imprime(velocidade, tempo, distancia, litros):
    print('Velocidade:', velocidade)
    print('Tempo:', tempo)
    print('Distância: ', distancia)
    print('Litros: ', litros)
    
t, v = leitura()
d = calcula_distancia(t, v)
l = calcula_litros(d)
imprime(v,t,d,l)

#%%Crie um arquivo .py com duas funções
#- Função para ler um string (recebe como parâmetro uma mensagem e retorna o que o usuário digitou)
#- Função para ler um número float (recebe como parâmetro uma mensagem e retorna o que o usuário digitou)

#criação do modelo:
    
def ler_string():
    return input(mensagem)

def ler_float():
    return float(input(mensagem))

#obs: o arquivo tem que ser salvo com o nome de leitura.py para ser importado no google colab
#no google colab, quando for importar

import leitura as lt

texto = lt.ler_string()
print (texto)

numero = lt.ler_floay()
print (numero)

#%%Crie uma lista vazia e faça a leitura de dois valores do tipo float, colocando cada um dos valores nas primeiras posições da lista (o valor1 ficará na posição 0 da lista e o valor2 ficará na posição 1 da lista). Faça a divisão dos dois valores e trate as seguintes exceções:
#- ValueError: se o usuário digitar um caracter
#- ZeroDivisionError: se o usuário digitar zero e ocorrer erro na divisão
#- IndexError: caso a divisão seja feita levando em consideração posições que não existem na lista
#- KeyboardInterrupt: caso o usuário interrompa a execução
#Mostre uma mensagem personalizada na ocorrência de cada um desses erros

# quando se coloca o f dentro de parenteses com string com aspas ele puxa a função anterior ex: linha 227

lista = []
try:
    lista.append(float(input('dígite o primeiro valor: ')))
    lista.append(float(input('dígite o segundo valor: ')))
    divisao = lista [0] / lista [1]
except ValueError:
    print ('Erro, Valor inválido')
except ZeroDivisionError:
    print ('Erro, não zero em divisão')
except IndexError:
    print ('Erro, o índice não existe')
except KeyboardInterrupt:
    print ('Erro, o usuário interrompeu a conexão')
else:
    print (f'A divisão é {divisao}')
    
#%%Considerando o dicionário com o nome dos alunos e suas respectivas notas abaixo, crie uma estrutura de repetição para percorrer cada elemento do dicionário para gravar cada aluno em um novo arquivo de texto
#- Cada aluno deve ocupar uma linha do novo arquivo de texto
#- O formato deve ser: nome,nota (Pedro,8.0)
#- Após a criação do arquivo de texto, faça a leitura do arquivo e mostre todos os alunos
#alunos = {'Pedro': 8.0, 'Maria': 10.0, 'Amilton': 7.5}    

alunos = {'Pedro': 8.0, 'Maria': 10.0, 'Amilton': 7.5}
alunos

with open('alunos.txt','w'):
    for aluno, nota in alunos.items():
        arquivo.write(f'{aluno},{nota}\n')
        
with open('alunos.txt','w'):
    for linha in arquivo:
        
#%%Crie expressões regulares para extrair as seguintes informações do texto abaixo (use a função findall):
#- Números
#- CEPs
#- URLs

texto = "minha casa fica na rua Carneiro, 78. O CEP é 88388-000 e meu site é https://www.iaexpert.academy"

import re
re.findall('\d', texto)  

re.findall('\d{5}-\d{3}', texto) 

re.findall('https?://[A-Za-z0-9]+', texto) 

#%% 1. Crie uma classe chamada aluno com os seguintes atributos:
#- Nome
#- Nota 1
#- Nota 2
#- Crie um construtor para a classe (__init__)

#2.Crie as seguintes funções (métodos):
#- Calcula média, retornando a média aritmética entre as notas
#- Mostra dados, que somente imprime o valor de todos os atributos
#- Resultado, que verifica se o aluno está aprovado ou reprovado (se a média for maior ou igual a 6.0, o aluno está aprovado)

#3.Crie dois objetos (aluno1 e aluno2) e teste as funções

class Aluno:
    
    # Estava errado só o nome da função init. O correto é __init__, com
    # dois underlines no início e no fim. Isso é importante pois no método de
    # construção ele entende que a função __init__ é uma inicialização.
    # Quando se cria a classe já roda essa função. Coloquei um print pra
    # testar isso.
    
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        print('A função __init__ funcionou.')
    
    def calcula_media(self):
        self.media = (self.nota1 + self.nota2)/2
    
    def mostrar_dados(self):
        print('Nome:',self.nome)
        print('Nota 1:',self.nota1)
        print('Nota 2:',self.nota2)
        print('Média:',self.media)
    
    def resultado(self):
        if self.media >= 6.0:
            print('Aprovado')
        else:
            print ('reprovado')
        
aluno1 = Aluno('Joao', 9.0, 7.0)
media = aluno1.calcula_media()
result = aluno1.resultado()

aluno1 = Aluno('Pedro', 9.0, 2.0)
media = aluno1.calcula_media()
result = aluno1.resultado()

# Uma sugenstão pra que se possa colocar qualquer quantidade de notas
# para o aluno.

class Aluno:

    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota
        print('A função __init__ funcionou.')
    
    def calcula_media(self):
        self.media = sum(self.nota)/len(self.nota)
    
    def mostrar_dados(self):
        print('Nome:',self.nome)
        print('Notas:',self.nota)
        print('Média:',self.media)
    
    def resultado(self):
        if self.media >= 6.0:
            print('Aprovado')
        else:
            print ('reprovado')
        
aluno1 = Aluno('Joao', [9, 7, 8])
media = aluno1.calcula_media()
result = aluno1.resultado()

aluno2 = Aluno('Pedro', [9, 4, 2])
media = aluno1.calcula_media()
result = aluno1.resultado()

# A mesma coisa, só que de uma forma um pouco mais elegante.
class Aluno:

    def __init__(self, nome, nota):
        
        self.nome = nome
        self.nota = nota
        print('A função __init__ funcionou.')
    
    def resultado(self):
        
        self.media = sum(self.nota)/len(self.nota)
        self.media = round(self.media,2)
        if self.media >= 6.0:
            result = 'aprovado'
        else:
            result = 'reprovado'
            
        print('O aluno '+self.nome+' foi '+result+'. Com média '+str(self.media)+'.')
            
aluno1 = Aluno('Joao', [9, 7, 8])
media = aluno1.calcula_media()
result = aluno1.resultado()

aluno2 = Aluno('Pedro', [9, 4, 2])
media = aluno1.calcula_media()
result = aluno1.resultado()

#%% Pré-processamento de dados.

dados.describe() #para informações estatísticas da tabela do pandas, obs: o 'dados' é nome da tabela, então pode variar, mas geralmente é dados mesmo.

# boas biblíotecas para plotar gráficos.
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

#excluir colunas. 

df.drop('Name', axis = 1, inplace = True) #axis = 1 apaga a coluna inteira. Inplace = True, salva a informação no dataframe.
df2 = df.drop('Name', axis = 1) #aqui, eu não excluo a coluna da tabela original, eu crio uma variação sem a coluna que desejo remover.

#excluir valores inconsistêntes das tabelas. usei a mesma lógica do excluir colunas para entender na tabela origina e também sem excluir ela.
df.drop(df[df['Age']>0].index, inplace = True)
df2 = df.drop(df[df['Age'] > 0].index)
df[df[df'Age'] > 0].index # retorna os indices que tem valor maior que 0

#tratamento de valores faltantes.
df.isnull() #  retonar onde tem valores faltantes, False = não tem valores faltantes e True =tem valores faltantes.
df.isnull().sum() # além de fazer o que a funçção acima faz, essa ainda soma os valores faltantes de cada coluna.
df['Age'].fillna(30, inplace = True) #Aqui foi usado uma função para substituir dados faltantes.
df['Age'].min() #retorna o valor mínimo da coluna.
df[ 'Age'].max() #retona o valor máximo das colunas.

from sklearn.preprocessing import LabelEncoder # função para substituir dados como palavras e letras por dados númericos.
#%% machine learn

# naiive bayes.
from sklearn.naive_bayes import GaussianNB
x = df.drop(columns=['Survived'])
y = df['Survived']
modelo_1 = GaussianNB()
modelo_1.fit(x,y)

#comparar os acertos e os erros.
from sklearn.metrics import accuracy_score, confusion_matrix
accuracy_score(y,x) # y = os valores reais, x = as previsões do algoritimo 
confusion_matrix(y,x) # faz a mesma coisa do accuracy_score(), porém da a resposta em classes. Mais informações no curso de programação, aula 39 de naive bayes. 

#árvore de decisão.

from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
x = df.drop(columns=['Survived'])
y = df['Survived']
modelo_1 = DecisionTreeClassifier(criterion = 'entropy')
modelo_1.fit(x,y)
modelo_1.feature_importances_ # mostra a importância de cada variável.

from sklearn import tree #para plotar gráfico da árvore de decisão.
tree.plot_tree(modelo_1) #para plotar gráfico da árvore de decisão.


