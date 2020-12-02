#!/usr/bin/env python3
import os 
import sys
import array
import re

test = re.compile(r"(\d+)-(\d+) ([a-z]): (.*)")
count = 0
with open('passwords.txt') as f:
    for line in f:
        line = line.strip()
        match = test.match(line)
        if match:
            i = int(match.group(1))
            j = int(match.group(2))
            letter = match.group(3)
            password = match.group(4)
            #print(f"checking {line}, {letter}, {i}, {j}, {password}, {len(password)}")
            first = password[i-1]
            second = password[j-1]
            if first == letter or second == letter:
                if first != second:
                    count = count+1
print(f"Total Count: {count}")