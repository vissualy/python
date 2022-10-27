def main():
    blockchain()

def blockchain():
    print('to access admin: pass')
    with open('bank19pass.txt') as file:
        lines = file.readlines()
        for line in lines:
            pas = line.rstrip()
            user = input('pass\n: ')
            if user == pas:
                admin()
            else:
                blockchain()

def admin():
    with open('buysellfinalconfirmation.txt') as file:
        lines = file.readlines()
        for line in lines:
            user = line.rstrip()
            if user == 'buy':
                buying()
            elif user == 3:
                selling()
    print('advanced setting')
    user2 = input('choice')
    if user == 1:
        existence()
    elif user == 4:
                burning()
    elif user == 5:
                price_movement()

def coins():
    existence()
    buying()
    selling()
    burning()
    price_movement()

class Coin_prove():
    def __init__(self,totalcoins):
        self.totalcoins = totalcoins
    def __str__(self):
        return f'coins in circulation: {self.totalcoins}'

    @classmethod
    def prove(cls):
        with open('coins.txt') as file:
            lines = file.readlines()
            for line in lines:
                totalcoins = line.rstrip()
                return cls(totalcoins)

def existence():
    content = Coin_prove.prove()
    print(content)

def buying():
    with open('coinsboughtrequest.txt') as file:
        lines = file.readlines()
        for line in lines:
            coinsrequest = float(line.rstrip())
    with open('coins.txt') as file1:
        lines1 = file1.readlines()
        for line1 in lines1:
            coins = float(line1.rstrip())
            buyin = coins - coinsrequest
            with open('buying.txt','w') as w:
                w.write(f'{buyin}')
            print('')
            print('to confirm buy: Y')
            print('to reject buy: N')
            user = 'y'
            if user == 'Y' or 'y':
                with open('requestbuyconfirmation.txt','w') as file2:
                    file2.write(f'{user}')
                    print('request approved')
            elif user == 'N' or 'y':
                with open('requestbuyconfirmation.txt','w') as file4:
                    file4.write(f'{user}')
                    print('request rejected')
    with open('blockconfirmation.txt') as file3:
        lines3 = file3.readlines()
        for line3 in lines3:
            blockconfirmation = line3.rstrip()
            if blockconfirmation == 'confirm' or 'CONFIRM':
                print('confirm clock: confirm')
                print('rejectblock: reject')
                user1 = 'confirm'
                if user == 'confirm' or 'CONFIRM':
                    with open('blockconfirmationreturn.txt','w') as file5:
                        file5.write(f'{user1}')
                    print('request aproved')
                    with open('totalcoinsbought.txt','w') as fol:
                        fol.write(f'{coinsrequest}')
                    bought()
                    burning()
            elif user == 'reject' or "REJECT":
                with open('blockconfirmationreturn.txt','w') as file6:
                    file6.write(f'{user1}')
                print('request rejected')
def bought():
    with open('buying.txt') as file:
        lines = file.readlines()
        for line in lines:
            buying = line.rstrip()
            with open('coins.txt','w') as w:
                w.write(f'{buying}')
                price_buy()
                    
def selling():
    with open('coinssoldrequest.txt') as file:
        lines = file.readlines()
        for line in lines:
            coinsrequest = line.rstrip()
    with open('coins.txt') as file2:
        lines2 = file2.readlines()
        for line2 in lines2:
            coins = line2.rstrip()
            sellin = coins + coinsrequest
            with open('selling.txt','w')as w:
                w.write(f'{sellin}')
            print('')
            print('to confirm sell: Y')
            print('to reject buy: N')
            user = 'Y'
            if user == 'Y' or 'y':
                with open('requestsellconfirmation.txt','w') as file3:
                    file3.write(f'{user}')
                    print('request approved')
            elif user == 'N' or 'n':
                with open('requestsellconfirmation.txt','w') as file5:
                    file5.write(f'{user}')
                    print('request rejected')
def sold():
    with open('selling.txt') as file:
        lines = file.readlines()
        for line in lines:
            sell = line.rstrip()
            with open('coins.txt') as w:
                w.write(f'{sell}')
                price_sell()


