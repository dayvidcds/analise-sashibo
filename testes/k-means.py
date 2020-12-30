import numpy as np #para manipular os vetores
import pandas as pd #para abrir arquivos
from sklearn.cluster import KMeans #para usar o KMeans
from sklearn.preprocessing import MinMaxScaler #para normalizar
from numpy import unique
from numpy import where
from sklearn.datasets import make_classification
from sklearn.cluster import KMeans
from matplotlib import pyplot

#carregando arquivo
arq = pd.read_csv('../DATASETS/dataset2.csv', sep=';')  

#criando array do arquivo csv
dataset = np.array(arq)

#normalizando array
#normalized = MinMaxScaler(feature_range = (50, 200)) #valor para normalizacao
#x_norm = normalized.fit_transform(dataset) #normalizando


model = KMeans(n_clusters=4, random_state=1)
# fit the model
model.fit(dataset)
# assign a cluster to each example

"""#passando imagem (HSV e HSI) para predicao
imgjpg = np.array([[121,	148,	117,	0.186027,	0,	0.507186
]])
print(model.predict(imgjpg))"""

yhat = model.predict(dataset)
# retrieve unique clusters
clusters = unique(yhat)
# create scatter plot for samples from each cluster
for cluster in clusters:
	# get row indexes for samples with this cluster
	row_ix = where(yhat == cluster)
	# create scatter of these samples
	pyplot.scatter(dataset[row_ix, 0], dataset[row_ix, 1])
# show the plot
pyplot.show()

