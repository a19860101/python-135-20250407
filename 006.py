# 作業
# 盎司(oz)換算毫升(ml)
# 1盎司 =  29.573毫升

n = input('請輸入要換算的數字:')
s = input('單位是oz還是ml?(o/m):')

if s == 'o':
    result = float(n) * 29.573
    result = round(result,2)
    print(f'換算結果:{n}oz約{result}ml')
else:
    result = float(n) / 29.573
    result = round(result, 2)
    print(f'換算結果:{n} ml約{result} oz')