n1=int(input('digite um número:'))
n2=int(input('digite outro número:'))
s=n1+n2
s1=n1-n2
s2=n1/n2
s3=n1**n2
print('Soma',s)
print('Supração',s1)
print('Divisão',s2)
print('exponenciação',s3)

#soma,divisão,supração,exponecial
número = int(input('digite um número:'))
resultado = número % 2
if resultado == 0:
   print('o número {} é PAR'.format(número))
else: print('o número {} é ÍMPAR'.format(número))

#ímpar ou par
for cont in range(0,10):
    print(cont **2)

#lista de números
x = 10
while x<=1000:
    x= x **2
    print (x)

#fazer a operação em loop até chegar no resultado desejado
n1 = int(input('Digite um número:'))
print(n1)
import random
lista = (1,2,3,4,5)
escolhido = random.choice(lista)
if n1 == escolhido:
    print('You win!')
else: print('You lose!')
print('o número escolhido foi {}'. format(escolhido))
opção = 0
while opção != 2:   
    print(''' [ 1 ] Continuar jogando 
          [ 2 ] Sair do jogo''')
    opção = int(input('qual é a opção?'))
print('Fim do jogo! Volte sempre !')
#jogo de acertar o número



    