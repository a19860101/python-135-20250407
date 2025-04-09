# 作業
# 盎司(oz)換算毫升(ml)
# 1盎司 =  29.573毫升

import math

oz = float(input('請輸入盎司(oz):'))

# ml = round(oz * 29.573,1)
ml = math.ceil(oz * 29.573)

print(oz,'盎司(oz)約等於',ml,'毫升(ml)')