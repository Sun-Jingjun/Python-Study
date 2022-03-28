# 遍历元组
tup = (1, 2, 3, 4)
print('tuple')
for t in tup:
    print(t)

# 遍历列表
list = [1, 2, 3, 4, '4', '3', '2', '1']
print('list')
for l in list:
    print(l)

# 遍历集合
set = {2, 4, 5, 6, 6}
print('set')
for s in set:
    print(s)

# 遍历map
dict = {'a': 1, 'b': 2, 'c': 3}
print('dict-v')
# 遍历v
for v in dict.values():
    print(v)
print('dict-k,v')
# 遍历k,v
for k, v in dict.items():
    print('{}:{}'.format(k, v))

# 索引遍历 1，2，3...
l = [1, 2, 3, 4, 5, 6]
print('index')
for i in range(0, len(l)):
    print(l[i])

# 索引和value
print('index,value')
for index, val in enumerate(l):
    print('{}:{}'.format(index, val))

# while循环
i = 1
while i < 5:
    i += 1

# 条件与循环的嵌套使用 y= |x| + 1
y = [x + 1 if x > 0 else -x + 1 for x in range(0, 10)]
print(y)
