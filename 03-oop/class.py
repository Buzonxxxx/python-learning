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

    '''
    類方法（@classmethod)
        用途：當你需要訪問或修改類屬性，或者需要在不創建實例的情況下執行與類相關的操作時，使用類方法。
        特點:類方法接收一個隱含的第一個參數cls,代表類本身。
        使用情境：
            創建類的工廠方法(factory method),用於創建類的實例。
            訪問或修改類屬性。
            執行與類相關的操作，而不需要實例。
    '''
    @classmethod
    def adding_things(cls, num1, num2):
        return cls('Teddy', num1 + num2)
    
    '''
    靜態方法通常用於執行一些與類相關但不需要訪問類或實例屬性的方法。它們更像是類內部的普通函數。
    '''
    @staticmethod
    def adding_things2(num1, num2):
        return num1 + num2

print(PlayerCharacter.adding_things2(2,3)) # 5

player1 = PlayerCharacter('Louis', 39)
player1.attack = 50

print(player1.name) # Louis
print(player1.attack) # 50
print(player1.shout()) # my name is Louis
print(player1.adding_things2(2,3)) # 5

player3 = PlayerCharacter.adding_things(2,3)
print(player3.age) # 5
