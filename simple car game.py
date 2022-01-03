t = True
while t:
    something = input('> ')
    if something == 'help':
        print('''
start - to help the car
stop - to stop the car
quit = to exit''')
    elif something == 'start':
        print('car started')
    elif something == 'stop':
        print('car stopped')
    elif something == 'quit':
        break
    else:
        print('I dont understand that')