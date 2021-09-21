#problem 1 : word
with open("/Users/apple/Desktop/Shubham/waste.txt",'r') as f:
    for i in f :
        for word in i.split():
            print(word)


# problem 2: counting

with open("/Users/apple/Desktop/Shubham/waste.txt",'r') as f:
    count=0
    for i in f :
        count=+1
print(count)

# problem 3: merge

data = data2 = ""
  

with open('/Users/apple/Desktop/Shubham/waste.txt','r') as f1:
    data_1 = f1.read()

with open('/Users/apple/Desktop/Shubham/abc.py','r') as f2:
    data_2 = f2.read()
  

final_data=data_1+data_2
  
with open('/Users/apple/Desktop/Shubham/merged.txt','w') as f3:
    f3.write(final_data)

# problem 4 : reverse using stack
import queue
q=queue.LifoQueue()
lq=queue.LifoQueue()
with open("/Users/apple/Desktop/Shubham/waste.txt",'r') as f:
    for i in f:
        lq.put(i)
while lq.empty() !=True:
    print(lq.get())
#print(lq.empty())