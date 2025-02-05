class User:
    def sign_in(self):
        return 'Logged in'

    def attack(self):
        print('do nothing')

class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power
    
    def attack(self):
        print(f'attacking with power of {self.power}')

class Archer(User):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows
    
    def check_arrows(self):
        print(f'{self.arrows} remaining')
    
    def run (self):
        print('ran really fast')

class HybridBorg(Wizard, Archer):
    def __init__(self, name, power, arrows):
        Archer.__init__(self, name, arrows)
        Wizard.__init__(self, name, power)

hb1 = HybridBorg('borgie', 50, 100)
print(hb1.run()) #ran really fast
print(hb1.check_arrows()) #100 remaining
print(hb1.attack()) #attacking with power of 50
print(hb1.sign_in())