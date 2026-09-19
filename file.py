f = open("demo.txt" ,"a+")
# data=file.readline()
# print(data)
# print(type(data))
# file.close()

d=f.write("hello madam garu ")
print(f.read())
print(d)
f.close()

#with syntax
with open("demo.txt", "r") as f :
    data=f.read()
    print(data)


with open("demo.txt","w") as f:
    data=f.write("helloo world")
    print(data)

import os
os.remove("demo.txt")

#practice questions
#create practice.txt add the datta 
with open("practice.txt","r") as f:
   data=f.write("Hi everyone \n we are learning File I/O \n using Java \n I like programming in Java")
   print(data)

#replace occurences Java as python
with open("practice.txt","r") as f:
   data=f.read()
new_data=data.replace("Java","Python")
print(new_data)
with open("practice.txt","w") as f:
    f.write(new_data)

word="learning"
with open("practice.txt","r") as f:
    data=f.read()
    if(data.find(word)!=-1):
        print("found")
    else:
        print("Not found")


def check_forline():
    word="learning"
    data=True
    line_no=1
    with open("practice.txt","r") as f:
        while data :
            data=f.readline()
            if(word in data):
                print(line_no)
            line_no +=1
    return -1
print(check_forline())

#q
count=0
with open("practice.txt","r") as f:
    data=f.read()
    print(data)
    # n=""
    # for i in range(len(data)):
    #     if(data[i] == ","):
    #         print(int(n))
    #         n=""
    #     else:
    #         n+=data[i]
    num = data.split(",")
    for val in num:
        if(int(val)%2==0):
            count +=1
print(count)
