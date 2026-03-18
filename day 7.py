# import re
# var ='gasgg54@#vscsd!s*'
# count = 0
# for i in var:
#     z = re.findall('[a-z,0-9]',i)
#     z = ord(i)
#     print (z)
#     if z:
#          if z>=97 and z<= 122:
#           continue
#     elif z>=48 and z <= 57:
#           continue
#     else:
#         count+=1
# print(count)

# find the intersesection of three arrays
# a = [1,2,3]
# b = [2,3,4]
# c = [3,4,5]
# result = []
# for i in a:
#     if i in b and i in c:
#         result.append(i)
# print(result)

# # move zeros to the end of the array
a = [0,1,0,3,12]
# for i in a:
#     if i == 0:
#         a.remove(i)
#         a.append(i)
# print(a)

## find second largest number in the array
# a = [9,2,7,4,5]
# a.sort()
# print(a)
# print(a[-2])

#finding the total distance between ajecent items of list of 5 numbers
a = [10,11,7,12,14]
total_distance = 0
for i in range(len(a) - 1):
    total_distance += abs(a[i+1] - a[i])
print(total_distance)