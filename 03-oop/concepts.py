"""
Four Pillars of OOP

1. Encapsulate
Bundle the data and the methods that operate on that data into a single unit called a class

2. Abstraction
Call the function without knowing how to implement it

3. Inheritance

4. Polymorphism = Many forms
Redefine methods
"""

# Private: undescore
class PlayerCharacter:
    # dunder method: don't modify it
    def __init__(self, name, age):
        self._name = name # attributes
        self._age = age

# Inheritance
class User:
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        return 'Logged in'

    def attack(self):
        print('do nothing')

class Wizard(User):
    def __init__(self, name, power, email):
        super().__init__(email)
        self.name = name
        self.power = power
    
    def attack(self):
        User.attack(self)
        print(f'attacking with power of {self.power}')

class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows
    
    def attack(self):
        print(f'attacking with arrows of {self.num_arrows}')

wizard1 = Wizard('Merlin', 60, 'merlin@gmail.com')
print(wizard1.email) #merlin@gmail.com


# isinstance()
print(isinstance(wizard1, Wizard)) # True
print(isinstance(wizard1, User)) # True
# Python base class: object
print(isinstance(wizard1, object)) # True

# Polymorphism
archer1 = Archer("Robn", 30)

def player_attack(char):
    char.attack()

player_attack(wizard1) #do nothing
                       #attacking with power of 60
                       
player_attack(archer1) #attacking with arrows of 30

# introspection
print(dir(wizard1))

