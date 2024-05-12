# Analysis of the Iris Data Set. 
# Author Jennifer Ibanez Cano


import numpy as np
import pandas as pd

# Loaad the data
df = pd.read_csv('iris.data.txt')

# Check the data
print(df)

# Check the different types of the variables. 

print(df.dtypes)

# check the number of flowers per species

print(df['species'].value_counts())


# check the mean of the petal length of each 3 types of flowers. 

Iris_setosa_df = df.loc[df['species'] == 'Iris-setosa', ['petal_length']]
out = Iris_setosa_df.groupby('petal_length').mean()
print('Iris_setosa')
print(out)
print()

Iris_virginica_df = df.loc[df['species'] == 'Iris-virginica', ['petal_length']]
out = Iris_virginica_df.groupby('petal_length').mean()
print('Iris_virginica')
print(out)
print()

Iris_versicolor_df = df.loc[df['species'] == 'Iris-versicolor', ['petal_length']]
out = Iris_versicolor_df.groupby('petal_length').mean()
print('Iris_versicolor')
print(out)
print()