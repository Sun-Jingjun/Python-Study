# 初始化创建map
# 索引访问map，map中如果有元素不存在，会直接报错
map = {1: 2, 2: 3}
print(map[2])

map2 = dict([(1, 2), (3, 4)])
print(map2[1])

map3 = dict({1: 2, 3: 4})
print(map3[3])

# todo 这种方式为什么不能使用数字作为key，有待研究
map4 = dict(a=2, b=4)
d4 = dict(name='jason', age=20, gender='male')
print(map4['a'])
print(map4.get('c'))

# map可以存放不同类型的元素
map0 = {1: 2, '3': 3}
print(map0)

# map中增加元素
map5 = {1: 11, 2: 22}
map5[3] = 33
print(map5[3])

# 修改元素
map5[3] = 333
print(map5[3])

# 删除元素
# map5.pop(3)
# print(map5[3])

# 根据k，v排序
map6 = {'b': 3, 'a': 4, 'b': 1, 'h': 2}
sort_k_map6 = sorted(map6.items(), key=lambda x: x[0])
sort_v_map6 = sorted(map6.items(), key=lambda x: x[1])
print(sort_k_map6)
print(sort_v_map6)
