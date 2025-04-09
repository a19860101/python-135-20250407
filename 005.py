# list 列表

data = [123, 2.3,'hello',True, 'apple', 'banana']

# print(data)
# print(data[0])
# print(data[1])
# print(data[2])
# print(data[3])

# for
# for item in data:
    # print(item)

# for i in range(1,11):
    # print(i,end=' ')

# while
# break 中斷 continue 繼續
a = 1
# while a < 10:
#     if a == 5:
#         a += 1
#         continue
#     print(a, end=' ')
#     a += 1


# 巢狀迴圈
# for x in ['x','y','z']:
#     for y in [1,2,3]:
#         if y == 3:
#             continue
#         print(x,y)

# 99乘法表
for i in range(1,10):
    for j in range(1,10):
        if i == 1:
            continue
        # print(i,'x',j,'=',i*j)
        print(f'{i}x{j}={i * j}')


for i in range(6):
    print('-'* (6-i))