def price_movement():
    price_buy()
    price_sell()
def price_buy():
    with open('coinsboughtrequest.txt') as file:
        lines = file.readlines()
        for line in lines:
            coins = float(line.rstrip())
            with open('price.txt') as fop:
                trees = fop.readlines()
                for tree in trees:
                    price = float(tree.rstrip())
                    if coins >= 10000000 < 25000000:
                        price1 = price * 2
                        with open('price.txt','w') as fil:
                            fil.write(f'{price1}')
                    elif coins >= 25000000 < 50000000:
                        price2 = price * 3
                        with open('price.txt','w') as file1:
                            file1.write(f'{price2}')
                    elif coins >=50000000 < 100000000:
                        price3 = price * 4
                        with open('price.txt','w') as file2:
                            file2.write(f'{price3}')
                    elif coins >= 100000000 < 200000000:
                        price4 = price * 5
                        with open('price.txt','w') as file3:
                            file3.write(f'{price4}')
                    elif coins >= 200000000 < 300000000:
                        price5 = price * 6
                        with open('price.txt','w') as  file4:
                            file4.write(f'{price5}')
                    elif coins >= 300000000 < 400000000:
                        price6  = price * 7
                        with open('price.txt','w') as file5:
                            file5.write(f'{price6}')
                    elif coins >= 400000000 < 500000000:
                        price7 = price * 8
                        with open('price.txt','w') as file6:
                            file6.write(f'{price7}')
                    elif coins >= 50000000 < 600000000:
                        price8 = price * 9
                        with open('price.txt','w') as file7:
                            file7.write(f'{price8}')
                    elif coins >= 600000000 < 700000000:
                        price9  = price * 10
                        with open('price.txt','w') as file8:
                            file8.write(f'{price9}')
                    elif coins>= 700000000 < 800000000:
                        price10 = price * 11
                        with open('price.txt','w') as file9:
                            file9.write(f'{price10}')
                    elif coins >= 800000000 < 900000000:
                        price11 = price*12
                        with open('price.tx','w') as file10:
                            file10.write(f'{price11}')
                    elif coins >= 900000000 < 1000000000:
                        price12 = price*13
                        with open('price.txt','w') as file11:
                            file11.write(f'{price12}')
                    elif coins >= 1000000000 < 2000000000:
                        price13 = price*14
                        with open('price.txt','w') as file12:
                            file12.write(f'{price13}')
                    elif coins >= 2000000000 < 4000000000:
                        price14 = price * 15
                        with open('price.txt','w') as file13:
                            file13.write(f'{price14}')
                    elif coins >= 4000000000 < 6000000000:
                        price15 = price * 16
                        with open('price.txt','w') as file14:
                            file14.write(f'{price15}')
                    elif coins >= 6000000000 < 8000000000:
                        price16 = price * 17
                        with open('price.txt','w') as file15:
                            file15.write(price16)
                    elif coins >= 8000000000 <10000000000:
                        price17 = price*18
                        with open('price.txt','w') as file16:
                            file16.write(f'{price17}')
                    elif coins >= 10000000000 < 20000000000:
                        price18 = price* 19
                        with open('price.txt','w') as file17:
                            file17.write(f'{price18}')
                    elif coins >= 20000000000 < 30000000000:
                        price19 = price*20
                        with open('price.txt','w') as file18:
                            file18.write(f'{price19}')
                    elif coins >= 30000000000 < 40000000000:
                        price20 = price*21
                        with open('price.txt','w') as file21:
                            file21.write(f'{price20}')
                    elif coins >= 40000000000 < 50000000000:
                        price21 = price * 22
                        with open('price.txt','w') as file22:
                            file22.write(f'{price21}')
                    elif coins >= 50000000000 < 60000000000:
                        price22 = price * 23
                        with open('price.txt','w') as file23:
                            file23.write(f'{price22}')
                    elif coins >= 60000000000 < 70000000000:
                        price23 = price * 24
                        with open('price.txt','w') as file24:
                            file24.write(f'{price23}')
                    elif coins >= 70000000000 < 80000000000:
                        price24 = price*25
                        with open('price.txt','w') as file25:
                            file25.write(price24)
                    elif coins >= 80000000000 < 90000000000:
                        price25 = price * 26
                        with open('price.txt','w') as file26:
                            file26.write(f'{price25}')
                    elif coins >= 90000000000 < 100000000000:
                        price26 = price * 27
                        with open('price.txt','w') as file27:
                            file27.write(f'{price26}')
                    elif coins >= 100000000000 < 200000000000:
                        price27 = price * 28
                        with open('price.txt','w') as file28:
                            file28.write(price27)
                    elif coins >= 200000000000 < 400000000000:
                        price28 = price * 29
                        with open('price.txt','w') as file29:
                            file29.write(f'{price28}')
                    elif coins >= 400000000000 < 600000000000:
                        price29 = price * 30
                        with open('price.txt','w') as file30:
                            file30.write(f'{price29}')
                    elif coins >= 600000000000 < 800000000000:
                        price30 = price * 31
                        with open('price.txt','w') as file31:
                            file31.write(f'{price30}')
                    elif coins >= 800000000000 < 1000000000000:
                        price31  = price * 32
                        with open('price.txt','w') as file31:
                            file31.write(f'{price31}')
