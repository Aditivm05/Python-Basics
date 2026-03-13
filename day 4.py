#PRINT NUMBERS FROM 1 TO 5 AND BREAK THE LOOP WHEN NUMBER 3 IS ENCOUNTERED
# for i in range(1,5):
#    if i == 3:
#        break
#    print(i)

# PRINT NUMBERS FROM 1 TO 5 EXCEPT 3
# for i in range(1,5):
#     if i == 3:
#         continue
#     print(i)

# WAP to pint the sequence from (1,2,4,5,)$(5,4,2,1)
# for x, y in zip(range(1,6),range(5,0,-1)):
#        if x == 3 and y ==3:
#               continue
#        print(x, "",y)

# print numbers from 1 to 5 uisng while loop
# i=1
# while i<=5:
#     print(i)
#     i+=1

# WAP to print the UESERNAME AND PASSWORD
# username = ""
# password = ""
# while username != "admin" and password != "hello":
#      username = input("enter username:")
#      password = input("enter password:")
# print("welcome to the system")

#WAP to print the sum of first n natural numbers
# n=int(input("enter a number: "))
# sum=0
# i=1
# while i<=n:
#     sum=sum+i
#     i+=1
# print("sum of first",n,"numbers is",sum)

# WAP TO REMOVE DUPLICATE CHARACTERS IN A STRING
# name = "ZARA"
# result = ""
# for ch in name:
#     if ch not in result:
#         result = result + ch
# print(result)
 
# REVERSE THE STRING
# name = "ADITI"
# result = ""
# for ch in name:
#      result = ch + result
# print(result)

# 
# mycart=[10,20,200,300,800,60,700]
# for i in mycart:
#     if i>400:
#         print("This is is my purchased cart item")
#         continue
#     print(i)

# WAP to check wheather the given string is palindrome or not
# name = input("enter a string: ")
# if name == name[::-1]:
#     print("This is a palindrome string")
# else:
#      print("This is not a palindrome string")

# WAP TO CHECK IF TWO STRINGS ARE ANAGRAM OF EACH OTHER OR NOT
# str1 = input("enter first string: ")
# str2 = input("enter second string: ")
# if sorted(str1) == sorted(str2):
#    print("The strings are anagrams")
# else:
#      print("The strings are not anagrams")

#WAP A FUNCTION TO ADD KEY VALUE PAIRS TO A DICTIONARY
# my_dict = {}
# n = int(input("How many key-value pairs do you want to add? "))
# for i in range(n):
#     key = input(f"Enter key {i+1}: ")
#     value = input(f"Enter value for '{key}': ")
#     my_dict[key] = value
# print("Dictionary:", my_dict)   
# 
# Remove key value pair from a dictionary
# my_dict = {'name': 'Aditi', 'age': 25, 'city': 'Delhi'}
# key_to_remove = input("Enter the key you want to remove: ")
# if key_to_remove in my_dict:
#    del my_dict[key_to_remove]
# print("Updated Dictionary:", my_dict)

# WAP if a given key is present in a dictionary or not
# my_dict = {'name': 'Aditi', 'age': 25, 'city': 'Nagpur'}
# key_to_check = input("Enter the key you want to check: ")
# if key_to_check in my_dict:
#     print(f"The key '{key_to_check}' is present in the dictionary.")
# else:
#     print(f"The key '{key_to_check}' is not present in the dictionary.")

# nested for loop 
# for i in range(1,4):
#     for j in range(1,4):
#         print("i",end="")
#     print()

# WAP to print the following pattern
# n= int(input("Enter the number of rows:"))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(chr(64+j),end="")
#     print()

# WAP to print the following pattern
# n= int(input("Enter the number of rows:"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(n+1-i,end="")
#     print()

n= int(input("Enter the number of rows:"))
for i in range(1,n+1):
    for j in range(1,n+2-i):
        print("*",end="")
    print()    
