def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)
show(6)

def fact(n):
    if (n==0 or n== 1):
        return 1
    return fact(n-1)*n
print("fact:",fact(5))

# sum of n number
def cal_sum(n):
    if(n==0):
        return 0
    return cal_sum(n-1) + n
su=cal_sum(7)
print(su)

#print all elememts in a list
#hint:use list and index parameters
def l(list,index=0):
    if (index == len(list)):
        return
    print(list[index])
    l(list,index+1)
fruits = ['mango','banana','pragne','green']
l(fruits)
   
    