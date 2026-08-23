def sum(a,b):
    s = a+b
    print("Sum :",a,"+",b,"=",s)
    return s
sum(7,8)
sum(74,6)
sum(634,79)

def calc(a,b,c):
    sum=a+b+c
    avg = sum / 3
    print(avg)
    return avg
calc(7,8,9)

#WAF to print the length of a  list
city = ["delhi","mumbai","kolkata","chennai","bangalore"]
name = ["ram","shyam","mohan","sita","gita"]
def p_len(list):
    print(len(list))
p_len(city)
p_len(name)

#WAF to print the elements of a list in a single line
city = ["delhi","mumbai","kolkata","chennai","bangalore"]
def print_list(list):
    for item in list:
        print(item,end=" ")
print_list(city)        


# factoial
def cal(n):
    fact=1
    for i in range(1,n+1):
        fact*= i
    print(fact)
cal(5)

#WAF to convert USD to INR
def conv(usd_val):
    inr_val=usd_val * 83
    print(usd_val,"USD =",inr_val,"INR ")
conv(56)

# Homework problem
Number = int(input("Enter a number :"))
def odd_even(Number):
    if Number%2 == 0:
        print("EVEN")
    else:
        print("ODD")
odd_even(Number)

