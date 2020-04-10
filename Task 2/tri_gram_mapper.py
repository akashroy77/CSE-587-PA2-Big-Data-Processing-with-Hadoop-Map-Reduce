#!/usr/bin/env python3

import sys
import string
text=""
input_string=[]
output=[]
count=2
for line in sys.stdin:
	line = line.replace(","," ")
	line="".join(l for l in line if l not in string.punctuation)
	line = ' '.join(line.split())
	line=line.replace("\r","")
	line=line.replace("\n","")
	line=line.replace("\t","")
	line=line.strip()
	text+=line
input_string=text.split(' ')
l=len(input_string)
while(count< l+2):
	if(count==l):
		output.append([input_string[count-2],input_string[count-1]," "])
	elif(count==l+1):
		output.append([input_string[count-2]," "," "])
	else:
		output.append([input_string[count-2],input_string[count-1],input_string[count]])
	count+=1
map_list=[]
for i in range(len(output)):
	wordset=output[i]
	output_string=" "
	for i in range(len(wordset)):
		if("science" in wordset[i] or "Science" in wordset[i] or "SCIENCE" in wordset[i] or "fire" in wordset[i] or "Fire" in wordset[i] or "FIRE" in wordset[i] or "sea" in wordset[i] or "Sea" in wordset[i] or "SEA" in wordset[i]):
			wordset[i]="$"

		if(i is not 2):
			output_string+=wordset[i]+"_"
		else:
			output_string+=wordset[i]
	map_list.append(output_string)
for i in range(len(map_list)):
	print(map_list[i]," ","1","\n")

		
