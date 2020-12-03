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

row = 0
col = 0
count = 0
width = len(trees[0]) - 1
rows = len(trees) - 1 

while row <= rows:
    char = trees[row][col]    
    if char == '#':
        count += 1
    row += 1
    col += 3
    if col > width:
        col = col - width - 1    

print(f"I found {count} trees")