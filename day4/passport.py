#!/usr/bin/env python3
import os 
import sys
import re
import array

passports = []
total = 0
fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
passportStr = ''
with open('passports.txt') as f:
    passport = {}
    for line in f:
        line = line.strip()
        if line:
            passportStr = passportStr + line + ' '
        else:
            splitString = passportStr.split()
            for split in splitString:
                key, val = ''.join(split).split(":")
                passport[key] = val
                
            passportStr = ''
            passports.append(passport)
            passport = {}

for passport in passports:
    print(f"passport: {passport}")
    matchAll = True
    for field in fields:
        if field not in passport.keys():
            matchAll = False
    if matchAll:
        total += 1
    

print(f"I found {total} valid passports")