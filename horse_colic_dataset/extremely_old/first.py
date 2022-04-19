import pandas as pd
import numpy as np

# cOOl function


def isnan(num):
    return num != num


colnames = ['surgery', 'age', 'hospital number', 'rectal temperature', 'pulse', 'respiratory rate', 'temperature of extremities', 'peripheral pulse', 'mucous membranes', 'capillary refill time', 'pain', 'peristalsis', 'abdominal distension', 'nasogastric tube',
            'nasogastric reflux', 'nasogastric reflux PH', 'rectal examination', 'abdomen', 'packed cell volume', 'total protein', 'abdominocentesis appearance', 'abdomcentesis total protein', 'outcome', 'surgical lesion', 'lesion type1', 'lesion type2', 'lesion type3', 'pathology data']
df = pd.read_csv("dataset/horse-colic.data", sep=' ',
                 names=colnames, header=None)
df.columns.names = ['id']

# Replace missing values with the column's mean
for col in df.columns:
    df[col] = df[col].replace(np.NaN, df[col].mean())

normalized_df = df.copy()
columns_to_normalize = ['rectal temperature', 'pulse', 'respiratory rate',
                        'nasogastric reflux', 'packed cell volume', 'total protein', 'abdomcentesis total protein']
x = normalized_df.loc[:, columns_to_normalize]
col_normalized = (x-x.min()) / (x.max() - x.min())
normalized_df[columns_to_normalize] = col_normalized
print(normalized_df.isnull().sum())
