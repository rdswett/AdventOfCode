#!/usr/bin/env python3
import os 
import sys
import array
import re

test = re.compile(r"(\d+)-(\d+) ([a-z]): (.*)")
count = 0
with open('passwords.txt') as f:
    for line in f:
        match = test.match(line)
        if match:
            min = int(match.group(1))
            max = int(match.group(2))
            letter = match.group(3)
            password = match.group(4)
            i = password.count(letter)
            if i >= min and i <= max:
                count = count+1
print(f"Total Count: {count}")