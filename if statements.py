# an if statement is a statement that does something if certain conditions are meet
# such as

print("--- First Example ---")
x = 10
if x == 10:
    print(10)

# the process is simple, if x is equal to 10, then the 10 will be printed
# otherwise nothing will be printed

# else statements are used for when the conditions are not met for example:
print('''
--- 2nd Example ---''')
jacks_age = 9
if jacks_age == 10:
    print('jack is  10')
else:
    print('jack is not 10')

# elif statements is a compact version of else: if:. just to make code neater u know.
# here is an example of else if and elif:
print('''
--- 3rd Example ---''')
bob_age = 10
if bob_age == 10:
    print('bob is 10')
else:
    if bob_age == 9:
        print('bob is 9')

print('''
--- 4th Example ---''')

anna_age = 11
if anna_age == 12:
    print('anna is 12')
elif anna_age == 11:
    print('anna is 11')

# is is also important to properly indent the code.
# anything that is indented after a : will be dependent on the statement.
# anything that is not indented after a : will run regardless of the above statement
print('''
--- 5th Example ---''')
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

# the else statements might be hard for some so i'll explain.
# if is_hot and is_cold are false, then the else statement will be invoked
# the else statement doesnt belong to the else statement because the elif statement
# is a combination of if and else not just if.
print('''
--- 6th Example ---''')
is_hot = True
is_cold = False

if is_hot:
    print("it's a hot day")
    print("drink plenty of water")
elif is_cold:
    print("it's a cold day")
    print("wear warm clothes")
else:
    print("it's a lovely day")
print('have a good day')

# another program example:
# price of house is 1M

print('''
--- 7th Example ---
--- last example ---''')

price = 1000000
good_credit = True
bad_credit = False
percentage_for_good_credit = 0.1
percentage_for_bad_credit = 0.2
down_payment = ()

if good_credit:
    down_payment = price * percentage_for_good_credit
    print(f'down payment is {down_payment} because you have good credit :)')
elif bad_credit:
    down_payment = price * percentage_for_bad_credit
    print(f'down payment is {down_payment} because you have bad credit :(')





