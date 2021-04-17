import numpy as np #para manipular os vetores
import pandas as pd #para abrir arquivos
from matplotlib import pyplot as plt #para plotar os gráficos
from sklearn.cluster import KMeans #para usar o KMeans
from sklearn.preprocessing import MinMaxScaler #para normalizar

#carregando arquivo
arq = pd.read_csv('../DATASETS/DATASET.csv', sep=';')  

#criando array do arquivo csv
dataset = np.array(arq)

#normalizando array
normalized = MinMaxScaler(feature_range = (50, 200)) #valor para normalizacao
x_norm = normalized.fit_transform(dataset) #normalizando

#parâmetros dpara o k-means
kmeans = KMeans(n_clusters = 4, #numero de clusters
                init = 'random', n_init = 10, #algoritmo que define a posição dos clusters de maneira mais assertiva
                max_iter = 300) #numero máximo de iterações

#montando grupos (clusters)
kmeans.fit(x_norm)

#imprimindo centroides
print(kmeans.cluster_centers_)

#passando imagem (HSV) para predicao
imgjpg = np.array([[140,166,128]])

#predizando os dados para o dataset passado
pred_y = kmeans.predict(x_norm)

#imprime a predição da imagem passada
print(kmeans.predict(imgjpg))

#imprime a predicao para o csv importado
print(pred_y)

plt.scatter(x_norm[:,2], x_norm[:,1], x_norm[:,0], c = pred_y) #posicionamento dos eixos x e y
plt.xlim(0, 255) #range do eixo x
plt.ylim(0, 255) #range do eixo y
plt.grid() #função que desenha a grade no gráfico

#plotando no gráfico as posições de cada centroide
plt.scatter(kmeans.cluster_centers_[:,1],kmeans.cluster_centers_[:,0], s = 100, c = 'red')

plt.gcf().canvas.set_window_title('K-Means')

#mostrar gráfico
plt.show()

