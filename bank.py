import random

class Balance:
    def __init__(self,balance):
        self.balance = balance
    def __str__(self):
        return f'balance = {self.balance}'
    @classmethod
    def check_blnc(cls):
        with open('bank19.txt') as file:
            lines = file.readlines()
            for line in lines:
                balance = line.rstrip()
        return cls(balance)

class Deposit:
    def __init__(self,amount):
        self.amount = amount
    def __str__(self):
        return f'amount deposited: {self.amount}'
    @classmethod
    def moneyin(cls):
        while True:
            with open('bank19.txt') as file:
                lines = file.readlines()
                for line in lines:
                    balance = int(line.rstrip())
                    print('provide amount to deposit')
                    amount = int(input('amount\n: '))
                    deposit  = balance + amount
                    with open('bank19.txt','w') as fille:
                        fille.write(f'{deposit}')
                    print(f'deposit of,{amount} deposited successfully')
                    print('')
                    bank()
                    return cls(amount)

class Withdrawal:
    def __init__(self,ammount):
        self.ammount = ammount
    def __str__(self):
        return f'amount withdrawn: {self.ammount}'
    @classmethod
    def moneyout(cls):
        with open('bank19withdrawal.txt') as file:
            lines = file.readlines()
            for line in lines:
                ammount = int(line.rstrip())
                if ammount == 0:
                    print('invalid withdrawal')
                if ammount > 0:
                    with open('bank19.txt') as fille:
                        trees = fille.readlines()
                        for tree in trees:
                            balance = int(tree.rstrip())
                            withdraw = balance - ammount
                            with open('bank19.txt','w') as filee:
                                filee.write(f'{withdraw}')
                            with open('bank19withdraw.txt','w') as fi:
                                fi.write(f'{ammount}')
        old()

        return cls(ammount)

class Account:
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return f'account seccesfully created{self.name}'
    @classmethod
    def sign_up(cls):
        global name
        name = input('provide name\n: ')
        while True:
            age = int(input('provide age\n: '))
            if age < 18:
                print('too young')
            elif age >= 18:
                print(f'welcome,{name}')
                print('')
            break
        email = input('provide email\n: ')
        with open('bank19email.txt','w') as file:
            file.write(f'{email}')
        while True:
            pas1 = input('create new password\n: ')
            pas2 = input('confirm created password\n: ')
            if pas2 != pas1:
                print('paswords do not match')
            elif pas2 == pas1:
                print('password created succesfully')
            break
        bank
        with open('bank19pass.txt','w') as fille:
            fille.write(f'{pas2}')
        return cls(name)
        
    @classmethod
    def login(cls):
        with open('bank19email.txt') as file:
            lines = file.readlines()
            for line in lines:
                while True:
                    exist = line.rstrip()
                    user = input('provide email\n: ')
                    if user != exist:
                        print(f'invalid {user}, email does not exist')
                    elif user == exist:
                        print('valid email')
                        break
        print('')
        old()
        print('')
        bank()

def main():
    print('to log-in: 1')
    print('to  sign-up: 2')
    user = int(input('choice\n: '))
    if user == 1:
        log = Account.login()
        print(log)
    elif user == 2:
        sign = Account.sign_up()
        print(sign)
    else:
        print('invalid choice')

def bank():
    print('to check balance: bal')
    print('to deposit: dep')
    print('to  withdraw: with')
    print('for settings: sett')
    print('for crypto: crypto')
    user = input('choice\n: ')
    print('')
    if user == 'bal':
        check_balance()
    elif user == 'dep':
        deposit_accont()
    elif user == 'with':
        withdraw()
    elif user == 'sett':
        settings()
    elif user == 'crypto':
        crypto()
    else:
        print('invalid')
        bank()

def check_balance():
    user = Balance.check_blnc()
    print(user)
    print('')
    bank()
def deposit_accont():
    depo = Deposit.moneyin()
    print(depo)
    with open('bank19.txt') as file:
        lines = file.readlines()
        for line in lines:
            print(f'new balance = {line.rstrip()}')
    bank()

def withdraw():
    user = Withdrawal.moneyout()
    print(user)
    with open('bank19.txt') as file:
        lines = file.readlines()
        for line in lines:
            balance = line.rstrip()
            print(f'new balance: {balance}')
            print('')
    bank()

def settings():
    print('for password settings: pass')
    print('to go back out: exit')
    user = input('choice\n: ')
    print('')
    if user == 'pass':
        password()
    elif user == 'exit':
        print('please wait.................')
        print('')
        bank()
        print('')
    else:
        settings()

def password():
    print('for create new password: create')
    user = input('choice\n: ')
    print('')
    if user == 'create':
        old() ,print(''),create_new(),print(''),bank()
    elif user == '':
        password()

