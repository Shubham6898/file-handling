# problem IP address:

import re
with open("waste.txt","r") as file:
    for line in file:
        print(re.findall("[0-9.]+",line))