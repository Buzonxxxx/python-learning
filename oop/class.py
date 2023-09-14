class PlayerCharacter:
    # Class Object Attribute: use when the value won't change in different instances
    membership = True
    
    # Constructor
    def __init__(self, name, age):
        if PlayerCharacter.membership:
            self.name = name # attributes
            self.age = age

    def shout(self):
        return f'my name is {self.name}'

    @classmethod
    def adding_things(cls, num1, num2):
        return cls('Teddy', num1 + num2)
    
    # static method 不用init class
    @staticmethod
    def adding_things2(num1, num2):
        return num1 + num2

# class method / static method 可以不用instantiate instance
print(PlayerCharacter.adding_things2(2,3)) #5

player1 = PlayerCharacter('Louis', 39)
player1.attack = 50

print(player1.name) # Louis
print(player1.attack) # 50
print(player1.shout()) # my name is Louis
print(player1.adding_things2(2,3)) # 5

player3 = PlayerCharacter.adding_things(2,3) # 5
print(player3.age)

# help(player1)
# help(str)
