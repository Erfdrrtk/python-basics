# or is used to return true if one of the statements is true

print('''
--- 1st Example ---''')

x = 'dog'
y = 'cat'

if x == 'dog' or y == 'tail':
    print('1 or more statements are true')

# and returns true if both statements are ture

print('''
--- 2nd Example ---''')
a = 'sleep'
s = 'eat'
if s and a == 'cat':
    print('both equal cat')
else:
    print('they both dont equal cat')

# not reverses the result, returns False if the result is true.
# I think it only works with boolean values
# a way to think of not is that not is the same as false
# so the phrase: not cat is the same at false cat
print('''
--- 3rd Example ---''')
likes_cats = True
t = 'fun'
if t and not likes_cats:
    print('this person doesnt like cats')

# example program:
print('''
--- 4th Example --- ''')
good_credit = True
high_income = True
criminal_record = False

if good_credit or high_income:
    print('the applicant is eligible for loan')
if good_credit and not criminal_record:
    print('the applicant if eligible for load')
