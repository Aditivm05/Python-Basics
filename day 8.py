# # WAP TO PERFORM ARITHEMATIC OPERATION USING FUNCTIONAL PROGRAMMING APPROACH 
# import sys

# def Addition(val1, val2):    
#     print("Addition:", val1 + val2)

# def Subtraction(val1, val2):
#     print("Subtraction:", val1 - val2)

# def Multiplication(val1, val2):
#     print("Multiplication:", val1 * val2)

# def Division(val1, val2):
#     if val2 == 0:
#         print("Cannot divide by zero!")
#     else:
#         print("Division:", val1 / val2)

# while True:
#     print("\n1. Addition")
#     print("2. Subtraction")
#     print("3. Multiplication")
#     print("4. Division")
#     print("5. Exit")
    
#     choice = int(input("Enter your choice: "))

#     if choice == 5:
#         print("Exiting the program.")
#         sys.exit()

#     val1 = int(input("Enter first number: "))
#     val2 = int(input("Enter second number: "))
    
#     if choice == 1:
#         Addition(val1, val2)

#     elif choice == 2:
#         Subtraction(val1, val2)

#     elif choice == 3:
#         Multiplication(val1, val2)

#     elif choice == 4:
#         Division(val1, val2)

#     else:
#         print("Invalid choice. Please try again.")

# # nested function 
# def outerfunction():
#     print("This is the outer function.")

#     def innerfunction():
#         print("This is the inner function.")

#     innerfunction()
# outerfunction() # first we call the outer function which will print the message and then call the inner function to print its message.

# wap to count the word
# name = "Aditi is good programmer"
# count = 1
# for i in name:
#     if i == " ":
#         count += 1
#     else:
#         continue
# print("The number of words in the string is:", count)   
# 
# # what is the output of the following code
# init_tuple=()
# print(init_tuple.__len__())

# init_tuple_a ='a','b'
# init_tuple_b =('a','b')
# print(init_tuple_a == init_tuple_b) # True because both tuples have the same elements in the same order.

# init_tuple_a ='1','2'
# init_tuple_b =('3','4') 
# print(init_tuple_a + init_tuple_b)

# l =[1,2,3]
# init_tuple = ('python',)*(l.__len__()-l[::-1][0])
# print(init_tuple)

# INIT_TUPLE =('PYTHON')*3
# print(type(INIT_TUPLE))

# init_tuple =(1,)*3
# init_tuple[0]=2
# print(init_tuple)

# init_tuple =((1,2),)*7
# print(len(init_tuple[3:8]))

# # program to replace a string with another string
# s="" 
# s1=s.replace("difficult","easy")
# print(s1)
# #all occurance will be replaced
# s="ababababababab"
# s1=s.replace("a","b")
# print(s1)

#Removing space from the string
# city = input("Enter the name of the city: ")
# scity=city.strip()
# if scity=='Hyderabad':
#     print("Hello Hyderabad...Adab!")
# elif scity=='Chennai':
#     print("Hello  Chennai...Vanakkam!")
# elif scity=='Bangalore':
#     print("Hello Bangalore...shubhodaya!")
# else:
#     print("Your entered city is invalid!")    

# list comprehension
# s=[i*i for i in range(1,11)]
# print(s)

# val =[2**i for i in range (1,6)]
# print(val)

# s =[i*i for i in range(1,11)]
# print(s)

# val2=[i for i in s if i%2==0] 
# print(val2)

# dict comprehension
squares={x: x*x for x in range(1,16)}
print(squares)

doubles={x:2*x for x in range(1,6)}
print(doubles)