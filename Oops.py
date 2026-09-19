# class Car:
#     college_name="ST.peters college"
#     def __init__(self, name, marks):
#         self.name= name
#         self.marks= marks
#         print("Adding new name.....")
    
# car1=Car("Anushka",56)
# print(car1.name,car1.marks)
# car2=Car("PRIYA",98)
# print(car2.name,car2.marks) 
# print(car1.college_name)

# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
# #     def welcome(self):
# #         print('welcome raaa',self.name)
# #     def getmarks(self):
# #         return self.marks
# # name=Student("Anushka",98)
# # name.welcome()
# # print("Yours marks are:",name.getmarks())

# #Practice question
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#     @staticmethod
#     def hello():
#         print("hello")
#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print("Hi", self.name, "Your avg marks are", sum/3)

   
# s1=Student("Anushka",[98,97,99])
# s1.get_avg()
# s1.hello()
# s1.name = "Ironman"
# s1.get_avg()
# class Car:
#     def __init__(self):#constructor
#         self.acc = False
#         self.brk=False
#         self.clutch=False
#     def start(self): #method
#         self.clutch=True
#         self.acc=True
#         print("Car started.....")

# car1=Car()
# car1.start()

#Question
class Account:
    def __init__(self,bal,acc):
        self.balance=bal
        self.account_no=acc

    def debit(self,amount):
        self.balance -= amount
        print("Rs.",amount,"Was debited from your account")
        print("Total balance : ",self.balance)

    def credit(self,amount):
        self.balance += amount
        print("Rs.",amount,"Was credited to your account")
        print("Total balance : ",self.balance)

    def Get_total(self):
        return self.balance
acc1=Account(9800,2654258155)
print("Total balance :" ,acc1.balance)
print("Account number :",acc1.account_no)
acc1.debit(1000)
acc1.credit(900)
print("TOTAL BALANCE IS :",acc1.Get_total())