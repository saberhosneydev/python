import pandas as pd
import random


def isnan(num):
    return num != num


colnames = ['surgery', 'age', 'hospital number', 'rectal temperature', 'pulse', 'respiratory rate', 'temperature of extremities', 'peripheral pulse', 'mucous membranes', 'capillary refill time', 'pain', 'peristalsis', 'abdominal distension', 'nasogastric tube',
            'nasogastric reflux', 'nasogastric reflux PH', 'rectal examination', 'abdomen', 'packed cell volume', 'total protein', 'abdominocentesis appearance', 'abdomcentesis total protein', 'outcome', 'surgical lesion', 'lesion type1', 'lesion type2', 'lesion type3', 'pathology data']
df = pd.read_csv("data/horse-colic.data", sep=' ', names=colnames, header=None)
df.columns.names = ['id']

# Fill the missing values in abdominocentesis appearance column based on range specified by dataset creator
for index, value in df['abdominocentesis appearance'].iteritems():
    if isnan(value):
        df.at[index, 'abdominocentesis appearance'] = random.choice(range(1, 3, 1))
# Fill the missing values in abdominocentesis total protein column based on range specified by dataset creator
for index, value in df['abdomcentesis total protein'].iteritems():
    if isnan(value):
        df.at[index, 'abdomcentesis total protein'] = random.uniform(0.0, 7.4)
# Fill the missing values in outcome column based on range specified by dataset creator
for index, value in df['outcome'].iteritems():
    if isnan(value):
        df.at[index, 'outcome'] = random.randrange(1, 3, 1)
# Fill the missing values in total protein column based on range specified by dataset creator
for index, value in df['total protein'].iteritems():
    if isnan(value):
        df.at[index, 'total protein'] = random.uniform(6, 7.5)
# Fill the missing values in packed cell volume column based on range specified by dataset creator
for index, value in df['packed cell volume'].iteritems():
    if isnan(value):
        df.at[index, 'packed cell volume'] = random.randrange(30, 50, 1)
# Fill the missing values in abdomen column based on range specified by dataset creator
for index, value in df['abdomen'].iteritems():
    if isnan(value):
        df.at[index, 'abdomen'] = random.randrange(1, 5, 1)
# Fill the missing values in outcome column based on range specified by dataset creator
for index, value in df['rectal examination'].iteritems():
    if isnan(value):
        df.at[index, 'rectal examination'] = random.randrange(1, 4, 1)
# Fill the missing values in nasogastric reflux PH column based on range specified by dataset creator
for index, value in df['nasogastric reflux PH'].iteritems():
    if isnan(value):
        df.at[index, 'nasogastric reflux PH'] = random.randrange(0, 14, 1)
# Fill the missing values in nasogastric reflux column based on range specified by dataset creator
for index, value in df['nasogastric reflux'].iteritems():
    if isnan(value):
        df.at[index, 'nasogastric reflux'] = random.randrange(1, 3, 1)
# Fill the missing values in nasogastric tube column based on range specified by dataset creator
for index, value in df['nasogastric tube'].iteritems():
    if isnan(value):
        df.at[index, 'nasogastric tube'] = random.randrange(1, 3, 1)
# Fill the missing values in abdominal distension column based on range specified by dataset creator
for index, value in df['abdominal distension'].iteritems():
    if isnan(value):
        df.at[index, 'abdominal distension'] = random.randrange(1, 4, 1)
# Fill the missing values in peristalsis column based on range specified by dataset creator
for index, value in df['peristalsis'].iteritems():
    if isnan(value):
        df.at[index, 'peristalsis'] = random.randrange(1, 4, 1)
# Fill the missing values in pain column based on range specified by dataset creator
for index, value in df['pain'].iteritems():
    if isnan(value):
        df.at[index, 'pain'] = random.randrange(1, 5, 1)
# Fill the missing values in capillary refill time column based on range specified by dataset creator
for index, value in df['capillary refill time'].iteritems():
    if isnan(value):
        df.at[index, 'capillary refill time'] = random.randrange(1, 2, 1)
# Fill the missing values in mucous membranes column based on range specified by dataset creator
for index, value in df['mucous membranes'].iteritems():
    if isnan(value):
        df.at[index, 'mucous membranes'] = random.randrange(1, 6, 1)
# Fill the missing values in peripheral pulse column based on range specified by dataset creator
for index, value in df['peripheral pulse'].iteritems():
    if isnan(value):
        df.at[index, 'peripheral pulse'] = random.randrange(1, 4, 1)
# Fill the missing values in temperature of extremities column based on range specified by dataset creator
for index, value in df['temperature of extremities'].iteritems():
    if isnan(value):
        df.at[index, 'temperature of extremities'] = random.randrange(1, 4, 1)
# Fill the missing values in respiratory rate column based on range specified by dataset creator
for index, value in df['respiratory rate'].iteritems():
    if isnan(value):
        df.at[index, 'respiratory rate'] = random.randrange(6, 12, 1)
# Fill the missing values in pulse column based on range specified by dataset creator
for index, value in df['pulse'].iteritems():
    if isnan(value):
        df.at[index, 'pulse'] = random.randrange(25, 40, 1)
# Fill the missing values in rectal temperature column based on range specified by dataset creator
for index, value in df['rectal temperature'].iteritems():
    if isnan(value):
        df.at[index, 'rectal temperature'] = random.uniform(37.0, 39.0)
# Fill the missing values in surgery column based on range specified by dataset creator
for index, value in df['surgery'].iteritems():
    if isnan(value):
        df.at[index, 'surgery'] = random.randrange(1, 2, 1)
print("Null values:")
print(df.isnull().sum())



normalized_df = df.copy()
columns_to_normalize = ['rectal temperature', 'pulse', 'respiratory rate',
                        'nasogastric reflux', 'packed cell volume', 'total protein', 'abdomcentesis total protein']
x = normalized_df.loc[:, columns_to_normalize]
col_normalized = (x-x.min()) / (x.max() - x.min())
normalized_df[columns_to_normalize] = col_normalized
print(normalized_df)
