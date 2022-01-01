# < is less than
# > is greater than
# >= is equal or greater than
# <= is equal or less than
# != is not equal to

print('''
--- first Example ---''')

temperature = 35
if temperature != 30:
    print('the temperature is not 30')
else:
    print('the temperature is 30')

print('''
--- 2nd example ---''')

name = 'alex honnold'
if len(name) < 3:
    print('name must be at least 3 characters')
elif len(name) > 50:
    print('name must be less than 50 or 50 ')
else:
    print('name is good')
