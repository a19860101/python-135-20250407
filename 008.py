# 跳脫字元
# s = 'hello \'John\''
# s = "hello \"john\""
# s = 'C:\\Users\\zac\\Documents\\python-135-20250407\\'
# s = r'C:\Users\zac\Documents\python-135-20250407'
# s = 'hello\njohn'
# s = 'hello\tjohn\t!\t!\t!'
# s = '1.\tjohn\n2.\tmarry\n10.\tmax'

# print(s)

# 格式化字串 %

# s = 'hello %-10s'
# s2 = '今天氣溫是%10d度'
# s3 = '今天氣溫是%3.1f度'
# s4 = 'Hello %s 你好 今天氣溫為 %3.1f'
# name = 'Mary'
#
# print(s % name)
# print(s % 'John')
# print(s3 % 20.5)
# print(s4 % ('Andy', 30))

# 格式化字串 format

# s = 'hello {}'
# print(s.format('john'))
# s = 'hello {} 今天氣溫為{}'
# s = 'hello {1} 今天氣溫為{0}'
# s = 'hello {name} 今天氣溫為{deg:3.2f}'
# print(s.format(name='john',deg=31))

# s = 'hello {:-^10s}'
# print(s.format('john'))

# s = '今天是{:_^20d}度'
# s = '今天是{0:_^20d}度'
# print(s.format(20))

# s = '今天是{deg:_^20d}度'
# print(s.format(deg=20))

# f字串
name = 'JOhn'
deg = 33
s = f'hello {name:~^10s} 今天是{deg:3.2f}'

print(s)
