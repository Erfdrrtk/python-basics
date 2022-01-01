print('''
if you enter your weight in lb, then the program will convert it to kg
and vice versa''')
# multiply number_convert with weight to get lb. divide number_convert with weight to get kg
number_convert = 2.205
weight = int(input('enter your weight (just the number): '))
kg_or_lb = input('is that in kg or lb? ')

if kg_or_lb == 'lb':
    weight = weight / number_convert
elif kg_or_lb == 'kg':
    weight = weight * number_convert
print(int(weight))


