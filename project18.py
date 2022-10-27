import random

def main():
    create_cassino_account()
    cassino_games()

def create_cassino_account():
    print('TO LOGIN INPUT 2 : TO REGISTER INPUT 1')
    user = int(input('provide choice\n: '))
    print('')
    if user == 1:
        sign_up()
    elif user == 2:
        login()
        print('')

def sign_up():
    print('PROVIDE NAME')
    name = input('name\n: ')
    print(f'welcome,{name}')
    print("PROVIDE AGE")
    while True:
        age = int(input('age\n: '))
        if age <18:
            print('UNDERAGE NOT ALLOWED')
        else:
            print(f'welcome,{name}')
            break
    print('')
    print('PROVIDE A VALID EMAIL ADDRESS')
    while True:
        email = input('provide email\n: ')
        if email == '':
            print('invalid email')
        else :
            break
    print('')
    with open('project18email.txt','w') as file:
        file.write(f'{email}')
    while True:
        print('CREATE NEW PAS')
        createpas = input('pas\n: ')
        print('confirm pas created')
        confirmpas = input('pas\n: ')
        if confirmpas != createpas:
            print('passwords do not match')
        elif  confirmpas == createpas:
            print('passwords set succesfully')
            break
    print('')
    with open('project18pas.txt','w') as fille:
        fille.write(f'{confirmpas}')

    x1 = random.randint(0,9)
    x2 = random.randint(0,9)
    x3 = random.randint(0,9)
    x4 = random.randint(0,9)
    x5 = random.randint(0,9)
    x6 = random.randint(0,9)
    x7 = random.randint(0,9)
    x8 = random.randint(0,9)
    overall = f'{x1}{x2}{x3}{x4}{x5}{x6}{x7}{x8}'
    print('COPY THE 2FA AND PASTE IIT IN YOUR AUTHENTICATOR')
    print(f'2fa key,{overall}')
    print('')
    with open('project182facode.txt','w') as filee:
        filee.write(f'{overall}')

def login():
    while True:
        with open('project18email.txt') as file:
            lines = file.readlines()
        print('PROVIDE EMAIL')
        user = input('email\n: ')
        for  line in lines:
            if user != line.rstrip():
                print('email does not exist')
            elif user == line.rstrip():
                print('please wait.............................')
                break
        break
    print('')
    with open('project18pas.txt') as fille:
        linnes = fille.readlines()
        while True:
            print('PROVIDE PASSWORD TO CONTINUE')
            user = input('password\n: ')
            for linne in linnes:
                if user != linne.rstrip():
                    print('!!invalid password!!')
                elif user == linne.rstrip():
                    print('login successfull')
                    break
            break
    print('')
    login_auth()


def cassino_games():
    print("AVAILABLE GAMES")
    print("rock paper sissors",'number guessing')
    print('to play rock paper sissors input rock')
    print('to play number guessing input number')
    print('TO ACCESS SETTINGS PRINT SETTINGS')
    userr = input('provide choice\n: ')
    print('')
    if userr == 'rock':
        rock_paper_sissors()
    elif userr == ('number guessing'):
        number_guessing()
    elif  userr == 'setting':
        settings()

class Number:

    set1 = [1,2,3,4,5,6,7,8,9]

    @classmethod
    def shuffle(cls):
        return random.choice(cls.set1)
    
class Rock:

    rocks = ['rock','papper','sissors']

    @classmethod
    def shuffle(cls):
        return random.choice(cls.rocks)

def rock_paper_sissors():
    while True:
        user = input('provide choice\n: ')
        answer = Rock.shuffle()
        if user == 'home':
           cassino_games()
        while True:
            with open('project18cassinomoney.txt') as file:
                lines = file.readlines()
                for line in lines:
                    balance = int(line.rstrip())
                    print('INPUT BET')
                    bet = int(input('bet\n: '))
                    bett = (balance - bet)
                    profit = (bet + bet) + balance
                    print('')
                    if user != answer:
                        print(f'lost:{answer}')
                        print(bett)
                        with open('project18cassinomoney.txt','w') as fille:
                            fille.write(f'{bett}')
                    elif balance == 0:
                        print('not enough money top up')
                        deposit_money()
                    elif balance < bet:
                        print('not enough money bet lower')
                    elif user == answer:
                        print(f'won:{answer}')
                        print(profit)
                        with open('project18cassinomoney.txt','w') as fillle:
                            fillle.write(f'{profit}')
            break
        
        break
    rock_paper_sissors()
        
