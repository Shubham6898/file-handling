'''import re

#q1: program to extract IP address from file
with open("ip.txt","r") as file:
    for line in file:
        print(re.findall("[0-9.]+",line))


#q2: program to check if the string starts with particular substring using regex
string="our friends are happy"
list1=re.findall("\Amy friends",string)
#print(list1)
if len(list1)<1:
    print("The string does not start with the required substring(regex)")
else:
    print("it starts")


#q3: program to remove duplicate words in a sentence
a=re.findall("[A-Za-z0-9]+","Happy Birthday Happy 92 for you")
a1=""
for item in a:
    if item not in a1:
        a1=a1+" "+item
print(a1[1:])

#q4: for parsing and processing url

print(re.findall("([a-zA-Z]+)://", "https://github.com/SimranWadhwa/TrainingPython-FIL/tree/main/python"))
#print(re.findall("[a-zA-Z]+://", "https://github.com/SimranWadhwa/TrainingPython-FIL/tree/main/python"))
print(re.findall("://([a-zA-Z0-9/_.-]+)", "https://github.com/Simran_Wadhwa/TrainingPython-FIL/tree/main/python"))

print(re.findall("([a-zA-Z]+)://([a-zA-Z0-9_/.-]+)", "https://github.com/SimranWadhwa/TrainingPython-FIL/tree/main/python"))
print(re.findall("/([a-zA-Z0-9_.-]+)", "https://github.com/Simran_Wadhwa/TrainingPython-FIL/tree/main/python"))

'''

import numpy as np
a=np.array([[1,2,3],[4,5,6]])
b=np.array([[4,5,6],[1,2,3]])
sum_array=a+b
print("SUM-Array:\n",sum_array)
div_array=a/b
print("Div_array\n",div_array)
mul_array=a*b
print("MUl_array\n",mul_array)
sub_array=a-b
print("SUB_arr:\n",sub_array)
mod_arr=a%b
print('Mod_arr:\n',mod_arr)
print('Min element of a:\n',a.min())
# mean:
print("Mean of array a:\n",a.mean())
