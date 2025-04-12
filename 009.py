# s = 'hello world!!'

# 子字串
# print(s[0])
# print(s[12])
# print(s[0:8])
# print(s[6:])
# print(s[:5])
# print(s[-1])
# print(s[-7])
# print(s[-4:-2])
# print(s[::2])

# 字串方法
s = 'hello world apple banana'
# len() 字串長度
# print(len(s))

# count() 計算文字數量
# print(s.count('o'))

# index() 取得文字索引值 若找不到該字會報錯
# print(s.index('l'))
# print(s.index('q'))

# find() 取得文字索引值 若找不到該字會回傳-1
# print(s.find('q'))
# print(s.find('l'))

# isalpha()
# 判斷字串是否為全英文
# print(s.isalpha())

n = '123.3'
# isdigit()
#判斷字串是否為數字
# print(n.isdigit())

# startswith()
# 判斷字串第一個字母是否為指定文字
# print(s.startswith('h'))
# endswith()
# 判斷字串最後一個字母是否為指定文字
# print(s.endswith('d'))

# upper() 字串轉大寫
# print(s.upper())

# lower() 字串轉小寫
# print(s.lower())

# capitalize() 首字大寫
# print(s.capitalize())

# title() 每個單字的首字大寫
# print(s.title())

# replace() 取代文字
# print(s)
# print(s.replace('apple','orange'))


# split() 分裂 文字轉串列(list)
print(s)
q = s.split()
# q = s.split('o')
# print(type(q))

# strip()
msg = '    hello    '
print(msg.strip())
print(msg.lstrip())
print(msg.rstrip())