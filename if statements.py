# an if statement is a statement that does something if certain conditions are meet
# such as

x = 10
if x == 10:
    print(10)

# the process is simple, if x is equal to 10, then the 10 will be printed
# otherwise nothing will be printed

# else statements are used for when the conditions are not met for example:
jacks_age = 9
if jacks_age == 10:
    print('jack is  10')
else:
    print('jack is not 10')

# elif statements is a compact version of else: if:. just to make code neater u know.
# here is an example of else if and elif:
bob_age = 10
if bob_age == 10:
    print('bob is 10')
else:
    if bob_age == 9:
        print('bob is 9')

anna_age = 11
if anna_age == 12:
    print('anna is 12')
elif anna_age == 11:
    print('anna is 11')

# is is also important to properly indent the code.
# anything that is indented after a : will be dependent on the statement.
# anything that is not indented after a : will run regardless of the above statement

# example:
mark_age = 14
if mark_age == 15:
    print('mark is 15')
print("hehe I print regardless of mark's ")

# notice that the 2nd print statement is not indented. this means that
# it is not part of the if statement and will run regardless of it

# random fun program with if statements:

# if its hot:
    # print('its a hot day)
    # print('drink plenty of water)
# elif its cold:
    # print('its a cold day)
    # print('wear warm clothes')
# else:
    # print('its a lovely day)

x = input('is it hot or cold? ')
weather = x.lower()
# this asks the user to enter hot or cold and then converts the response to lowercase
# and then assigns the response to the variable weather.
if weather == 'hot':
    print('''
''')
elif:
    weather

