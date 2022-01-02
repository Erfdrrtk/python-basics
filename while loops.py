# while loops are used to repeat a block of code an number of times until a condition is met
# example:
print('''
--- 1st Example ---''')
j = 0
while j != 7:
    print('*' * j)
    j = j + 1
# the program repeats print('*' * j) until j != 7 is not true
# remember that in python the index starts at 0

# guessing game:
print('''
--- 2nd Number ---''')
secret_number = 9
limit = 3
tries = 0
guess = int(input('guess: '))
while guess != secret_number:
    if tries == limit:
        print('out of tries')
        break
    tries = tries + 1
    guess = int(input('try again: '))










