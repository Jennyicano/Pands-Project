# Analysis of the Iris Data Set. 
# Author Jennifer Ibanez Cano

import os
import numpy as np
import csv

# Load the data from txt to csv

with open('iris.data.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[4]} species, {row[0]} sepal_length, {row[1]} sepal_width, {row[2]} petal_length, {row[3]} petal_width')
            line_count += 1
    print(f'Processed {line_count} lines.')
    