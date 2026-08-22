# user = input("Enter your name :")

# # print("Length of the user : ",len(user))
# str= "Hi , $hello $iam my name is $anuhsk $1876283"
# print("Occurence of $ is :",str.count("$"))
#conditional statements
age =int(input("Enter your age :"))
if age >=18 :
    print("Eligible for vote")
elif age == 17 :
    print("Wait for one year")
else :
    print("Not eliggible")        

light = input("Enter a color:")
if (light == "red"):
    print("Stop")
elif (light == " orange"):
    print("Get ready")
elif (light == "green") :
    print("GO")        
print("End of code")  
  
marks = int(input("Enter total marks:"))
if (marks >=90):
     grade = "A"
elif (marks >=80):
   grade = "B"
elif (marks >= 70) :
    grade = "C"
elif ( marks >=60):
    grade = "D"
else :
    grade = "Fail"   
print("Grade of a student : ",grade) 
 
age = 89
if (age >=18):
    if (age>=80 ):
        print("Cannot drive")
    else :
        print("Can drive")
else :
    print("Cannot drive")
   
n = int(input("Enter a number :"))
if(n%2==0):
    print("even")   
elif (n%2 !=0) :
    print("odd")   
else :
    print("none7") 
 
a = int(input("Enter a :"))
b = int(input("Enter b :"))
c = int(input("Enter c :"))
if (a>b and a>c):
    print("First is greater",a)
elif (b>=c) :
    print("second is greater",b)
else :
    print("third greater ",c)  
     
num = int(input("Enter a number :"))
if(num%7==0):
    print("it is a multiple of 7")
else :
    print("not a multiple of 7")    