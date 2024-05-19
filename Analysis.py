# Analysis of the Iris data Set. 
# Author Jennifer Ibanez Cano

# Below you can find the program that perfirm my analysis of the Iris data set. 

# For data frames, I'll need to import pandas.
import pandas as pd

# For numerical, I'll need to import numpy.
import numpy as np

# For plotting, I'll need to import matplotlib.pyplot.
import matplotlib.pyplot as plt

# Seaborn. 

import seaborn as sns 

# Load the data.
# df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
df = pd.read_csv('iris.data.csv')


# I'll add 'print()' after every function to leave an empty newline, so when I run the program the terminal will show an empty line 
# to separete the variables text.

# Check the data.
print(df)
print()

# Check the different types of the variables. 

print(df.dtypes)
print()

# Describe the data set.

print(df.describe())
print()

# Output a sumary of each variable to a single text. 

f=open("summary.txt","w")  # I create a text file and will overwrite any existing content.

# Check the number of flowers per species. 
f.write("Summary of species")
# I add a newline to the text file I'm writing to
f.write("\n")
f.write(df['species'].value_counts().to_string())
f.write("\n")
f.write("\n")

#I print it on the terminal also
print(df['species'].value_counts())
print()

# For the following variables I'm using .groupby and the function mean to have 
# the numbers in groups of different flowers and the mean of each variable. 

# Check the petal width mean by species.

petal_w = df.groupby('species')['petal_width'].mean()
print(petal_w)
print()

f.write("Petal width (cm) mean by species")
f.write("\n")
f.write(petal_w.to_string())
f.write("\n")
f.write("\n")

# Check the petal length mean by specie.

petal_l = df.groupby('species')['petal_length'].mean()
print(petal_l)
print()

f.write("Petal length (cm) mean by species")
f.write("\n")
f.write(petal_l.to_string())
f.write("\n")
f.write("\n")

# Check the sepal width mean by specie.

sepal_w = df.groupby('species')['sepal_width'].mean()
print(sepal_w)
print()

f.write("Sepal width (cm) mean by species")
f.write("\n")
f.write(petal_w.to_string())
f.write("\n")
f.write("\n")

# Check the sepal length mean by specie.

sepal_l = df.groupby('species')['sepal_length'].mean()
print(sepal_l)

f.write("Sepal length (cm) mean by species")
f.write("\n")
f.write(petal_w.to_string())
f.write("\n")
f.write("\n")

# I close the file text.
f.close()

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

plt.hist(petal_w, bins=10, color='blue', edgecolor='black', alpha=0.7, rwidth=0.78)
plt.xlabel('Petal width (cm)')
plt.ylabel('')
plt.title('Petal width (cm) of Iris flowers')
plt.savefig('Petal width_hist.png')
plt.show()

# Plotting the histogram of the petal length. 

petal_l = df['petal_length']
print(petal_l)
print()

plt.hist(petal_l, bins=10, color='green', edgecolor='black', alpha=0.7, rwidth=0.78)
plt.xlabel('Petal length (cm)')
plt.ylabel('')
plt.title('Petal length (cm) of Iris flowers')
plt.savefig('Petal length_hist.png')
plt.show()

# Plotting the histogram of the sepal width.

sepal_w = df['sepal_width']
print(sepal_w)
print()

plt.hist(sepal_w, bins=10, color='magenta', edgecolor='black', alpha=0.7, rwidth=0.78)
plt.xlabel('Sepal width (cm)')
plt.ylabel('')
plt.title('Sepal width (cm) of Iris flowers')
plt.savefig('Sepal width_hist.png')
plt.show()

# Plotting the histogram of the sepal length. 

sepal_l = df['sepal_length']
print(sepal_l)
print()

plt.hist(sepal_l, bins=10, color='orange', edgecolor='black', alpha=0.7, rwidth=0.78)
plt.xlabel('Sepal length (cm)')
plt.ylabel('')
plt.title('Sepal length (cm) of Iris flowers')
plt.savefig('Sepal length_hist.png')
plt.show()

# Output a scatter plot of each pair of variables. 

# The first scatter plot is with the variables: petal length and petal width. 

# To start I'll get the data of the variables
species = df['species'].unique()
# unique() gets the unique elements of the array species, in this case the 3 types of Iris flowers.
petal_l = df['petal_length']
petal_w = df['petal_width']

