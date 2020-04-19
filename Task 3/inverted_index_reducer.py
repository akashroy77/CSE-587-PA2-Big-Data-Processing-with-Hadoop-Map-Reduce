#! /usr/bin/python

from sys import stdin
import re
import collections

occurrence= {}
map_list=[]
for line in stdin:
	line=line.strip();
        details=line.split(":")
	word=details[0].lower()
	occurrence.setdefault(word,{});
	file_name=details[-1]
	if file_name in occurrence[word]:
		occurrence[word][file_name]+=1
	else:
		occurrence[word][file_name]=1
for word in occurrence:
        file_inverted = ["%s:%d" % (doc_id, occurrence[word][doc_id])
                         for doc_id in occurrence[word]]

        word_list = ','.join(file_inverted)
        print(word+"  "+word_list)
	
        
