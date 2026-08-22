#print numbers from 1 - 100
# a = range(100,0,-1)
# for i in a :
#     print(i)
# #print numbers from 100 - 1
# a = range(1,101)
# for i in a :
#     print(i)   
# #print multiplictaion table of any number
# n = int(input("Enter a number:"))
# for i in range(1,11):
#     print(n,"*",i,"=",n*i)  
for i in range(5):
    pass
print("hello")

#find sum of first n natural numbers
#using for loop
n = 6
sum = 0
for i in range (1,n+1)  :
    sum += i
print("total:",sum)    
#using while loop
n = 5
sum=0
i = 1
while i <=n:
    sum += i
    i +=1
  
print("total:",sum)    

#find the factorial of first n number 
#using for loop
n = 5
fact = 1
for i in range(1,n+1):
    fact *= i
print("fact :",fact)   
#using while loop 
n = 5
fact = 1
i=1
while i<=n:
    fact *=i
    i+=1
print("fact :",fact)    
#question ?
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
for num in range(1, 5):
    if is_prime(num):
        print(num)

#question ?
for i in range(1,4):
    for j in range(i):
        print("*",end="")    
    print() 
print()
print("*")    

#question ?
for n in range(1,30):
    r = "Fizz" *(n%3==0) + "Buzz" *(n%5==0) 
    print(r or n)

for i in range (5):
    pass #used to do nothing,it just doesn't perform any operation inside a loop
print(i)    