# I'll asign diferent colors and shapes(using the format as markers) for the different species of Iris flowers, 
# to distinguish the differents between each others
colors = ['m', 'y', 'b']
markers = ['p', 's', 'D']

# I'm using the markers: 'p' as pentagon, 's' as square, , and 'D' as diamond shape.

# Create a scatter plot.
plt.figure(figsize=(10,7))
for i, species in enumerate(species):
    species = df[df['species'] == species]
    plt.scatter(species['petal_length'], species['petal_width'], color= colors[i], marker=markers[i], label=species, alpha=0.7)

# Axis labels.
plt.xlabel('Petal length (cm)', color='pink')
plt.ylabel('Petal width (cm)', color='pink')

# Title.
plt.title('Scatter plot of petal length and petal widht by species', color='purple')
plt.legend(df['species'].unique())

# X limits.
plt.xlim(0, 8)
# Y limits.
plt.ylim(0, 3)

plt.savefig('Scatter plot of petal length and petal width.png')
plt.show()

# The second scatter plot is with the variables: sepal length and sepal width. 

# To start I'll get the data of the variables that I'm using.
species = df['species'].unique()  
sepal_l = df['sepal_length']
sepal_w = df['sepal_width']

# I'll asign diferent colors and shapes(using thr formar as markers) for the different species of Iris flowers, 
# to distinguish the differents between each others
colors = ['m', 'y', 'b']
markers = ['v', 's', 'o']

# I'm using the markers: 'v' as triangle, 's' as square, and 'o' as a circle shape.

# Create a scatter plot.
plt.figure(figsize=(10,7))
for i, species in enumerate(species):
    species = df[df['species'] == species]
    plt.scatter(species['sepal_length'], species['sepal_width'], color= colors[i], marker=markers[i], label=species, alpha=0.7)

# Axis labels.
plt.xlabel('Sepal length (cm)', color='blue')
plt.ylabel('Sepal width (cm)', color='blue')

# Title.
plt.title('Scatter plot of sepal length and sepal width by species', color='green')
plt.legend(df['species'].unique())

# X limits.
plt.xlim(3, 9)
# Y limits.
plt.ylim(1, 5)

plt.savefig('Scatter plot of sepal length and sepal width.png')
plt.show()

# Create a bar chart to show all the variables of each specie.

species = ("Iris-setosa", "Iris-versicolor", "Iris-virginica")
variables = {
    'petal_width': (0.244, 1.326, 2.026),
    'petal_length': (1.464, 4.260, 5.552),
    'sepal_width': (3.418, 2.770, 2.974), 
    'sepal_length': (5.006, 5.936, 6.588)
}
# The label locations.
x = np.arange(len(species)) 
# The width of the bars 
width = 0.15  
multiplier = 0

# To add the different variables of the Iris flowers I created multiple subplots using plt.subplots

fig, ax = plt.subplots(layout='constrained') 

for attribute, measurement in variables.items():
    offset = width * multiplier
    rects = ax.bar(x + offset, measurement, width, label=attribute)
    ax.bar_label(rects, padding=3)
    multiplier += 1
    
# Add some text for labels, title and custom x-axis tick labels, etc.

ax.set_ylabel('Measures (cm)')
ax.set_title('Iris Data')
ax.set_xticks(x + width, species)
ax.legend(loc='upper left', ncols=2)
ax.set_ylim(0, 7)
plt.savefig('Bar chart Iris Data')
plt.show()


# Check the correlation between the variables

# I'll generate a correlation matrix with the numeric values to check which variables have the best correlation between them.
# First I'll remove the non-numeric variables, because the non-numeric vakues are not useful for this analysis. 
# Then I'll use the function corr()
df2 = df.drop('species', axis=1)

matrix = df2.corr()
print(matrix)

# Here is another way to get the correlation coefficient between  variables.
# I'm using corrcoef() to get the correlation coeficient betweent 2 variables.

petal_l = df['petal_length']
petal_w = df['petal_width']
sepal_l = df['sepal_length']
sepal_w = df['sepal_width']


corr = np.corrcoef(petal_l, petal_w)
print(corr)

corr1 = np.corrcoef(sepal_l, sepal_w)
print(corr1)

corr2 = np.corrcoef(sepal_l, petal_l)
print(corr2)

### End