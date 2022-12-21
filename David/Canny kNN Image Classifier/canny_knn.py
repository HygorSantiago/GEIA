# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 04:24:57 2022

Classificação de imagens usando Algoritmo de Canny e kNN.

@author: David Rodrigues
"""

from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from keras.datasets import fashion_mnist, mnist, cifar10
from matplotlib import pyplot as plt
import numpy as np
import cv2 as cv
import pandas as pd
import time

class canny_knn():
    # classificação de imagens com knn e pré-processamento com algoritmo de detecção de bordas de canny
    
    def __init__(self, t_min, t_max, n_neighbors=5, metric='euclidean'):
        # variáveis do objeto
        self.t_min = t_min
        self.t_max = t_max
        self.n_neighbors = n_neighbors
        self.metric = metric
        
    def processar(self, arr_img):
        # processamento das imagens.
        list_flatted = []
        list_img = []
        # obtém apenas os contornos e transforma as matrizes em vetores n-dimensionais
        for img in arr_img:
            new_img = cv.Canny(img,self.t_min,self.t_max)
            list_img.append(new_img)
            # imagens achatadas
            flatted_img = np.array(new_img).flatten()
            list_flatted.append(flatted_img)
        # transforma as listas em array numpy
        np_flatted = np.array(list_flatted)
        np_img = np.array(list_img)
        # retorna o conjunto achatado
        return np_flatted, np_img
    
    def treinar(self, x_train, y_train):
        # treina o modelo e o retorna
        self.neigh = KNeighborsClassifier(n_neighbors=self.n_neighbors, metric=self.metric)
        self.neigh.fit(x_train, y_train)
        # retorna o modelo treinado
        return self.neigh
    
    def classificar(self, x_pred):
        # efetua as predições
        list_pred = self.neigh.predict(x_pred)
        self.np_pred = np.array(list_pred)
        # retorna as valores preditos
        return self.np_pred
    
    def avaliar(self, y_true, labels=None):
        # acurácia do modelo
        acc_score = accuracy_score(y_true, self.np_pred)
        # matriz de confusão
        confusion = confusion_matrix(y_true, self.np_pred)
        if labels != None:
            confusion = pd.DataFrame(confusion, index=labels, columns=labels)

        # retorna a acurácia e a matriz de confusão
        return acc_score, confusion
    
# parâmetros usados no teste
t_min = 300
t_max = 350
vizinhos = 10
metrica = 'euclidean'

#%% análise 1: fashion mnist   
    
# carrega o banco fashion_mnist
fm = fashion_mnist.load_data()
# imagens pré-processadas
pp_img = canny_knn(t_min, t_max).processar(fm[0][0][:10])
# imagens antes e depois do processamento
for (index, img) in enumerate(fm[0][0][:10]):
    plt.figure()
    plt.subplot(121),plt.imshow(pp_img[1][index],cmap = 'gray')
    plt.title('Bordas'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(img,cmap = 'gray')
    plt.title('Imagem'), plt.xticks([]), plt.yticks([])

# rótulos ordenados das imagens
labels = ('T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot')

x_train = fm[0][0]
y_train = fm[0][1]

x_test = fm[1][0]
y_test = fm[1][1]

# inicio da aplicação da arquitetura
start = time.time()
# criação do modelo
cknn = canny_knn(t_min, t_max, vizinhos, metrica)
# processamento dos dados
x_train = cknn.processar(x_train)[0]
x_test = cknn.processar(x_test)[0]
# treina o modelo
cknn.treinar(x_train, y_train)
# avalia o modelo
cknn.classificar(x_test)
# fim da aplicação da arquitetura
end = time.time()

# tempo total gasto
tempo_fm = end - start
# desempenho da arquitetura
avalicacao_fm = cknn.avaliar(y_test, labels)

print('tempo fashion-mnist: '+str(tempo_fm)+'s')

#%% análise 2: mnist
    
# carrega o banco mnist
mnist = mnist.load_data()
# imagens pré-processadas
pp_img = canny_knn(t_min, t_max).processar(mnist[0][0][:10])
# imagens antes e depois do processamento
for (index, img) in enumerate(mnist[0][0][:10]):
    plt.figure()
    plt.subplot(121),plt.imshow(pp_img[1][index],cmap = 'gray')
    plt.title('Bordas'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(img,cmap = 'gray')
    plt.title('Imagem'), plt.xticks([]), plt.yticks([])
    
# rótulos ordenados das imagens
labels = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

x_train = mnist[0][0]
y_train = mnist[0][1]

x_test = mnist[1][0]
y_test = mnist[1][1]

# inicio da aplicação da arquitetura
start = time.time()
# criação do modelo
cknn = canny_knn(t_min, t_max, vizinhos, metrica)
# processamento dos dados
x_train = cknn.processar(x_train)[0]
x_test = cknn.processar(x_test)[0]
# treina o modelo
cknn.treinar(x_train, y_train)
# avalia o modelo
cknn.classificar(x_test)
# fim da aplicação da arquitetura
end = time.time()

# tempo total gasto
tempo_mnist = end - start
# desempenho da arquitetura
avalicacao_mnist = cknn.avaliar(y_test, labels)

print('tempo mnist: '+str(tempo_mnist)+'s')

#%% análise 3: cifar100
    
# carrega o banco cifar10
cifar = cifar10.load_data()
# imagens pré-processadas
pp_img = canny_knn(t_min, t_max).processar(cifar[0][0][:10])
# imagens antes e depois do processamento
for (index, img) in enumerate(cifar[0][0][:10]):
    plt.figure()
    plt.subplot(121),plt.imshow(pp_img[1][index],cmap = 'gray')
    plt.title('Bordas'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(img,cmap = 'gray')
    plt.title('Imagem'), plt.xticks([]), plt.yticks([])

# rótulos ordenados das imagens
labels = ('airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck')

x_train = cifar[0][0]
y_train = cifar[0][1]

x_test = cifar[1][0]
y_test = cifar[1][1]

# inicio da aplicação da arquitetura
start = time.time()
# criação do modelo
cknn = canny_knn(t_min, t_max, vizinhos, metrica)
# processamento dos dados
x_train = cknn.processar(x_train)[0]
x_test = cknn.processar(x_test)[0]
# treina o modelo
cknn.treinar(x_train, y_train)
# avalia o modelo
cknn.classificar(x_test)
# fim da aplicação da arquitetura
end = time.time()

# tempo total gasto
tempo_cifar = end - start
# desempenho da arquitetura
avalicacao_cifar = cknn.avaliar(y_test, labels)

print('tempo cifar: '+str(tempo_cifar)+'s')