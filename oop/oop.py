class PlayerCharacter:
    # Class Object Attribute: use when the value won't change in different instances
    membership = True
    
    # Constructor
    def __init__(self, name, age):
        if PlayerCharacter.membership:
            self.name = name # attributes
            self.age = age

    def shout(self):
        print(f'my name is {self.name}')

player1 = PlayerCharacter('Louis', 39)
player1.attack = 50

print(player1.name)
print(player1.age)
print(player1.attack)
print(player1.shout())

# help(player1)
# help(str)
