print("{:10}".format(1234))      # '      1234'
print("{:7}".format(123))       # '    123'
print("{:<10}".format(1234))     # '1234      '
print("{:^10}".format(1234))     # '   1234   '

print("{:12}".format("hello"))   # 'hello       '
print("{:>12}".format("hello"))  # '       hello'
print("{:^12}".format("hello"))  # '   hello    '

x = 1234567.89012345
print(x)                         # 1234567.89012345

print("{:20}".format(x))         # '    1234567.89012345'
print("{:20,}".format(x))        # '  1,234,567.89012345'
print("{:20,.3}".format(x))      # '            1.23e+06'
print("{:20,.3f}".format(x))     # '       1,234,567.890'
print("{:,.4f}".format(x))       # '1,234,567.8901'
print("{:,.4e}".format(x))       # '1.2346e+06'

p = 0.3
print("{:.2%}".format(p))        # '30.00%'
