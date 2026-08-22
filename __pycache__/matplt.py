# import matplotlib.pyplot as plt
# x=[1,2,3,4,5]
# y=[10,20,30,40,50]
# plt.plot(x,y)
# plt.show()

# import matplotlib.pyplot as plt
# city=['America',"china","India"]
# population =[200,300,600]
# plt.bar(city,population)
# plt.show()

import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[1,4,1,4,1]
line=[10,20,30,40]
plt.scatter(x,y , marker = "*")
plt.scatter(x,line,marker = ">")
plt.title("Line Graph")
plt.ylabel('Y-axis')
plt.xlabel("X-axis")
plt.show()
