#%% teste de ruído
import pandas as pd
import random
import numpy as np

lista_1 = (6.8,6.5,6.6,6.7,3.0,9.0,8.6,7.4,4.5,9.5,8.1,4.7,5.6,6.4)
lista_2 = (45,38,40,37,43,36,50,55,34,41,66,35,70,65,60,90,42)
lista_3 = (0,1)
lista_4 = ('low', 'medium', 'high')

colunas = 'pH','Temprature','Taste','Odor','Fat ','Turbidity','Grade'

pH =pd.DataFrame(np.random.choice(lista_1,212))  
Temprature = pd.DataFrame(np.random.choice(lista_2,212))
Taste = pd.DataFrame(np.random.choice(lista_3,212))
Odor = pd.DataFrame(np.random.choice(lista_3,212))
Fat = pd.DataFrame(np.random.choice(lista_3,212))
Turbidity = pd.DataFrame(np.random.choice(lista_3,212))
Grade = pd.DataFrame(np.random.choice(lista_4,212))

tabela = pd.concat([pH, Temprature, Taste, Odor, Fat, Turbidity, Grade],axis = 1)
#dados de teste

#%% teste de ruído

# Lista com os nomes das variáveis, pra ficar mais organizado.
features = 'pH', 'Temprature', 'Taste', 'Odor', 'Fat ', 'Turbidity', 'Grade'
df.columns = features

# Matriz aleatória. Cuidado com os tamanhos. O -0.5 é pra
# permitir que seja negativa. Quero dados que aumentem ou
# diminuam os originais.
aleatorio = np.random.random(df.drop(columns=['Colour']).shape) - 0.5

# Num DataFrame igual, pra ficar organizado, mas isso é opcional.
aleatorio = pd.DataFrame(aleatorio) 

# Cálculo das médias das colunas, isso vai ser usado pra
# corrigir as ordens de grandeza.
media = df.drop(columns=['Colour']).mean(axis=0)

# Novo DataFrame.
nova = pd.DataFrame()

# Aqui é onde a mágica acontece.
# Percentual de ruído que eu quero testar, 10%.
fator_de_ruido = 0.1

# Para cada coluna faça a seguinte conta:
    
# novo = original + ruido

# onde
# ruído = fator de ruído * média * valor aleatório

# Observe que o fator de ruído é o percentual que aceitamos
# de erro. A média coloca tudo na mesma proporção e o
# valor aleatório o responsável por bagunçar tudo.
for i in range(len(features)):
    nova[df.drop(columns=['Colour'])[i]] = df.drop(columns=['Colour']).iloc[:,i] + fator_de_ruido*media[i]*aleatorio.iloc[:,i]

for i in range(len(features)):
    nova[features[i]] = df.iloc[:,i] + fator_de_ruido*media[i]*aleatorio.iloc[:,i]
