def main():
    bank()

def bank():
    print('TO LOGIN:1\nTO SING UP:2')
    user = input('choice\n: ')
    if user == '1':
        login()
    elif user == '2':
        sing_up()

def sing_up():
    print('PROVIDE NAME')
    name = input('name\n: ')
    while True:
        print('PROVIDE AGE')
        age = int(input('age\n: '))
        if age <18:
            print('too young')
        elif age >=18:
            print(f'welcome,{name}')
            break
    print('PROVIDE EMAIL')
    email = input('email\n: ')
    with open('project18bankemail.txt','w') as file:
        file.write(f'{email}')
    while True:
        print('CREATE NEW PASSWORD')
        pas = input('password\n: ')
        print('PROVIDE CREATED PASSWORD')
        confirm = input('password\n: ')
        if confirm != pas:
            print('passwords do not match\n: ')
        elif confirm == pas:
            print('password created succesfully')
            break
    with open('project18bankpassword.txt','w') as fille:
        fille.write(f'{confirm}')
    money_bank()

def login():
    while True:
        with open('project18bankemail.txt') as file:
            lines = file.readlines()
            for line in lines:
                print('PROVIDE EMAIL')
                user = input('email\n: ')
                if user != line.rstrip():
                    print('email d oes not exist')
                elif user == line.rstrip():
                    print('welcome')
        break
    while True:
        with open('project18bankpassword.txt') as filee:
            trees = filee.readlines()
            for tree in trees:
                print('PROVIDE PASSWORD')
                inp = input('password\n: ')
                if inp!=tree.rstrip():
                    print('invalid password')
                elif inp==tree.rstrip():
                    print('loged in seccesfully')
        break
    money_bank()


def money_bank():
    with open('project18bank.txt') as fille:
        lines = fille.readlines()
        for line in lines:
            print(f'BALANCE\n: {line.rstrip()}')
    while True:
        setting = input('FOR SETTINGS:input setting\n: ')
        if setting == 'setting':
            access_setting()
        break

def access_setting():
    print('TO REFIL MONEY:deposit\nTO CHECK BALANCE:portfolio\nTO CHANGE PASSWORD:password')
    choice = input('choice\n: ')
    if choice == 'deposit':
        refil_money()
    elif choice == 'portfolio':
        wallet()
    elif choice == 'password':
        new_pas()

def refil_money():
    old_pas()
    print('INPUT AMOUNT TO REFIL')
    amount = int(input('amount\n: '))
    with open('project18bank.txt') as file:
        lines = file.readlines()
        for line in lines:
            balance = int(line.rstrip())
            deposit = amount + balance
            with open('project18bank.txt','w') as fille:
                fille.write(f'{deposit}')
            print('NEW BALANCE')
            print('please wait................................')
            print('...................................')
            print(f'BALANCE: {deposit}')
    with open('project18bank.txt','w') as fil:
        fil.write(f'{deposit}')
    
def wallet():
    with open('project18bank.txt') as file:
        lines = file.readlines()
        for line in lines:
            print(f'portfolio:{line.rstrip()}')

def password():
    old_pas()
    new_pas()

def old_pas():
    while True:
        with open('project18bankpassword.txt') as file:
            lines = file.readlines()
            for line in lines:
                print('PROVIDE PASSWORD')
                user = input('password\n: ')
                if user != line.rstrip():
                    print('invalid pas')
                elif user == line.rstrip():
                    print('welcome')
        break

def new_pas():
    while True:
        print('CREATE NEW PASSWORD')
        pas = input('password\n: ')
        print('CONFIRM CREATED PASSWORD')
        confirm = input('password\n: ')
        print('CONFIRM CURRENT PASSWORD')
        old_pas()
        if confirm != pas:
            print('passwords do not match')
        elif confirm  == pas:
            print('password changed successfully')
        break
    with open('project18bankpassword.txt','w') as file:
        file.write(f'{confirm}')

if __name__=='__main__':
    main()