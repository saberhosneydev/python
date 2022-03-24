import pandas as pd
from sklearn import preprocessing
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import scipy.cluster.hierarchy as shc
from sklearn.cluster import AgglomerativeClustering

colnames = ['surgery', 'age', 'hospital number', 'rectal temperature', 'pulse', 'respiratory rate', 'temperature of extremities', 'peripheral pulse', 'mucous membranes', 'capillary refill time', 'pain', 'peristalsis', 'abdominal distension', 'nasogastric tube',
            'nasogastric reflux', 'nasogastric reflux PH', 'rectal examination', 'abdomen', 'packed cell volume', 'total protein', 'abdominocentesis appearance', 'abdomcentesis total protein', 'outcome', 'surgical lesion', 'lesion type1', 'lesion type2', 'lesion type3', 'pathology data']
catagorical_columns = []
numerical_columns = ['rectal temperature', 'pulse', 'respiratory rate',
                     'nasogastric reflux', 'packed cell volume', 'total protein', 'abdomcentesis total protein']
df = pd.read_csv("dataset/horse-colic.data",
                 sep=' ', names=colnames, header=None)
df.columns.names = ['id']

# df.drop(['Column1', 'Column2', 'Column3', 'Column4'], axis=1, inplace=True)

# Replace missing values with the most frequant value
complete_df = df.copy()
for col in complete_df.columns:
    complete_df[col] = complete_df[col].replace('?', np.nan)
    complete_df[col] = complete_df[col].fillna(complete_df[col].mode()[0])

normalized_df = complete_df.copy()
to_norm = normalized_df.loc[:, numerical_columns]
# col_normalized = (norm-norm.min()) / (norm.max() - norm.min())
x = to_norm.values  # returns a numpy array
min_max_scaler = preprocessing.MinMaxScaler()
x_scaled = min_max_scaler.fit_transform(x)
to_norm = pd.DataFrame(x_scaled)
normalized_df[numerical_columns] = to_norm


refined_df = normalized_df.copy()
x = refined_df
y = refined_df[['outcome']]

kmeans = KMeans(algorithm='auto', copy_x=True, init='random', max_iter=100,
                n_clusters=3, n_init=10,
                random_state=0, tol=0.2, verbose=0)

identified_clusters = kmeans.fit_predict(x)

refined_df['clusters'] = pd.Series(identified_clusters)

# n = 0
# for col in colnames:
#     plt.title(colnames[n])
#     plt.scatter(refined_df[col], refined_df['clusters'] ,c=refined_df['clusters'],cmap='rainbow')
#     plt.figure()
#     n+=1

refined_df_2 = normalized_df.copy()
plt.figure(figsize=(16, 9))
plt.title("Horse Colic Dendograms")
dend = shc.dendrogram(shc.linkage(
    refined_df_2, method='complete'), truncate_mode='lastp')
plt.axhline(y=1, color='r', linestyle='--')
plt.show()

cluster = AgglomerativeClustering(
    n_clusters=3, affinity='euclidean', linkage='ward')
cluster.fit_predict(refined_df_2)
plt.figure(figsize=(10, 7))
m = 0
for col in colnames:
    plt.title(colnames[m])
    plt.scatter(refined_df[col], refined_df['clusters'],
                c=refined_df['clusters'], cmap='rainbow')
    plt.figure()
    plt.show()
    m += 1