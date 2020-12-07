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
    valid = 0
    for key in sorted(passport):
        value = passport[key].strip()
        if key == 'byr':
            i = int(value)
            if i >= 1920 and i <= 2002:
                valid +=1
        elif key == 'iyr':
            i = int(value)
            if i >= 2010 and i <= 2020:
                valid +=1
        elif key == 'eyr':
            i = int(value)
            if i >= 2020 and i <= 2030:
                valid +=1
        elif key == 'hgt':
            match = re.match(r"(\d+)(in|cm)", value)
            if match:
                num = int(match.group(1))
                unit = match.group(2)
                if unit == 'cm':
                    if num >= 150 and num <= 193:
                        valid += 1                        
                else:
                    if num >= 59 and num <= 76:
                        valid += 1                        
        elif key == 'hcl':
            match = re.match(r"#[a-f0-9]{6}", value)
            if match:            
                valid += 1            
        elif key == 'ecl':
            match = re.match(r"(amb|blu|brn|gry|grn|hzl|oth)", value)
            if match:
                valid += 1                
        elif key == 'pid':
            match = re.match(r"[0-9]{9}$", value)
            if match:
                valid += 1                
        else:
            if key != 'cid':
                print("INVALID KEY!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                valid = 0
                break

    if valid == 7:
        total += 1
    #else:
        #print(f"INVALID PASSPORT {valid}")
    
    

print(f"I found {total} valid passports")