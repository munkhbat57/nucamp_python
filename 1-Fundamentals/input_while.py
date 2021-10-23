while True:
    print('1')
    print('2')
    print('3')
    option = input('pick ')
    print(type(option))
    if option == '1':
        print('p 1')
    elif option == '2':
        print('p 2')
    elif option == 3:
        print('p 3')
        break
    else:
        print('invalid')
