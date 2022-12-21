# Classificação de imagens com Algoritmo de Canny + kNN

## Uma breve introdução
Com intuito de classificar imagens, foi criada uma arquitetura baseada no Algoritmo de Canny e no kNN. O Algoritmo de Canny foi aplicado as imagens dos bancos **fashion-mnist, mnist e cifar-10**, com intuito de reduzir o ruído destas, e posteriormente as imagens foram classificadas utilizando o kNN. Os hiperparâmetros de ambos algoritmos foram definidos de forma arbitrária.

Detalhes sobre os bancos de dados citados acima podem ser obtidos na documentação do keras.

##Resultados
Para cada banco de dados, a arquitetura obteve as seguintes porcentagens de acerto (acurácia).
|  Banco de dados   |  Acurácia   |
| ----------------- | ----------- |
|  mnist            |  88%        |
|  fashion-mnist    |  79%        |
|  cifar-10         |  14%        |

Atraves da análise da matriz de confusão (disponível ao rodar o código) e da acurácia é possível observar o bom funcionamento da arquitetura para imagens simples, ou seja, com poucos contornos. Um exemplo disso é a elevada acurácia obtida no banco de dados mnist. Contudo, imagens complexas, ou seja, com muitos contornos, tendem a ser classificadas mais frequentemente, afetando assim o desempenho do modelo. Podemos observar isso analisando o desempenho da arquitetura ao lidar com o fashion-mnist, tendo a classe 'skirt' sendo predita erroneamente mais vezes. Contudo, tal comportamento é evidenciado com maior força no banco de dados cifar-10, onde a maioria das imagens são classificadas como da classe 'deer', comprometendo de forma crítica o desempenho do modelo.

## Próximos passos
* Ajuste dos hiperparâmetros;
* Comparação com outros modelos;
* Avaliação do desempenho em bancos de dados reduzidos;
* Avaliação do impacto de mudanças no pré-processamento.
