#!/usr/bin/env python3
import os 
import sys
import re
import array

formSet = set()
total = 0
with open('forms_short.txt') as f:
    for line in f:
        line = line.strip()
        if line:
            for c in line:
                formSet.add(c)
        else:
            total += len(formSet)
            formSet = set()
    total += len(formSet)

    
print(f"Total: {total}")
    
