#!/usr/bin/env python3
import os 
import sys
import re
import array

seats = []
ids = []
max = 0

with open('tickets.txt') as f:
    for line in f:
        line = line.strip()
        if line:
            seats.append(line)
        
for seat in seats:
    row = seat[:7]
    col = seat[7:]
    first = 0
    last = 127
    i = 0
    while i < 6:
        diff = last - first
        diff = (diff + 1)/2
        if row[i] == 'F':
            last -= diff
        else:
            first += diff
        i += 1
    finalRow = first
    if row[6] == "B":
        finalRow = last
    first = 0
    last = 7
    i = 0
    while i < 2:
        diff = last - first
        diff = (diff + 1)/2
        if col[i] == 'L':
            last -= diff
            
        else:
            first += diff
        
        i += 1
    
    finalCol = first
    if col[2] == "R":
        finalCol = last
    id = (finalRow * 8) + finalCol
    ids.append(id)
    
    if id > max:
        max = id
    
print(f"{max} is the highest id")
ids  = sorted(ids)
i = 1
prev = ids[0]

while i < len(ids) - 2:
    cur = ids[i]
    if cur != prev + 1:
        if cur == prev +2:
            print(f"my seat is {prev+1}")
            break
    prev = cur
    i += 1