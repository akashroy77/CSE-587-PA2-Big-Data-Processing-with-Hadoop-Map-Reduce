#!usr/bin/env python3
import sys

output={}
words=[]
for input in sys.stdin:
	input=input.strip()
	words=input.split(' ')
	for i in words:
		if(i is not "1"):
			if(i in output):
				output[i]+=1
			else:
				output[i]=1
	sorted_dict=sorted(output.items(),key=lambda x:x[1],reverse=True)
	for k in range(2):
		print(sorted_dict[k][0])
	

