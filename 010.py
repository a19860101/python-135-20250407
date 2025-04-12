def foo():
    x = 10
    y = 2
    # print(x * y)
    return x * y


result = foo()

def area(w,h):
    return w * h

# print(area(12,24))

def jp_to_tw(dollar,rate=0.22):
    return dollar * rate

print(jp_to_tw(rate=0.225,dollar=10000))

import time
def timer( end,start=0):
    for x in range(end, start, -1):
        print(x)
        time.sleep(1)
    print('完成')

# timer(10)

# for i in range(5,0,-1):
#     print(i)

def fullname(first, last):
    print(f'{first} {last}')

fullname('Mary','Chan')
fullname(last='Lee', first='Max')
