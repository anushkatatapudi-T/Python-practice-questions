# question no.1
name =input("Enter you name:")
age = int(input("Enter you age:"))
college =input("Enter you college name:")
information=f'My name is {name}\nI am {age} years old\nI study at {college}\n'
print(information)
print(name)
print(age)
print(college)
# qno.2
first=int(input("enter a value:"))
second=int(input("enter b value:"))
add = first+second
product = first * second
division = first/second
difference = first - second
print("Addition:",add)
print("Product:",product)
print("Division:",division)
print("Difference:", difference)
# qno.3
string = input("Enter a string:")
print(string[3:8])
print(string[0:1])
print(string[-1:])
print(string[-1::-1])
# qno.4
num = int(input("enter a number:"))
if num > 0 :
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")        
# qno.5
num = int(input("enter a number:"))
if num%2 == 0:
    print("Even number")
else :
    print("Odd number")

#day-1 (variables,print,input,commments)
print("5"+"5") #"inside this is a character not a number "
print(5+5) # it is not inside a string and it is a number(integer)
#because it allows the string to join together
x=5 
y=x
x=10
print(x,y) #y will be 5 because it x changes y doesnt change it will remain the same value
#No , variable cannot start with a number becuase it some rules if we start with a number ex:12nms it cannot understand whetherr it is reading a vairable or a number ,Yes! it can start with a underscore(_)
#underscore(_) means it is perfect valid varible or  used for special meaning
#input() it usually gives str value because we think that if we type 10 it is a number but python will store it as a character 
#no matter what user types are because str means text adn number means it is use to perform a specific task 
# we can convert it by using the datatype (int,float)
#if we dont convert ex:if we take input as 10 20 and used to do mathematical operation it cannot do 