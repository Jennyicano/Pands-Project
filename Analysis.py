# Analysis of the Iris Data Set. 
# Author Jennifer Ibanez Cano

# For data frames, I'll need to import pandas.
import pandas as pd

# For numerical, I'll need to import numpy.
import numpy as np

# For plotting, I'll need to import matplotlib.pyplot.
import matplotlib.pyplot as plt

# Loaad the data
df = pd.read_csv('iris.data.txt')

# I'll add 'print()' after every function to leave an empty newline, 
# suing this when I run the program the terminal will show an empty line 
# to separete the variables text.

# Check the data
print(df)
print()

# Check the different types of the variables. 

print(df.dtypes)
print()

# Describe the data set

print(df.describe())
print()

# Output a sumary of each variable to a single text. 

# Check the number of flowers per species. 

print(df['species'].value_counts())
print()

# For the following variables I'm using .groupby and the function mean to have 
# the numbers in groups of different flowers and the mean of each variable. 

# Check the petal width mean by specie.

petal_w = df.groupby('species')['petal_width'].mean()
print(petal_w)
print()

# Check the petal length mean by specie.

petal_l = df.groupby('species')['petal_length'].mean()
print(petal_l)
print()

# Check the sepal width mean by specie.

sepal_w = df.groupby('species')['sepal_width'].mean()
print(sepal_w)
print()

# Check the sepal length mean by specie.

sepal_l = df.groupby('species')['sepal_length'].mean()
print(petal_l)

# Histograms of each variale, the histograms will be save to a png files. 

# Plotting the histogram of the diferent species. 

species = df['species']

plt.hist(species, bins=5, color='purple', edgecolor='black')
plt.xlabel('Species')
plt.ylabel('Quantity')
plt.title('Iris flowers')
plt.show()