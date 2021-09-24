# problem IP address:

'''import re
ans=[]
IP_pattern = re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b',text)
with open('waste.txt','r') as f:
    for i in f.readlines():
        print(i)
        ans.append(IP_pattern.search(i))
print(ans)
'''

import sys, re

f = open('waste.txt','r')
text = f.read()
ips = [] 
regex = re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b',text)
if regex is not None:
    for match in regex:
        if match not in ips:
            ips.append(match)
            print(match)