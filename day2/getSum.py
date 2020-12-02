#!/usr/bin/env python3
import os 
import sys
import array

inputs = []
with open('input.txt') as f:
    for line in f:
        line = line.split()
        if line:
            inputs.append(int(''.join(line)))

print(f"Total Entries: {len(inputs)}")

for i in inputs:
    #print(f"{i}")
    for j in inputs:
        #if inputs.index(i) is inputs.index(j):
            #continue
        for k in inputs:
            total = i+j+k
            #print(f"{i} + {j} = {total}")
            if total == 2020:
                sum = i*j*k
                print(f"{sum}")
                sys.exit()
