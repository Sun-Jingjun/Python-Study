# 字符串可以使用单引号，双引号，三引号
str0 = "I'm a student"
print(str0)

str2 = ''' ok !!! '''
print(str2)

# 字符串是字符数组，可以直接通过索引访问单个字符，完成切片等操作
c = str0[1]
c2 = str0[1:]
print(c)
print(c2)

# replace替换字符,字符串
print(str2.replace('!', '?'))
print(str2.replace('ok', 'hello'))

# 字符串拼接,在py2.5后进行了优化，可以放心使用。也可以使用join将列表中的每个字符串全部拼接起来
nums = ''
for n in range(0, 10):
    nums += str(n)
print(nums)

nums2 = []
for n in range(0, 10):
    nums = nums2.append(str(n))
l = ''.join(nums2)
print(l)

# split 与其他语言的使用没有区别，返回一个分割后的数组
def query_data(namespace, table):
    """
    given namespace and table, query database to get corresponding
    data
    """

path = 'hive://ads/training_table'
namespace = path.split('//')[1].split('/')[0]  # 返回'ads'
table = path.split('//')[1].split('/')[1]  # 返回 'training_table'
data = query_data(namespace, table)


# 格式化format ，也可以使用%的这种类型，不过官方最新推荐的方式为format
id = 3
name = 'sun'

print('userid = {},username = {}'.format(id,name))