class Newpas:
    def __init__(self,pas2):
        self.pas2 = pas2
    def __str__(self):
        return f'password set successffully'

    @classmethod
    def createpas(cls):
        while True:
            pas1 = input('create new password\n: ')
            pas2 = input('confirm created password\n: ')
            with open('bank19pass.txt') as file:
                lines = file.readlines()
                for line in lines:
                    passnow = line.rstrip()
                    if pas2 != pas1:
                        print('invalid passwords do not match')
                    elif pas2 == passnow:
                        print('invalid: cannot change to existing password')
                        print('')
                        Newpas.createpas()
                    else:
                        break
                break
        print('password seccesffully changed')
        print('')
        with open('bank19pass.txt','w') as file:
            file.write(f'{pas2}')
        settings()
        return cls(pas2)

def create_new():
    user = Newpas.createpas()
    print(user)

class Oldpas:
    def __init__(self,user):
        self.user = user
    def __str__(self):
        return f'valid password welcome'
    @classmethod
    def old(cls):
        with open('bank19pass.txt') as file:
            lines = file.readlines()
            for line in lines:
                while True:
                    pas = line.rstrip()
                    user = input('provide password\n: ')
                    if user != pas:
                        print('invalid password')
                    else:
                        break
        return cls(user)

def old():
    user = Oldpas.old()
    print(user)

def crypto():
    with open('price.txt') as file:
        lines = file.readlines()
        for line in lines:
            pric = line.rstrip()
            price = format(pric)
            print(f'price: {price}')
            print('to go to porforlio: wallet')
            print('to buy: buy')
            print('to sell: sell')
            print('to go back: back')
            print('to go to metaverse: metaverse')
            user = input('choice\n: ')
            if user == 'buy':
                with open('buysellfinalconfirmation.txt','w') as file2:
                    file2.write(f'{user}')
                old()
                buy()
            elif user == 'sell':
                with open('buysellfinalconfirmation.txt','w') as file3:
                    file3.write(f'{user}')
                old()
                sell()
            elif user == 'back':
                bank()
            elif user == 'wallet':
                portforlio()
            elif user == 'metaverse':
                metaverse()
            else:
                crypto()

def buy():
    with open('bank19.txt') as file:
        lines = file.readlines()
        for line in lines:
            allmoney = float(line.rstrip())
    with open('price.txt') as file1:
        lines1 = file1.readlines()
        for line1 in lines1:
            price = float(line1.rstrip())
            print('provide amount of coins to be bought')
            user = float(input('amount\n: '))
            if user > 1000000000000:
                print('too many at once')
                buy()
            coinsboughtrequest = user
            moneyused = user * price
            with open('coinsboughtrequest.txt','w') as file2:
                file2.write(f'{coinsboughtrequest}')
    with open('usercoins.txt') as file6:
        lines6 = file6.readlines()
        for line6 in lines6:
            usercoins = float(line6.rstrip())
            usercoinbal = usercoins + user
    with open('requestbuyconfirmation.txt') as file3:
        lines3 = file3.readlines()
        for line3 in lines3:
            confirm = line3.rstrip()
            moneybal = allmoney - moneyused
            if confirm == 'Y' or 'y':
                print('block confirmation: confirm')
                print('block rejection: reject')
                user = 'confirm'
                if user == 'confirm':
                    with open('blockconfirmation.txt','w') as f:
                        f.write(f'{user}')
                    print('confirmed')
                elif user == 'reject':
                    with open('blockconfirmation.txt','w') as g:
                        g.write(f'{user}')
                    print('rejected')
    with open('blockconfirmationreturn.txt') as file9:
        lines9 = file9.readlines()
        for line9 in lines9:
            value = line9.rstrip()
            if value == 'confirm':
                with open('bank19.txt','w') as file4:
                    file4.write(f'{moneybal}')
                with open('usercoins.txt','w') as file5:
                    file5.write(f'{usercoinbal}')
                print('transaction succesfull')
                crypto()
            elif value == 'reject':
                print('transaction failed')
                buy()
            else:
                print('transaction failed')
                buy
    x = ''
    with open('requestbuyconfirmation.txt','w') as file7:
        file7.write(f'{x}')
    print('')

def market_cap():
    with open('totalcoinsbought.txt') as file:
        lines = file.readlines()
        for line in lines:
            totalcoinsbought = line.rstrip()
    with open('price.txt') as file1:
        lines1 = file1.readlines()
        for line1 in lines1:
            price = line1.rstrip()
            marketcap = totalcoinsbought * price
            with open('blockchainmarketcap.txt','w') as di:
                di.write(f'{marketcap}')