def price_sell():
    with open('coinssoldrequest.txt') as file:
        lines = file.readlines()
        for line in lines:
            coins = float(line.rstrip())
            with open('price.txt') as fop:
                trees = fop.readlines()
                for tree in trees:
                    price = float(tree.rstrip())
                    if coins >= 10000000 < 50000000:
                        price1 = price / 2
                        with open('price.txt','w') as fil:
                            fil.write(f'{price1}')
                    elif coins >= 50000000 < 100000000:
                        price2 = price / 3
                        with open('price.txt','w') as file1:
                            file1.write(f'{price2}')
                    elif coins >=100000000 < 200000000:
                        price3 = price / 4
                        with open('price.txt','w') as file2:
                            file2.write(f'{price3}')
                    elif coins >= 200000000 < 300000000:
                        price4 = price / 5
                        with open('price.txt','w') as file3:
                            file3.write(f'{price4}')
                    elif coins >= 300000000 < 400000000:
                        price5 = price / 6
                        with open('price.txt','w') as  file4:
                            file4.write(f'{price5}')
                    elif coins >= 400000000 < 500000000:
                        price6  = price / 7
                        with open('price.txt','w') as file5:
                            file5.write(f'{price6}')
                    elif coins >= 500000000 < 600000000:
                        price7 = price / 8
                        with open('price.txt','w') as file6:
                            file6.write(f'{price7}')
                    elif coins >= 60000000 < 700000000:
                        price8 = price / 9
                        with open('price.txt','w') as file7:
                            file7.write(f'{price8}')
                    elif coins >= 700000000 < 800000000:
                        price9  = price / 10
                        with open('price.txt','w') as file8:
                            file8.write(f'{price9}')
                    elif coins>= 800000000 < 900000000:
                        price10 = price / 11
                        with open('price.txt','w') as file9:
                            file9.write(f'{price10}')
                    elif coins >= 900000000 < 1000000000:
                        price11 = price/12
                        with open('price.tx','w') as file10:
                            file10.write(f'{price11}')
                    elif coins >= 1000000000 < 20000000000:
                        price12 = price/13
                        with open('price.txt','w') as file11:
                            file11.write(f'{price12}')
                    elif coins >= 20000000000 < 30000000000:
                        price13 = price/14
                        with open('price.txt','w') as file12:
                            file12.write(f'{price13}')
                    elif coins >= 30000000000 < 40000000000:
                        price14 = price / 15
                        with open('price.txt','w') as file13:
                            file13.write(f'{price14}')
                    elif coins >= 40000000000 < 50000000000:
                        price15 = price / 16
                        with open('price.txt','w') as file14:
                            file14.write(f'{price15}')
                    elif coins >= 50000000000 < 60000000000:
                        price16 = price / 17
                        with open('price.txt','w') as file15:
                            file15.write(price16)
                    elif coins >= 60000000000 <70000000000:
                        price17 = price/18
                        with open('price.txt','w') as file16:
                            file16.write(f'{price17}')
                    elif coins >= 70000000000 <80000000000:
                        price18 = price/ 19
                        with open('price.txt','w') as file17:
                            file17.write(f'{price18}')
                    elif coins >= 80000000000 < 90000000000:
                        price19 = price/20
                        with open('price.txt','w') as file18:
                            file18.write(f'{price19}')
                    elif coins >= 90000000000 < 100000000000:
                        price20 = price/21
                        with open('price.txt','w') as file21:
                            file21.write(f'{price20}')
                    elif coins >= 100000000000 < 200000000000:
                        price21 = price / 22
                        with open('price.txt','w') as file22:
                            file22.write(f'{price21}')
                    elif coins >= 200000000000 < 300000000000:
                        price22 = price / 23
                        with open('price.txt','w') as file23:
                            file23.write(f'{price22}')
                    elif coins >= 300000000000 < 400000000000:
                        price23 = price / 24
                        with open('price.txt','w') as file24:
                            file24.write(f'{price23}')
                    elif coins >= 400000000000 < 500000000000:
                        price24 = price/25
                        with open('price.txt','w') as file25:
                            file25.write(price24)
                    elif coins >= 500000000000 < 600000000000:
                        price25 = price / 26
                        with open('price.txt','w') as file26:
                            file26.write(f'{price25}')
                    elif coins >= 600000000000 < 700000000000:
                        price26 = price / 27
                        with open('price.txt','w') as file27:
                            file27.write(f'{price26}')
                    elif coins >= 700000000000 < 800000000000:
                        price27 = price / 28
                        with open('price.txt','w') as file28:
                            file28.write(price27)
                    elif coins >= 800000000000 < 900000000000:
                        price28 = price / 29
                        with open('price.txt','w') as file29:
                            file29.write(f'{price28}')
                    elif coins >= 900000000000 < 1000000000000:
                        price29 = price / 30
                        with open('price.txt','w') as file30:
                            file30.write(f'{price29}')
                    elif coins >= 1000000000000 < 2000000000000:
                        price30 = price / 31
                        with open('price.txt','w') as file31:
                            file31.write(f'{price30}')
                    elif coins >= 2000000000000 < 50000000000000:
                        price31  = price / 32
                        with open('price.txt','w') as file31:
                            file31.write(f'{price31}')