def number_guessing():
    while True:
        user = input('provide a lucky number 1 to 9\n: ')
        answer = Number.shuffle()
        if user == 'home':
            cassino_games()
        while True:
            with open('project18cassinomoney.txt') as file:
                lines = file.readlines()
                for line in lines:
                    balance = int(line.rstrip())
                    print("INPUT BET")
                    bet = int(input('bet\n: '))
                    bett = (balance - bet)
                    profit = (bet + bet) + balance
                    print('')
                    if user != answer:
                        print(bett)
                        with open('project18cassinomoney.txt','w') as fille:
                            fille.write(f'{bett}')
                    elif balance == 0:
                        print('not enough money top up')
                        deposit_money()
                    elif balance < bet:
                        print('not enough money bet lower')
                    elif user == answer:
                        print(profit)
                        with open('project18cassinomoney.txt','w') as fillle:
                            fillle.write(f'{profit}')
            break
        
        break                        

def settings():
    print('TO RETURN TO cassino INPUT cassino')
    print("TO CONTINUE INPUT continue")
    while True:
        y = input('choice\n: ')
        if y == 'cassino':
            cassino_games()
        if y == 'continue':
            print('')
            break
    print('PROVIDE SETTING TO NAVIGATE')
    print('TO CHANGE PASSWORD INPUT: password settings\nTO CREATE  OR CHAANGE AUTHENTICATOR INPUT:authenticator settings\nTO CHANGE EMAIL:email setttings\nTO GO TO ADVANCED SETTINGS:advanced settings')
    user = input('provide setting\n: ')
    if user == 'password settings':
        print('SURE TO CHANGE PASSWORD')
        x = input('choice\n: ')
        if x == 'yes' or 'YES' or 'Y':
            print('')
            change_password()
        elif x== 'no' or 'NO' or 'N':
            print('')
            user
    elif user == 'authenticator settings':
        print('SURE TO CHANGE OR CREATE AUTHENTICATOR')
        z = input('choice\n: ')
        if z == 'yes'  or 'YES' or 'Y' or 'Yes':
            print('')
            create_auth()
        elif z == 'no' or 'NO' or 'N' or "No":
            print('')
            user
    elif user == 'email settings':
        print('SURE TO CHANGE YOUR EMAIL')
        y = input('choice')
        if y == 'yes' or 'YES' or 'Yes' or 'Y':
            print('')
            change_email()
        elif y == 'no' or 'NO' or 'No' or 'N':
            print('')
            user
    elif user == 'advanced settings':
        print('SURE TO PROCEED TO ADVANCED SETTINGS')
        n = input('choice\n: ')
        if n == 'yes' or 'YES' or 'Yes' or  'Y':
            print('')
            advanced_settings()
        elif n == 'no' or 'No' or 'NO' or 'N':
            print('')
            user
    else:
        print('invalid option')

def change_password():
    print('TO RETURN TO setting INPUT settings')
    print('TO CONTINUE PRINT CONTINUE')
    while True:
        x = input('choice\n: ')
        if x == 'settings':
            settings()
        elif x == 'continue':
            break
    old_pas()
    new_pas()

def old_pas():
    print('INPUT CURRENT PASSWORD TO CONTINUE')
    while True:
        user = input('password\n: ')
        with open('project18pas.txt') as file:
            lines = file.readlines()
            print('')
            for line in lines:
                while True:
                    if user != line.rstrip():
                        print('invalid password')
                    elif user == line.rstrip():
                        print('access granted')
                        break
        break

def new_pas():
    old_pas()
    while True:
        print("PROVIDE NEW PASSWORD")
        pas = input('password\n: ')
        print('CONFIRM NEW PASSWORD')
        conf_pas = input('password\n: ')
        print('')
        if conf_pas != pas:
            print('passwords do not match')
        elif conf_pas == pas:
            print('password successfuly updated')
            break
        old_pas()
        login_auth()
        with open('project18pas.txt','w') as dile:
            dile.write(f'{conf_pas}')

def authenticator():
    create_auth()
    login_auth()

