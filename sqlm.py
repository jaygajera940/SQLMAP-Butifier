#!/bin/env python3

import json

dic = {}
filepath = "output/file.txt"
with open(filepath,'r') as fp:
    a = fp.read().split("---")
a = "".join(a[1])
a=a.replace('\n',"")
s = a.split(":")
for i in range(0,len(s)-1,2):
    dic[s[i]] = s[i+1]

print(dic)
with open("output.json",'w') as fp:
      json.dump(dic,fp)
