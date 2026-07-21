#variables , numbers ,strings
#  # qno.6
sentence = "I like apple"
char = len(sentence)
num = len(sentence.split())
print("Total Character :",char)
print("Number of words :",num)
u =sentence.upper()
l = sentence.lower()
print("Uppercase:",u)
print("Lowercase:",l)
print(sentence.replace('apple','banana'))
# # qno 7
str = "banana"
print(str.count("a"))
# qno8 
num = input("Enter a string:")
rev = num[-1::-1]
if num == rev :
    print("palindrome")
else :
    print("not palindrom")    
# # qno 9
var = [12,4,6,7,5]
sum = sum(var)
avg = sum/len(var)
lar = max(var)
small = min(var)
print("Largest",lar)
print("Smallest:",small)
print("Sum :",sum)
print("Average:",avg)
# # qno10
n = [1,2,2,3,4,4,5]
print(set(n))
# qno 11
n = [1,4,5,7,89,2]
print(n[-1::-1])
# qno 12
n = [2,4,6,8,9,7]
a = sorted(n)
print(a[-2])
#qno 13
num = input("Enter a string:")
print(len(num)>=8 )
print(any(ch.isdigit() for ch in num))
print(any(ch.isupper()for ch in num))
#qno 14
c = int(input("enter number:"))
f = c*9/5 + 32
a = round(f,1)
if a.is_integer() :
    print(int(a))
else:
    print(a)    
#qno 15
# method -1
n = input("Enter:")
reverse = (n[::-1])
print("Reversed string is :", reverse)
if n == reverse :
    print("Palindrome")
else :
    print("not a palindrome")    
# #method 2
n = input("enter:")
reverse = ""
for i in range(len(n)-1,-1,-1):
    reverse = reverse + n[i]
print("Reversed string is :", reverse)
if n == reverse :
    print("Palindrome")
else :
    print("not a palindrome")     
#qno 16
# method 1
num = input("Enter a charcters:")
a = int(num[0:1])
b=int(num[1:2])
c=int(num[2:3])
d=int(num[3:4])
e=int(num[4:5])
total = a+b+c+d+e
print(total)
# method 2
num = input("Enter a charcters:")
a = int(num[0])
b=int(num[1])
c=int(num[2])
d=int(num[3])
e=int(num[4])
total = a+b+c+d+e
print(total)
# qno 17
a = int(input("enter a number:"))
b=int(input("enter a number:"))
a,b=b,a 
print("a:",a , "b:",b)