def create_auth():
    #write authenticator code 
    x1 = random.randint(0,9)
    x2 = random.randint(0,9)
    x3 = random.randint(0,9)
    x4 = random.randint(0,9)
    x5 = random.randint(0,9)
    x6 = random.randint(0,9) 
    x7 = random.randint(0,9)
    x8 = random.randint(0,9)

    overall = print(f'{x1}{x2}{x3}{x4}{x5}{x6}{x7}{x8}')

    while True:
        print('TO ADD OR CHANGE authenticator INPUT password')
        user = input('password\n: ')
        with open('project18pas.txt') as file:
            lines = file.readlines()
            print('')
            for line in lines:
                if user != line.rstrip():
                    print('invalid password')
                elif user == line.rstrip():
                    print('welcome')
                    break
        break

    print('TO ADD OR CHANGE authenticator COPY THE 2fa CODE AND PASTE IT IN THE authenticator')
    print(f'{overall}')
    with open('project182facode.txt','w') as fille:
        fille.write(f'{overall}')
    #input auth and password to set auth
    while True:
        print('PROVIDE AUTHENTICATOR CODE')
        auth = input('code\n: ')
        with open('project18authenticator.txt') as fiile:
            trees = fiile.readlines()
            print('')
            for tree in trees:
                if auth != tree.rstrip():
                    print('invalid code')
                elif auth == tree.rstrip():
                    print('please wait...............................')
        break
    while True:
        print('PROVIDE PASSWORD TO COMPLETE THE AUTHENTICATOR')
        pas = input('password\n: ')
        with open('project18pas.txt') as fi:
            cups = fi.readlines()
            print('')
            for cup in cups:
                if pas != cup.rstrip():
                    print('invalid password')
                elif pas == cup.rstrip():
                    print('succesfully created authenticator')
                    break
        break
    while True:
        print('PROVIDE AUTHENTICATOR CODE')
        code = input('code\n: ')
        with open('project18authenticator.txt') as file:
            lines = file.readlines()
            print('')
            for line in lines:
                if code != line.rstrip():
                    print('invalid authenticator')
                elif code == line.rstrip():
                    print('correct')
        break

def login_auth():
    while True:
        print('PROVIDE AUTHENTICATOR CODE')
        code = input('code\n: ')
        with open('project18authenticator.txt') as file:
            lines = file.readlines()
            for line in lines:
                if code != line.rstrip():
                    print('invalid authenticator')
                elif code == line.rstrip():
                    print('correct')
        break

def change_email():
    print('TO RETURN TO setting INPUT settings')
    while True:
        x = input('choice\n: ')
        print('')
        if x == 'settings':
            settings()
        elif x == '':
            break
    while True:
        print('PROVIDE OLD EMAIL')
        old_email = input('email\n: ')
        print('PROVIDE CURRENT EMAIL')
        new_email = input('email\n: ')
        print('')
        while True:
            choice = input('sure to change email (Y,N)\n: ')
            if choice == 'N':
                change_email()
            elif choice == 'Y':
                print('please wait .........................................')
                break
        with open('project18email.txt') as file:
            lines = file.readlines()
            for line in lines:
                if old_email != line.rstrip():
                    print('invalid email')
                elif old_email == line.rstrip():
                    print('please wait ..............................................')
                    break
        break
    old_pas()
    login_auth()
    with open('project18email.txt','w') as fille:
        fille.write(f'{new_email}')

def advanced_settings():
    print('TO ACCESS ADVANCED SETTINGS FOLLOW THE INNSTRUCTIONS')
    print('')
    old_pas()
    login_auth()
    print('DEPOSIT MONEY:deposit\nCHECK BALANCE:portfolio\nWITHDRAW MONEY:withdraw')
    user = input('choice\n: ')
    if user == 'deposit':
        print('')
        deposit_money()
    elif user == 'portfolio':
        print('')
        check_balance()
    elif user == 'withdraw':
        print('')
        withdraw_money()

def money():
    deposit_money()
    check_balance()
    withdraw_money()

def deposit_money():
    print('PROVIDE AMOUNT TO DEPOSIT')
    amount = int(input('amount\n: '))
    with open('project18bank.txt') as file:
        lines = file.readlines()
        for line in lines:
            bankbalance = int(line.rstrip())
            deposit = amount
            newbank_balance = bankbalance - deposit
            old_pas()
            login_auth()
    with open('projectbank.txt','w') as fill:
        fill.write(f'{newbank_balance}')
    #balance for cassino money
    print(f'balance:{amount}')
    print('')
    with open('project18cassinomoney.txt','w') as fille:
        fille.write(f'{deposit}')
    advanced_settings()

def check_balance():
    old_pas()
    login_auth()
    with open('project18cassinomoney.txt') as file:
        lines = file.readlines()
        for line in lines:
            print(f'BALANCE:{line.rstrip()}')
            print('TO RETURN TO SETTING:setting')
            choice = input('choice\n: ')
            if choice  == 'setting':
                advanced_settings()
                print('')

def withdraw_money():
    with open('project18cassinomoney.txt') as file:
        lines = file.readlines()
        for line in lines:
            balance = line.rstrip()
            user = input('provide amount to withdraw\n: ')
            withdrawal = balance - user
            with open('project18bank.txt')  as fille:
                trees = fille.readlines()
                for tree in trees:
                    balance1 = tree.rstrip()
                    withdrawal1 = withdrawal + balance1
                    if user == 'setting':
                        advanced_settings()
                    old_pas()
                    login_auth()
                    print('')
                    print(f'whithdrawal of ${withdrawal1} complete')
                    with open('project18bank.txt','w') as filee:
                        filee.write(f'{withdrawal1}')
                        advanced_settings()
                        

if __name__=='__main__':
    main()