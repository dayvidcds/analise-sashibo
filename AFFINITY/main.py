#Affinity Propagation para clusterização e comparação com o k-means

from numpy import unique
from numpy import where

from sklearn.cluster import AffinityPropagation
from matplotlib import pyplot

import numpy as np #para manipular os vetores

import pandas as pd #para abrir arquivos
from matplotlib import pyplot as plt #para plotar os gráficos
from sklearn.cluster import KMeans #para usar o KMeans
from sklearn.preprocessing import MinMaxScaler #para normalizar
from sklearn.cluster import AffinityPropagation

#carregando arquivo
arq = pd.read_csv('dataset2.csv', sep=';')  

#criando array do arquivo csv
dataset = np.array(arq)

#normalizando array
normalized = MinMaxScaler(feature_range = (50, 200)) #valor para normalizacao
x_norm = normalized.fit_transform(dataset) #normalizando


#montando grupos (clusters)
model = AffinityPropagation(damping=0.9)
model.fit(x_norm)

imgjpg = np.array([[140,166,128]])

# assign a cluster to each example
yhat = model.predict(x_norm)

print(model.cluster_centers_)

print(model.predict(imgjpg))

# retrieve unique clusters
clusters = unique(yhat)
# create scatter plot for samples from each cluster
plt.scatter(x_norm[:, 2], x_norm[:, 1], x_norm[:, 0], c = yhat)
# show the plot
plt.scatter(model.cluster_centers_[:,1],model.cluster_centers_[:,0], s = 200, c = 'red')

plt.grid()

plt.gcf().canvas.set_window_title('Affinity')

plt.show()