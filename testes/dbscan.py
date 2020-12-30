from numpy import unique
from numpy import where
from sklearn.cluster import DBSCAN
from matplotlib import pyplot
import numpy as np #para manipular os vetores
import pandas as pd #para abrir arquivos
from sklearn.preprocessing import MinMaxScaler #para normalizar

arq = pd.read_csv('../DATASETS/dataset2.csv', sep=';')   
dataset = np.array(arq)

normalized = MinMaxScaler(feature_range = (50, 200)) #valor para normalizacao
x_norm = normalized.fit_transform(dataset) #normalizando

# define the model
model = DBSCAN(eps=0.30, min_samples=9)

# fit model and predict clusters
yhat = model.fit_predict(x_norm)

# retrieve unique clusters
clusters = unique(yhat)
# create scatter plot for samples from each cluster
for cluster in clusters:
	# get row indexes for samples with this cluster
	row_ix = where(yhat == cluster)
	# create scatter of these samples
	pyplot.scatter(x_norm[row_ix, 0], x_norm[row_ix, 1], c = row_ix)
# show the plot
pyplot.show()