def burning():
    with open('coinsboughtrequest.txt') as file:
        lines = file.readlines()
        for line in lines:
            coins = float(line.rstrip())
            with open('coins.txt') as fop:
                trees = fop.readlines()
                for tree in trees:
                    price = float(tree.rstrip())
                    if coins >= 10000000 < 50000000:
                        price1 = price - 100000
                        with open('coins.txt','w') as fil:
                            fil.write(f'{price1}')
                    elif coins >= 50000000 < 100000000:
                        price2 = price - 120000
                        with open('coins.txt','w') as file1:
                            file1.write(f'{price2}')
                    elif coins >=100000000 < 200000000:
                        price3 = price - 140000
                        with open('coins.txt','w') as file2:
                            file2.write(f'{price3}')
                    elif coins >= 200000000 < 300000000:
                        price4 = price - 160000
                        with open('coins.txt','w') as file3:
                            file3.write(f'{price4}')
                    elif coins >= 300000000 < 400000000:
                        price5 = price - 180000
                        with open('coins.txt','w') as  file4:
                            file4.write(f'{price5}')
                    elif coins >= 400000000 < 500000000:
                        price6  = price - 200000
                        with open('coins.txt','w') as file5:
                            file5.write(f'{price6}')
                    elif coins >= 500000000 < 600000000:
                        price7 = price - 240000
                        with open('coins.txt','w') as file6:
                            file6.write(f'{price7}')
                    elif coins >= 60000000 < 700000000:
                        price8 = price - 280000
                        with open('coins.txt','w') as file7:
                            file7.write(f'{price8}')
                    elif coins >= 700000000 < 800000000:
                        price9  = price - 320000
                        with open('coins.txt','w') as file8:
                            file8.write(f'{price9}')
                    elif coins>= 800000000 < 900000000:
                        price10 = price - 4600000
                        with open('coins.txt','w') as file9:
                            file9.write(f'{price10}')
                    elif coins >= 900000000 < 1000000000:
                        price11 = price - - 500000
                        with open('coins.tx','w') as file10:
                            file10.write(f'{price11}')
                    elif coins >= 1000000000 < 20000000000:
                        price12 = price - 550000
                        with open('coins.txt','w') as file11:
                            file11.write(f'{price12}')
                    elif coins >= 20000000000 < 30000000000:
                        price13 = price - 600000
                        with open('coins.txt','w') as file12:
                            file12.write(f'{price13}')
                    elif coins >= 30000000000 < 40000000000:
                        price14 = price - 650000
                        with open('coins.txt','w') as file13:
                            file13.write(f'{price14}')
                    elif coins >= 40000000000 < 50000000000:
                        price15 = price - 70000
                        with open('coins.txt','w') as file14:
                            file14.write(f'{price15}')
                    elif coins >= 50000000000 < 60000000000:
                        price16 = price - 750000
                        with open('coins.txt','w') as file15:
                            file15.write(price16)
                    elif coins >= 60000000000 <70000000000:
                        price17 = price - 750000
                        with open('coins.txt','w') as file16:
                            file16.write(f'{price17}')
                    elif coins >= 70000000000 <80000000000:
                        price18 = price - 800000
                        with open('coins.txt','w') as file17:
                            file17.write(f'{price18}')
                    elif coins >= 80000000000 < 90000000000:
                        price19 = price - 850000
                        with open('coins.txt','w') as file18:
                            file18.write(f'{price19}')
                    elif coins >= 90000000000 < 100000000000:
                        price20 = price - 900000
                        with open('coins.txt','w') as file21:
                            file21.write(f'{price20}')
                    elif coins >= 100000000000 < 200000000000:
                        price21 = price - 950000
                        with open('coins.txt','w') as file22:
                            file22.write(f'{price21}')
                    elif coins >= 200000000000 < 300000000000:
                        price22 = price - 1000000
                        with open('coins.txt','w') as file23:
                            file23.write(f'{price22}')
                    elif coins >= 300000000000 < 400000000000:
                        price23 = price - 1100000
                        with open('coins.txt','w') as file24:
                            file24.write(f'{price23}')
                    elif coins >= 400000000000 < 500000000000:
                        price24 = price - 1200000
                        with open('coins.txt','w') as file25:
                            file25.write(price24)
                    elif coins >= 500000000000 < 600000000000:
                        price25 = price - 1300000
                        with open('coins.txt','w') as file26:
                            file26.write(f'{price25}')
                    elif coins >= 600000000000 < 700000000000:
                        price26 = price - 1400000
                        with open('coins.txt','w') as file27:
                            file27.write(f'{price26}')
                    elif coins >= 700000000000 < 800000000000:
                        price27 = price - 1500000
                        with open('coins.txt','w') as file28:
                            file28.write(price27)
                    elif coins >= 800000000000 < 900000000000:
                        price28 = price - 1600000
                        with open('coins.txt','w') as file29:
                            file29.write(f'{price28}')
                    elif coins >= 900000000000 < 1000000000000:
                        price29 = price - 1700000
                        with open('coins.txt','w') as file30:
                            file30.write(f'{price29}')
                    elif coins >= 1000000000000 < 2000000000000:
                        price30 = price - 1800000
                        with open('coins.txt','w') as file31:
                            file31.write(f'{price30}')
                    elif coins >= 2000000000000 < 50000000000000:
                        price31  = price - 1900000
                        with open('coins.txt','w') as file31:
                            file31.write(f'{price31}')

if __name__=='__main__':
    main()