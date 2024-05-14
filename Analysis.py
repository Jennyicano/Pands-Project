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
print(sepal_l)

# Histograms of each variale, the histograms will be save to a png files. 

# Plotting the histogram of the diferent species. 

species = df['species']

plt.hist(species, bins=5, color='purple', edgecolor='black')
plt.xlabel('Species')
plt.ylabel('Quantity')
plt.title('Iris flowers')
plt.savefig('Species_hist.png')
plt.show()

# Plotting the histogram of the petal width. 

petal_w = df['petal_width']
print(petal_w)
print()

plt.hist(petal_w, bins=5, color='blue', edgecolor='black', alpha=0.7, rwidth=0.78)
plt.xlabel('Petal width')
plt.ylabel('')
plt.title('Petal width of Iris flowers')
plt.savefig('Petal width_hist.png')
plt.show()

# Plotting the histogram of the petal length. 

petal_l = df['petal_length']
print(petal_l)
print()

plt.hist(petal_l, bins=5, color='green', edgecolor='black', alpha=0.7, rwidth=0.78)
plt.xlabel('Petal Length')
plt.ylabel('')
plt.title('Petal length of Iris flowers')
plt.savefig('Petal length_hist.png')
plt.show()

# Plotting the histogram of the sepal width.

sepal_w = df['sepal_width']
print(sepal_w)
print()

plt.hist(sepal_w, bins=5, color='magenta', edgecolor='black', alpha=0.7, rwidth=0.78)
plt.xlabel('Sepal width')
plt.ylabel('')
plt.title('Sepal width of Iris flowers')
plt.savefig('Sepal width_hist.png')
plt.show()

# Plotting the histogram of the sepal length. 

sepal_l = df['sepal_length']
print(sepal_l)
print()

plt.hist(sepal_l, bins=5, color='orange', edgecolor='black', alpha=0.7, rwidth=0.78)
plt.xlabel('Sepal length')
plt.ylabel('')
plt.title('Sepal length of Iris flowers')
plt.savefig('Sepal length_hist.png')
plt.show()

# Output a scatter plot of each pair of variables. 

# The first scatter plot is with the variables: pental length and pental width. 

# To start I'll get the data of the variables
species = df['species']
petal_l = df['petal_length']
petal_w = df['petal_width']

# I'll asign diferent colors and shapes(using thr formar as markers) for the different species of Iris flowers, 
# to disting the different between each others
colors = ['purple', 'yellow', 'blue']
markers = ['s', 'p', 'D']

# I'm using the markers: 's' as square, 'p' as pentagon, and 'D' as diamond shape.

# Create a scatter plot.
plt.figure(figsize=(0,150))
for i in enumerate(species):
    species_df = df[df['species'] == species]
    plt.scatter(species_df['petal_length'], species_df['petal_width'], 
                color=colors, marker=markers, label=species, alpha=0.7)

# Axis labels.
plt.xlabel('petal_length')
plt.ylabel('petal_widht')

# Title.
plt.title('Scatter plot of petal length and petal widht by species', color='purple')
plt.legend()

# X limits.
plt.xlim(0, 8)

# Y limits.
plt.ylim(0, 4)

plt.show()