
# 创建并初始化set
s1 = {1,3,4,6,9,-1}
s2 = set({1,2,3,4})
s3 = set((1,2,34,5))


# set不能使用索引访问，底层使用了hash
# 判断元素是否在集合set中
if 1 in s1:
    print('1 in s1')
else:
    print('1 not in s1')


if 2 in s1:
    print('1 in s1')
else:
    print('2 not in s1')

# 增加元素,增加重复元素不报错，set保持唯一
s1.add(2)
print(s1)

s1.add(1)
print(s1)

s1.add('3')
print(s1)

# 删除元素
s1.remove(1)
print(s1)

# 排序
sort_set = sorted(s1)
print(sort_set)
