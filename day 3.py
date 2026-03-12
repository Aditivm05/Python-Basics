# wap to accept three marks and check maximum marks using nested if else 
# n1 = int(input("Enter the value of n1: "))
# n2 = int(input("Enter the value of n2: "))
# n3 = int(input("Enter the value of n3: "))
# if n1>n2:
#     if  n1>n3:
#         print("n1 is greater");
#     else:
#      print("n3 is greater");
# else:     
#     if n2>n3:
#         print("n2 is greater");
#     else:
#         print("n3 is greater");

# else if ladder

# wap to aaccpt percentage and if per > 90 ==> grade A and if per > 80 ==> grade B and if per > 70 ==> grade C and if per > 60 ==> grade D and if per > 50 ==> grade E and if per < 50 ==> grade F

# p = float(input("Enter percentage: "))
# if p > 90:
#     print("Grade A")
# elif p >= 80:
#     print("Grade B")
# elif p >= 70:
#     print("Grade C")
# elif p >= 60:
#     print("Grade D")
# elif p >= 50:
#     print("Grade E")
# else:
#     print("Grade F")

# mydict + {
#     "name ": "Aditi"
#     "professionaL": "Data Scientist"


# MYDICT ={
#     101:"Janhavi",
#     102:"Kanak",
#     "103":"Kohana",
#     "104":"Aditi",
#     105:"Mariyam",
#     106:"Shrushti",
#     }
# print(MYDICT)

# with the help of key printy values 
# a =MYDICT[102]
# print(a)

# update the value of the key 
# MYDICT[106]="Riddhi"
# print(MYDICT)
 
# for x in MYDICT:
#     print(x)

# MYDICT.pop(101)
# print(MYDICT)

# slicing
# name = "Aditi Mishra"
# print(name[0])
# print(name[1])
# print(name[-1])
# print(name[0:5])
# print(name[1:])
# print(name[:5])
# print(name[:])
# print(name[1:8:2])
# print(name[::-1])

# s = "help4code is best platform for practicing programming"
# print(s.find("help4code"))
# print(s.find("python"))
# print(s.find("programming"))

# s = "Aditi","janhavi","kanak"
# m = '|'.join(s)
# print(m)
 
# s = "Pytnon is a high level programming language"
# print(s.lower())
# print(s.upper())
# print(s.swapcase())
# print(s.title())
# print(s.capitalize())

# print("subject marks :")
# phy = 50
# chem = 60
# maths =70
# print("phyics ={} chemistry{} maths = {}".format(phy,chem,maths))
# print("phyics ={0} chemistry ={1} maths ={2}".format(phy,chem,maths))
# print("phyics ={x} chemistry ={y} maths ={z}".format(x=phy, y=chem, z=maths))

# total = phy + chem + maths
# print("total marks = {}",f"(total)")
# print("Roll no=","47".zfill(4))

# print ('Aditi05'.isalpha())   #True
# print ('Aditi'.isalpha())  
# print ('05'.isdigit())  
# print ('sdsdsds'.islower())  
# print (''.islower())  
# print ('Aditi05'.isupper())  
# print ('My name is Aditi'.istitle())  
# print (''.istitle())  
# print (''.isspace())  
# print ("Hello".startswith("He")) 
# print ("Hello".endswith("lo")) 
 
 #bodmas
# a = 50 
# b = 30
# c = 20
# d = 10
# print((a+b)*c/d)
# print((a-b)*c/d)
# print(a+(b*c)/d)

# x =['A','B','C'] 
# y =['A','B','C'] 
# z=[1,2,3,4]
# print(x==y)
# print(x==z)
# print(x!=z)

name = "Aditi"
# for i in name:
#     print(i)
data = ['a','e','i','o','u']  
vowels = 0 
con = 0
for i in name:
    if i in data:
        vowels += 1
    else:
        con += 1 

print("vowels =",vowels)
print("consonants =",con)
