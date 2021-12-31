# good source: https://www.w3schools.com/python/python_operators.asp
# do print() to see the results
# basic arithmetic operations:
10 + 10
10 - 10
10 * 10
10 / 10

# python arithmetic operators:
# % aka modulus returns the remainder of a division. the answer is 1:
modulus = 7 % 3
# ** aka exponentiation is the same as raising power to something like 5^5 or 1^1 ect
exponentiation = 5**5
# // aka floor division returns only the largest possible number of a division
floor = 10 // 7

# python Assignment operators:
# += assigns and then adds something onto a variable.
# -= does the same thing but subtracts
# *= same thing but multiples
# /= same thing but divides
# %= same thing but modulus
# //= same thing but floor division
# theres more that I will add later. you can find it on the website I linked at the top

# example:
x = 5
x += 7
# this returns 12

# python comparison operators:
# the == operator compares the value of 2 object
# example of how its used:
x = 5
if x == 10:
    print('this wont print because x does not equal 10')

# != is not equal to
5 != 10

# > is greater than and < is less than. basic stuff.
# >= is greater than or equal to
# <= is less than or equal to

5 >= 5
6 > 5

# operator precedence (basic math stuff):
x = (10 + 3) * 2 ** 2
# 1. parenthesis
# 2. exponentiation
# 3. multiplication or division
# 4. addition or subtraction

# this part is
# round() returns said number to the nearest 10th
x = 2.9
Round = round(x)

# abs() returns the absolute value of a number
a = -2.9
absolute = abs(a)

# import math allows for advanced math functions to be used
# such as acos() and asin()
import math
print(math.ceil(2.9))





