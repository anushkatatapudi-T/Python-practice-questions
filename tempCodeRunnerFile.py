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