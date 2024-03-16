import balance
balance.remain('self')

def verify(self):
    usr=input('\nusername:')
    pss=input('\npassword:')
    while True:
        if usr==pss:
            print('login successful')
            break
        else:
            print('login failed')
            break