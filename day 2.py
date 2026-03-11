# mylist = ["Aditi","Janhavi","Kohana","Kanak",77,"Anusha",60.52,"Zara",]
# print(mylist)
# print(type(mylist))
# print(mylist[0])
# print(mylist[1])
# print(mylist[2])
# print(mylist[-1])
# print(mylist[2:5])
# print(mylist[:5])
# print(mylist[1:])
# print(mylist[1:8:2])
# print(mylist[:])
# print(mylist[::-1])

# mylist.append('yash')
# mylist.append('Shrushti')
# print(mylist)

# mylist.insert(1,'Mariyam')
# print(mylist)

# mylist.remove(60.52)
# print(mylist)

# newlist = mylist.copy()
# print(newlist)
# print(newlist)

# mylist = [['Aditi','Mishra'],[85.56],[440022,"yyy"]]
# print("example of multidimensional list:")
# print(mylist)
# print(mylist[0][0])
# print(mylist[0][1])
# print(mylist[1][0])
# print(mylist[2][0])
# print(mylist[2][1])

# list1=["Aditi","Mishra"]
# print(list1*2)

# list2=[50,25.50]
# print(list1+list2)

# list2=[50,25.5,'Aditi']
# del list2[2]
# print(list2)
# list2.clear()
# print(list2)

# name="Aditi"
# print(name)
# myname=list(name)  #typecasting
# print(myname)

#sorting in ascending order
# mylist=[44,22,77,8,9,88]
# mylist.sort()
# print(mylist)

#sorting in descending order
# mylist=[44,22,77,8,9,88]
# mylist.sort(reverse= True)
# print(mylist)

# math = 10
# phy = 50
# eng = 40
# print(id(math))  
# print(id(phy))  # id function is used to return the address of variable 
# print(id(eng))

#aliasing
# mylist=[44,22,77,0,9,88]
# newlist = mylist
# print(id(mylist))
# print(id(newlist))

# membership operator 1) in  2) not in
# name = "Aditi"
# print('Z ' in name)
# print('Z'not in name)

#looping
# for i in range(1,10,2):
#     print(i)

# for i in range(5,0,-1):
#     print(i)

# for i in range(1,11):
#     print(i*2)

#Multiplication Table(2-20)
# for i in range(1,11):
#     for j in range(2,11):
#         print(i * j,end="\t")
#     print()
# print("-----------------------------------------------------------------")   
# for i in range(1,11):
#     for j in range(12,21):
#         print(i * j,end="\t")
#     print()

#simple if loop
#WAP TO ACCEPT ANY DIGIT AND CHECK THAT POS, NEG,ZERO
# no=int(input("enter any digit:"))
# if no>0:
#     print('posotive')
# if no<0:
#     print('negetive')
# if no==0:
#     print('zero')

# working non working day
# day = input("Enter the day: ")
# if day.lower() == "saturday" or day.lower() == "sunday":
#     print("Weekend")
# else:
#     print("Working Day"

# #WAP to accept three paper marks and calculate total,percentage and if percentage is greater then equal to 60 then he/she is eligible for placement
# m1 = int(input("Enter marks of Paper 1: "))
# m2 = int(input("Enter marks of Paper 2: "))
# m3 = int(input("Enter marks of Paper 3: "))

# total = m1 + m2 + m3
# percentage = total / 3

# print("Total Marks =", total)
# print("Percentage =", percentage)

# if percentage >= 60:
#     print("Eligible for Placement")
# else:
#     print("Not Eligible for Placement")

# WAP TO ACCEPT 5 DIFFERNT VALUE IN 5 DIFFERENT VAR AND CHECK MAX VALUE AND PRINT BY USING SIMPLE IF STATEMENT
# a = int(input("Enter first value: "))
# b = int(input("Enter second value: "))
# c = int(input("Enter third value: "))
# d = int(input("Enter fourth value: "))
# e = int(input("Enter fifth value: "))
# max = a
# if b > max:
#     max = b
# if c > max:
#     max = c
# if d > max:
#     max = d
# if e > max:
#     max = e
# print("Maximum value is:", max)    