#!/usr/bin/env python3
import os 
import sys
import array

trees = []
with open('map.txt') as f:
    for line in f:
        line = line.strip()
        if line:
            strLine = str(line)
            trees.append(strLine)

slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
width = len(trees[0]) - 1
rows = len(trees) - 1 
print(f"I have {rows} and a width of {width}")

total = 1
for x, y in slopes:
    row = 0
    col = 0
    count = 0
    while row <= rows:
        char = trees[row][col]    
        if char == '#':
            count += 1
        row += y
        col += x
        if col > width:
            col = col - width - 1
    total = total * count

print(f"I found {total} trees")