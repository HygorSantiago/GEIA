import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
dados = pd.read_csv("C:/Users/mathe/Documents/Estudos Python/train.csv")

df = dados

descrição = df.describe() # descriçôes estatísticas básica dos dados.

correlacao = df.corr() # correlação entre variáveis numéricas.

df.isnull() #  retonar onde tem valores faltantes, False = não tem valores faltantes e True =tem valores faltantes.
df.isnull().sum() # além de fazer o que a funçção acima faz, essa ainda soma os valores faltantes de cada coluna.

#%% excluindo colunas do data frame.

df.drop('Name', axis = 1, inplace = True)
df.drop('Ticket', axis = 1, inplace = True)
df.drop('Cabin', axis = 1, inplace = True)
#essas duas últimas colunas, não sei se vou manter excluído.
df.drop('SibSp', axis = 1, inplace = True)
df.drop('Parch', axis = 1, inplace = True)

df.set_index('PassengerId', inplace = True) #definindo uma coluna como index

#%% subistituindo string por int dentro das colunas

# coluna Sex
df['Sex'].replace('male', 0, inplace = True)
df['Sex'].replace('female', 1, inplace = True)

#coluna Age
df['Age'].fillna(30, inplace = True) #Aqui foi usado uma função para substituir dados faltantes
df['Embarked'].fillna('S', inplace = True)


#%%
sns.countplot(x = df['Survived'])

sobreviventes = df['Survived'].value_counts() #divide as variáveis de acordo com a sua igualdade

#%% sexo das pessoas no navio
sns.countplot(x = dados['Sex'])
df['Sex'].value_counts()

sexo = df['Sex'].value_counts()

#%% portão de embarque dos passageiros
sns.countplot(x = dados['Embarked'])

embarque = df['Embarked'].value_counts()

plt.figure()
lugar_de_embarque = embarque = df.groupby('Survived')['Embarked'].hist(alpha=0.75, grid=False)
plt.title('Distribuição de sobrevivnetes por porto de embarque')
plt.legend(['Mortos', 'Sobreviventes'])
#%% idades

plt.figure(figsize = (20,4))
dados.hist(column='Age')
plt.title('Idade')

mean_0 = dados['Age'].mean()
median_0 = dados['Age'].median()
std_0 = dados['Age'].std()
count_0 = dados['Age'].count()

Idade = df['Age'].value_counts()

plt.figure()
plt.hist(df['Age'])
plt.ylim(0, 190)
plt.title('Distribuição geral de idades')
plt.xlabel('Idades')

plt.figure()
sobrevivente_idade = df.groupby('Survived')['Age'].hist(alpha=0.75) # alpha determina a transparência do gráfico.
plt.grid(False)
plt.ylim(0, 190)
plt.legend(['Mortos', 'Sobreviventes']) # adiciona uma legenda quando há mais de um gráfico no mesmo plot.
plt.title('Distribuição de idades em relação aos sobreviventes')
plt.xlabel('Idades')

#%% tarifas pagas pelos passageiros
plt.figure()
plt.plot(dados['Fare'])
plt.title('Tarifa do passageiro')

plt.figure()
plt.hist(dados['Fare'],bins = 100)
plt.title('Tarifa do passageiro')

plt.figure(figsize = (45,4))
plt.xticks(rotation = 90)
sns.countplot(x = dados['Fare'])

#
plt.figure()
plt.boxplot(df['Fare'], vert=False) # vert determina de o gráfico ficará na vertical ou na horizontal.
plt.title('Distribuição de valores da passagem (Eixo x limitado)')
plt.xlim(0, 100)
plt.yticks([]) # remove os rótulos do eixo y

plt.figure()
plt.subplot(2,1,1)
plt.suptitle('Distribuição de valores da passagem')
plt.hist(df['Fare'])
plt.ylim(0,800)
plt.xticks([]) # determina os rótulos de x no gráfico. no caso ele terá valores de 0 a 550, com saltos de 60 unidades.

# Agrupa os dados pela coluna sobreviventes e gera o histograma das imagens.
plt.subplot(2,1,2)
df.groupby('Survived')['Fare'].hist(alpha=0.75) # alpha determina a transparência do gráfico.
plt.grid(False)
plt.ylim(0,800)
plt.xticks([x for x in range(0,600,30)], rotation=90) # rotation rotaciona os rótulos do eixo em x graus.
plt.legend(['Mortos', 'Sobreviventes']) # adiciona uma legenda quando há mais de um gráfico no mesmo plot.
plt.xlabel('Valor da passagem')



