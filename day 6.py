# what will be the output of the following code snippet?

# fruit_list1 = ['apple', 'Berry', 'Cherry', 'papaya']
# fruit_list2 = fruit_list1
# fruit_list3 = fruit_list1[:]
# fruit_list2[0] = 'Guava'
# fruit_list3[1] = 'Kiwi'

# sum = 0
# for ls in (fruit_list1, fruit_list2, fruit_list3):
#     print(ls)
#     if ls[0]=='Guava':
#         sum += 1
#     if ls[1]=='Kiwi':
#         sum += 20
# print(sum)        


# def f (i,value = []):
#     value.append(i)
#     print(value)
# f(1)
# f(2)
# f(3)


# def func(value,values):
#     var = 1
#     values[0] = 44   
# t=3
# v=[1,2,3]
# func(t,v)
# print(t,v[0])

# dict = {'c':97, 'a':96, 'b':98}
# for _ in sorted(dict):
#     print(dict[_])

# fruit = {}
# def addone(index):
#     if index in fruit:
#         fruit[index] += 1
#     else:
#         fruit[index] =1
# addone('Apple')
# addone('Banana')
# addone('apple')
# print(len(fruit))
# 
# Product of an ]array except self (sample input: [1,2,3,4] output: [24,12,8,6])
def productExceptSelf(nums):
    n = len(nums)
    output = [1] * n
# Left product
    for i in range(1, n):
        output[i] = output[i - 1] * nums[i - 1]
# Right product
    right_product = 1
    for i in range(n - 2, -1, -1):
        right_product *= nums[i + 1]
        output[i] *= right_product
    return output
# Call function
nums = [1, 2, 3, 4]
print(productExceptSelf(nums))