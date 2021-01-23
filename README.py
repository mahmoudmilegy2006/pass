import os
def func():
    name = input('Enter your name : ')
    what = input(r'are you new {1} or old {0} :')
    if what == '1' :
        passwordn = input('Enter your pasword : ')
        ope2 = open('passwords.txt','r').read()
        if name != '' and passwordn != '' :
            if passwordn in ope2 :
                print(f'Welcome {name} you have acount and your password is {passwordn}')
            else:
                al = passwordn+'_'+name
                print(f'Welcome {name} your password is {passwordn}')
                ope = open('passwords.txt','a')
                ope.write(f'{al}\n')
                print('acound added')
        else :
            print('error !!')
    elif what == '0' :
        ope2 = open('passwords.txt','r').read()
        passwordo = input('Enter your old password : ')
        if passwordo+'_'+name in ope2 :
            print(f'welcome {name} your password is {passwordo}')
        else:
            print('your have a wrong password , make new')
            func()
func()
