#Function

# def msg():
#     print("Hello World")
# msg()

# def add():
#     n1 = int(input("Enter the vale of n1:"))
#     n2 = int(input("Enter the vale of n2:"))
#     print("Add=",n1+n2)
# add()    

# how to writtem multiple value
# def add():
#     n1 = int(input("Enter the vale of n1:"))
#     n2 = int(input("Enter the vale of n2:"))
#     sum = n1+n2
#     mul = n1*n2
#     sub = n1-n2
#     div = n1/n2
#     return sum,sub,mul,div

# result = add()
# print(result)

# types of arrgument
#1.positional argument(position will be fixed)
# 2. keyword argument
# 3 default argument
# 4. variable argument

# #positional argument
# def personalInfo(fname,lname):
#     print("First name=",fname)
#     print("Last name:",lname)
# fname="Adit"
# lname="Mishra"    
# personalInfo(fname,lname)    

#default argument
# def cityName(city):
#     print(city)
# cityName("Nagpur")
# cityName("Mumbai") 
# cityName("Bilaspur")   

#variable name 
# def studentNames(*name):
#     print(name)
# studentNames("Aditi","Janhavi","Kanak","Kohana","Yash")

# mylist =[5,2,9,7,5,6]
# def searchElement(target):
#     for i in range(len(mylist)):
#         if mylist[i] == target:
#             print(mylist[i])
# searchElement(7)        
# 

mylist =[5,2,9,7,5,6]
def searchElement(target):
    for i in range(len(mylist)):
        if mylist[i] == target:
            print("Element found at index:",i)
searchElement(7)        