def sell():
    with open('usercoins.txt') as file:
        lines = file.readlines()
        for line in lines:
            coins = float(line.rstrip())
            print('enter amount to sell')
            user = float(input('ammount\n: '))
            if user > 50000000000000:
                print('too many at once')
                sell()
            coinssold = user
            usercoinsbal = coins - user
    with open('price.txt') as file2:
        lines2 = file2.readlines()
        for line2 in lines2:
            price  = float(line2.rstrip())
            moneygained = coinssold * price
            with open('coinssoldrequest.txt','w') as file3:
                file3.write(f"{coinssold}")
    with open('bank19.txt') as file4:
        lines4 = file4.readlines()
        for line4 in lines4:
            allmoney = float(line4.rstrip())
            bankbal = allmoney + moneygained
    with open('requestsellconfirmation.txt') as file5:
        lines5 = file5.readlines()
        for line5 in lines5:
            confirm = line5.rstrip()
            if confirm == 'Y' or 'y':
                print('block confirmation: confirmed')
                user1 = 'confirm'
                if user1 == 'confirm':
                    with open('blocksellconfirmation.txt','w') as fil:
                        fil.write(f'{user1}')
                    print('requested')
                elif user != 'confirm':
                    with open('blocksellconfirmation.txt','w') as fi:
                        fi.write(f'{user1}')
    with open('blockconfirmation.txt') as file9:
        lines9 = file9.readlines()
        for line9 in lines9:
            blockconfirmation = line9.rstrip()
            if blockconfirmation == 'confirm' or 'CONFIRM':                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
                with open('bank19.txt','w') as file6:
                    file6.write(f'{bankbal}')
                with open('usercoins.txt','w') as file7:
                    file7.write(f'{usercoinsbal}')
                print('transaction succesfull')
            elif blockconfirmation == 'reject' or 'REJECT':
                print('transaction failed')
                sell()
            else:
                print('transaction failed')
                sell()
        x = ''
        with open('requestsellconfirmation.txt','w') as file8:
            file8.write(f'{x}')

def portforlio():
    old()
    print('please wait..........................')
    with open('usercoins.txt') as file:
        lines = file.readlines()
        for line in lines:
            coins = float(line.rstrip())
            print('WALLET')
            print(f'BLACK COIN: {coins}')
    with open('price.txt') as file2:
        lines2=file2.readlines()
        for line2 in lines2:
            price = float(line2.rstrip())
            value = coins * price
            print(f'value in USD: {value}')
            print('')
            crypto()

def metaverse():
    print("AVAILABLE GAMES")
    print(':rock paper sissors:number guessing:')
    print('to play rock paper sissors: rock')
    print('to play number guessing: number')
    print('to go back: back')
    userr = input('provide choice\n: ')
    print('')
    if userr == 'rock':
        rock_paper_sissors()
    elif userr == ('number guessing'):
        number_guessing()
    elif  userr == 'back':
        crypto()

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
        answer = Rock.shuffle()
        user = input('provide choice\n: ')
        if user == 'home':
           bank()
        with open('cassinocoins.txt') as file2:
            lines1 = file2.readlines()
            for line1 in lines1:
                cassinocoins = float(line1.rstrip())
        with open('usercoins.txt') as file:
            lines = file.readlines()
            for line in lines:
                coins = float(line.rstrip())
                while True:
                    print('input amount to place bet')
                    user1 = float(input('amount\n: '))
                    if user == answer:
                        y = cassinocoins - user1
                        x = coins + user1
                        with open('usercoins.txt','w') as file1:
                            file1.write(f'{x}')
                        with open('cassinocoins.txt','w') as file3:
                            file3.write(f'{y}')
                        print(f'won:  +{user1}')
                    elif user != answer:
                        y1 = cassinocoins + user1
                        x1 = coins - user1
                        with open('usercoins.txt','w') as file1:
                            file1.write(f'{x1}')
                        with open('cassinocoins.txt','w') as file4:
                            file4.write(f'{y1}')
                        print(f'lost: -{user1}')
                    break
                
        break
    rock_paper_sissors()
        
def number_guessing():
    while True:
        user = input('provide a lucky number 1 to 9\n: ')
        answer = Number.shuffle()
        if user == 'home':
            bank()     
        with open('cassinocoins.txt') as file2:
            lines1 = file2.readlines()
            for line1 in lines1:
                cassinocoins = float(line1.rstrip())
        with open('usercoins.txt') as file:
            lines = file.readlines()
            for line in lines:
                coins = float(line.rstrip())
                while True:
                    print('input amount to place bet')
                    user1 = float(input('amount\n: '))
                    if user == answer:
                        y = cassinocoins - user1
                        x = coins + user1
                        with open('usercoins.txt','w') as file1:
                            file1.write(f'{x}')
                        with open('cassinocoins.txt','w') as file3:
                            file3.write(f'{y}')
                        print(f'won: +{user1}')
                    elif user != answer:
                        y1 = cassinocoins + user1
                        x1 = coins - user1
                        with open('usercoins.txt','w') as file1:
                            file1.write(f'{x1}')
                        with open('cassinocoins.txt','w') as file4:
                            file4.write(f'{y1}')
                        print(f'lost: -{user1}')
                    elif user1 == 'back':
                        crypto()
                    break
        break

if __name__=='__main__':
    main()