#%%sexo das pessoas no navio
sns.countplot(x = dados['Sex'])
df['Sex'].value_counts()

#%% sexo e mortalidade.
# filtra os dados (sex=male) e retorna a coluna survived.
homens_sobrevivencia = df.loc[df['Sex'] == 0, 'Survived']

# filtra os dados (sex=female) e retorna a coluna survived.
mulheres_sobrevivencia = df.loc[df['Sex'] == 1, 'Survived']

#tais informações podem ser visualizadas num gráfico de barras. Contudo, devemos usar antes a função value_counts()
vc_homens_sobrevivencia = homens_sobrevivencia.value_counts()
vc_mulheres_sobrevivencia = mulheres_sobrevivencia.value_counts()

plt.figure()
plt.suptitle("Número de sobreviventes em relação ao sexo")
plt.subplot(1,2,1) # subplot com uma linha, e duas colunas. o gráfico ficará na primeira posição.
plt.bar(x = vc_homens_sobrevivencia.index, height = vc_homens_sobrevivencia.values)
plt.ylim(0,500)
plt.xticks([0,1],['Mortos','Sobreviventes'])
plt.title('Homens')

plt.subplot(1,2,2) # subplot com uma linha, e duas colunas. o gráfico ficará na segunda posição.
plt.bar(x=vc_mulheres_sobrevivencia.index, height=vc_mulheres_sobrevivencia.values, color='pink') # color muda a cor do gráfico
plt.ylim(0, 500)
plt.xticks([0,1], ['Mortas', 'Sobreviventes'])
plt.yticks([]) # remove os rótulos do eixo y
plt.title('Mulheres')

#%% classe que os passageiros navegaram
sns.countplot(x = dados['Pclass'])

df['Pclass'].value_counts()
Passageiros_na_primeira_classe = (100*216)/891 # podeira ter usado o value_counts(), ele seria mais certeiro.
Passageiros_na_segunda_classe = (100*184)/891
Passageiros_na_terceira_classe = (100*491)/891

plt.figure()
plt.subplot(1,2,1)
classe = df['Pclass'].value_counts().sort_index() # sort_index() organiza os indices.
plt.pie(classe, autopct='%1.1f%%')
plt.legend(['1° classe','2° classe','3° classe'], loc='center left', bbox_to_anchor=(1, 0.5))
plt.title('Porcentagem de passageiros em relação a classe')

plt.subplot(2, 1, 2)
sobreviventes = df.loc[df['Survived'] == 1, 'Pclass'].value_counts().sort_index()#sort_index() organiza os indices.
plt.pie(sobreviventes, autopct='%1.1f%%')
plt.legend(['1° classe','2° classe','3° classe'], loc='center left', bbox_to_anchor=(1, 0.5))
plt.title('Porcentagem de sobreviventes em relação a classe')


#%% machine learn

# pre-processamento dos dados para realizar o machine learn

Embarke_dummies = pd.get_dummies(df['Embarked']) #atribuições matemáticas que vão deixar a coluna Embarked de mais fácil entendimento para o algoritimo de machine learn. 

df_machine_learn = pd.concat([df,Embarke_dummies],axis = 1) #junta um dataframe ao outro.

df_machine_learn.drop('Embarked', axis = 1, inplace = True) #excluí a coluna embarked porque eu separei ela no get_dummies.

#árvore de decisão

from sklearn.tree import DecisionTreeClassifier # modelo de machine learn árvore de decisão.
from sklearn import tree #para derar a imagem da árvore decisão.

x = df_machine_learn.drop(columns=['Survived'])
y = df_machine_learn['Survived']

modelo_1 = DecisionTreeClassifier(criterion = 'entropy', max_depth = 4, splitter = 'random' , random_state = 0) #forma da qual estou usando a árvore de decisão.
                                
modelo_1.fit(x,y) # treinando o modelo para gerar resultados.

modelo_1.feature_importances_ # mostra a importância de cada variável.

tree.plot_tree(modelo_1) #para gerar a imagem da árvore decisão.

previsoes = modelo_1.predict(x)


from sklearn.metrics import accuracy_score, confusion_matrix #para medir a acuracia e a matrix de confusão do modelo.

previsoes = modelo_1.predict(x)

accuracy_score(df['Survived'], previsoes) # testando a acuracia do modelo.
Matriz_Confusao = confusion_matrix (y,previsoes) # conferindo a matrix de confusão do modelo

