score = 90

# if
if score >= 60:
    print('恭喜及格')

# if...else
if score >= 60:
    print('恭喜及格')
else:
    print('不及格 請加油')

# if...elif...else
if score >= 80:
    print('優秀')
elif score >= 60:
    print('及格')
else:
    print('不及格 請加油')

x = 10

if x > 0:
    print('正')
elif x < 0:
    print('負')

# day = 8
# if day == 0:
#     print('星期日')
# elif day == 1:
#     print('星期一')
# elif day == 2:
#     print('星期二')
# elif day == 3:
#     print('星期三')
# elif day == 4:
#     print('星期四')
# elif day == 5:
#     print('星期五')
# elif day == 6:
#     print('星期六')
# else:
#     print('請設定正確的日子')

day = int(input('請輸入0-6:'))

match day:
    case 0:
        print('星期日')
    case 1:
        print('星期一')
    case 2:
        print('星期二')
    case 3:
        print('星期三')
    case 4:
        print('星期四')
    case 5:
        print('星期五')
    case 6:
        print('星期六')
    case _:
        print('請設定正確的日子')