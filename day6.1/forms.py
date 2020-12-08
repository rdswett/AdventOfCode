#!/usr/bin/env python3
import os 
import sys
import re
import array

formSet = set()
group = []
total = 0
with open('forms.txt') as f:
    for line in f:
        line = line.strip()
        if line:
            for c in line:
                formSet.add(c)
            group.append(formSet)
            formSet = set()
        else:
            total += len(set.intersection(*group))
            group = []
            formSet = set()
    
print(f"Total: {total}")
    
