# don't mix floats and decimals

from decimal import Decimal

deci_num = Decimal('0.1')
float_num = 0.1

# adding a decimal and a float this will raise a TypeError
# result = deci_num + float_num
# print(result)

# mixing decimals and intergers is legal
result = deci_num + 100
print(result)
