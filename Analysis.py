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

# Describe the data set

print(df.describe())

# Output a sumary of each variable to a single text. 

# Check the number of flowers per species. 

print(df['species'].value_counts())

# For the following variables I'm using .groupby and the function mean to have 
# the numbers in groups of different flowers and the mean of each variable. 
# Check the petal width mean by specie.

petal_w = df.groupby('species')['petal_width'].mean()
print(petal_w)

# Check the petal length mean by specie.

petal_l = df.groupby('species')['petal_length'].mean()
print(petal_l)

# Check the sepal width mean by specie.

sepal_w = df.groupby('species')['sepal_width'].mean()
print(sepal_w)

# Check the sepal length mean by specie.

sepal_l = df.groupby('species')['sepal_length'].mean()
print(petal_l)