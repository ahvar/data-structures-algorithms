
"""
The Unicode character U+FEFF is the byte order mark, or BOM, and is used to tell the difference between big- and little-endian UTF-16 encoding.
If you decode the web page using the right codec, Python will remove it for you

#!python2
#coding: utf8
u = u'ABC'
e8 = u.encode('utf-8')        # encode without BOM
e8s = u.encode('utf-8-sig')   # encode with BOM
e16 = u.encode('utf-16')      # encode with BOM
e16le = u.encode('utf-16le')  # encode without BOM
e16be = u.encode('utf-16be')  # encode without BOM
print 'utf-8     %r' % e8
print 'utf-8-sig %r' % e8s
print 'utf-16    %r' % e16
print 'utf-16le  %r' % e16le
print 'utf-16be  %r' % e16be
print
print 'utf-8  w/ BOM decoded with utf-8     %r' % e8s.decode('utf-8')
print 'utf-8  w/ BOM decoded with utf-8-sig %r' % e8s.decode('utf-8-sig')
print 'utf-16 w/ BOM decoded with utf-16    %r' % e16.decode('utf-16')
print 'utf-16 w/ BOM decoded with utf-16le  %r' % e16.decode('utf-16le')
"""

from rich import print as rprint
import csv
import math

plusminus = u"\u00B1"
def clean_line(line):
    new_line = []
    for word in line:
        new_word = ""
        if "\xa0" in word:
            new_word = word.replace("\xa0","")
        elif "!!" in word:
            new_word = word.replace("!!","_")
        elif plusminus in word:
            new_word = word.replace(plusminus,"")
        elif "%" in word:
            new_word = float(word.strip("%"))
        elif word.replace(",","").isdigit():
            new_word = int(word.replace(",",""))
        else:
            new_word = word
        new_line.append(new_word)
    return new_line
    #new_line = [word.replace("\xa0","") if "\xa0" in word else word for word in line]

us_age_sex = []
with open("/Users/arthurvargas/dev/pyreview/data/ACSST1Y2023.S0101-2025-01-06T173644.csv", newline='', encoding='utf-8-sig') as file_in:
    reader = csv.reader(file_in)
    for line in reader:
        line = clean_line(line)
        us_age_sex.append(line)

rprint(us_age_sex)

