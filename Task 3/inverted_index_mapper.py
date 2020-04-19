#!/usr/bin/env python

from sys import stdin
import os
import re
import string

text=""
for line in stdin:
        file_name = os.getenv('map_input_file')
	file_details=file_name.split("/")
	line = line.replace(","," ")
	line="".join(l for l in line if l not in string.punctuation)
	line = ' '.join(line.split())
	line=line.replace("\r","")
	line=line.replace("\n","")
	line=line.replace("\t","")
	line=line.strip()
        words = re.findall(r'\w+', line.strip())
        for word in words:
		print(word+" "+": 1"+" : "+file_details[-1])

