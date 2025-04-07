x = 10
y = 6

# pow() 次方
print(pow(x,3))
print(pow(4,10))

# round() 四捨五入
print(round(2.3))
print(round(2.6))

# abs() 絕對值
print(abs(-23))

# max() 取最大值
print(max(x,y))

# min() 取最小值
print(min(x,y))

import math
# math.floor() 無條件捨去
print(math.floor(3.5))

# math.ceil() 無條件進位
print(math.ceil(3.6))

print(math.pi)

# 求圓周長 2*pi*r

# t = input('請輸入文字')
# print(t)


r = float(input('請輸入半徑:'))
result = 2 * math.pi * r
result = round(result,2)
print(result)

# 作業
# 盎司(oz)換算毫升(ml)
# 1盎司 =  29.573毫升
