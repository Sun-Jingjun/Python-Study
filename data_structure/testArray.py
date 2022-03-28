# coding:utf-8

# 初始化元组和数组
arr1 = (1, 2, '3', '4')
arr2 = [1, 2, '3', '4']


arr2.reverse()
arr1 = list(reversed(arr1))



print(arr1, arr2)


tup = (1, 2, 3, 4)
new_tup = tup + (5, ) # 创建新的元组 new_tup，并依次填充原元组的值
print(new_tup)
