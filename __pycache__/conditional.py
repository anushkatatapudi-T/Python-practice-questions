# fizzBuzz (the classic): print 1 to 30, but multiples of 3 → "Fizz", multiples of 5 →
# "Buzz", multiples of both → "FizzBuzz"
# n = int(input("enter 1-30 number:"))
# for i in n range(1,31):
#    if (n%3 ==0):
#        if ( n%3 ==0 and  n%5==0):
#            print("FizzBuzz")
#         else :
#            print("Fizz")
#    elif ( n%5==0):
#        print("Buzz")

# Grade classifier: convert a numeric score to a letter grade (A/B/C/D/F) using as few
# comparisons as possible (think about the order of your conditions carefully).
# marks = int(input("enter your marks :"))
# if (marks >=90):
#      grade = "A"
# elif (marks >80):
#    grade = "B"
# elif (marks > 70) :
#     grade = "C"
# elif ( marks >=60):
#     grade = "D"
# else :
#     grade = "Fail"   
# print("Grade of a student : ",grade) 

# Leap year checker — the actual rule is trickier than "divisible by 4": divisible by 4,
# *except* century years, *unless* divisible by 400. (2000 is a leap year, 1900 is not.)
# year = int(input("Enter year: "))

# if year % 400 == 0:
#     print(year, "is a leap year")
# elif year % 100 == 0:
#     print(year, "is not a leap year")
# elif year % 4 == 0:
#     print(year, "is a leap year")
# else:
#     print(year, "is not a leap year")   

# Tricky — chained comparisons: predict, then explain: (1<2<3) and 3>2<5
# Python chains comparisons in a way most languages don't — figure out what's
# actually happening.
# a = int(input("Enter a number :"))
# if (1<2<3):
#     print("true")
# elif(3>2<5):
#     print("false") 
#     ython supports chained comparisons.
# 1 < 2 < 3 is equivalent to (1 < 2) and (2 < 3).
# 3 > 2 < 5 is equivalent to (3 > 2) and (2 < 5).
# Since both comparisons in each expression are True, the final result is True for both.   
x = int(input("Enter a number:"))
sign = "poss" if x>0 else "non-pos"
print(sign)