#separando a árvore de decisão em modelo de teste e treino, para evitar problemas de overfiting.

from sklearn.model_selection import train_test_split #divide o modelo em modelo de teste e treino.
[x_train, x_test, y_train, y_test] = train_test_split( x,y, test_size = 0.2 )

modelo_2 = DecisionTreeClassifier(criterion = 'entropy',random_state = 0)
modelo_2.fit(x_train,y_train)
previsoes_2 = modelo_2.predict(x_test)
accuracy_score(y_test, previsoes_2)
Matriz_Confusao_2 = confusion_matrix (y_test,previsoes_2)

tree.plot_tree(modelo_2)

# modelo de decisão rando forest.

from sklearn.ensemble import RandomForestClassifier # modelo de machine random forest.
[x_train, x_test, y_train, y_test] = train_test_split( x,y, test_size = 0.2 )
random_forest_df = RandomForestClassifier(n_estimators = 10, criterion = 'entropy', max_features = None,random_state = 0)
random_forest_df.fit(x_train, y_train)
modelo_3 = random_forest_df.predict(x_test)
accuracy_score(y_test, modelo_3)
Matriz_Confusao_3 = confusion_matrix (y_test,modelo_3)

# modelo de decisão extra tree.

from sklearn.ensemble import ExtraTreesClassifier # modelo de machine learn extra tree.
[x_train, x_test, y_train, y_test] = train_test_split( x,y, test_size = 0.2 )
extra_tree_df = ExtraTreesClassifier(criterion = 'entropy', max_features = None)
extra_tree_df.fit(x_train, y_train)
modelo_4  = extra_tree_df.predict(x_test)
accuracy_score(y_test, modelo_4)
Matriz_Confusao_4 = confusion_matrix (y_test,modelo_4)

# usando a função grid para encontrar os melhores parametros

from sklearn.model_selection import GridSearchCV # funcão para escolher os melhores parametros do modelo.

# melhores parametros DecisionTreeClassifier()
params = {'max_depth':[2,3,4,5,6,7,8],
          'criterion':['gini','entropy'],
          'class_weight':[None,'balanced'],
          'splitter': ['best', 'random']}

grid_search = GridSearchCV(estimator = DecisionTreeClassifier(),param_grid = params)

grid_search.fit(x,y)

melhores_parametros_DecisionTreeClassifier = grid_search.best_params_
melhor_resultado_DecisionTreeClassifier = grid_search.best_score_

# melhores parametros RandomForestClassifier

params_2 = {'criterion':['gini', 'entropy', 'log_loss'], 
            'max_features':['sqrt', 'log2', None]}

grid_search_2 = GridSearchCV(estimator = RandomForestClassifier(),param_grid = params_2)

grid_search_2.fit(x,y)

melhores_parametros_RandomForestClassifier = grid_search_2.best_params_
melhor_resultado_RandomForestClassifier = grid_search_2.best_score_

# melhores parametros ExtraTreesClassifier
params_3 = {'criterion':['gini', 'entropy', 'log_loss'],
            'max_features':['sqrt', 'log2', None]}

grid_search_3 = GridSearchCV(estimator = ExtraTreesClassifier(),param_grid = params_3)

grid_search_3.fit(x,y)

melhores_parametros_ExtraTreesClassifier = grid_search_3.best_params_
melhor_resultado_ExtraTreesClassifier = grid_search_3.best_score_


#cross_validation
from sklearn.model_selection import cross_val_score

scores = cross_val_score(modelo_1, x, y, cv = 5, scoring = 'accuracy')

#knn
from sklearn.neighbors import KNeighborsClassifier

knn_modelo = KNeighborsClassifier(n_neighbors = 5, metric = 'minkowski', p = 2)
knn_modelo.fit(x,y)

modelo_5  = knn_modelo.predict(x)
accuracy_score(y, modelo_5)
Matriz_Confusao_5 = confusion_matrix (y,modelo_5)

#melhores parametros para knn
params_4 = {'n_neighbors':[1,2,3,4,5,6,7,8,9,10]}

grid_search_4 = GridSearchCV(estimator = KNeighborsClassifier(),param_grid = params_4)

grid_search_4.fit(x,y)

melhores_parametros_KNeighborsClassifier = grid_search_4.best_params_
melhor_resultado_KNeighborsClassifier = grid_search_4.best_score_

















































