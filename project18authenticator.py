import random

class Facode:
    def __init__(self,user,aut):
        self.user = user
        self.aut = aut
        while True:
            with open('project182facode.txt') as file:
                lines = file.readlines()
                for line in lines:
                    if self.user != line.rstrip():
                        print('incorrect 2fa')
                    elif self.user == line.rstrip():
                        print(self.aut)
            break
class Authentic:
    x1 = random.randint(0,9)
    x2 = random.randint(0,9)
    x3 = random.randint(0,9)
    x4 = random.randint(0,9)
    x5 = random.randint(0,9)
    x6 = random.randint(0,9)
    x7 = random.randint(0,9)
    x8 = random.randint(0,9)
    x9 = random.randint(0,9)
    x10 = random.randint(0,9)
    x11 = random.randint(0,9)
    x12 = random.randint(0,9)
    x13 = random.randint(0,9)
    x14 = random.randint(0,9)
    x15 = random.randint(0,9)
    x16 = random.randint(0,9)
    overall = f'{x1}{x2}{x3}{x4}{x5}{x6}{x7}{x8}{x9}{x10}{x11}{x12}{x13}{x14}{x15}{x16}'
    @classmethod
    def authenticator(cls):
        while True:
            return cls.overall
    with open('project18authenticator.txt','w') as file:
        file.write(f'{overall}')

def main():
    auth()
    

def auth():
    user = input('provide 2fa code\n: ')
    aut = Authentic.authenticator()
    return Facode(user,aut)

if __name__=='__main__':
    main()