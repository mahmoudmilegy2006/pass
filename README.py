def func():

    name = input('Enter your name : ')
    what = input(r'are you new {1} or old {0} :')

    passwords = []

    if what == '1' :
        passwordn = input('Enter your pasword : ')
        passwords.append(passwordn)
        print(passwords)
        print('Welcome')
        what2 = input('do you want to sign again [1=true],[0=false] : ')
        if what2 == '1' :
            func()
        elif what2 == '0':
            print('godbay')

    elif what == '0' :
        passwordo = input('Enter your old password : ')
        print(passwords)
        if passwordo in passwords :
            print(f'wlcome {name}')
        else:
            print('your have a wrong password , make new')
            func()

func()


