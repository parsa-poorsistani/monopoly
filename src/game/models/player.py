from models.cell import Cell,City,Company,Airport
import random

class Player:
    
    def __init__(self,name:str) -> None:
        self.name = name
        self.balance = 1500
        self.location = 0
        self.is_bankrupted = False
        self.properties:list = []
        
    def move(self,num_spaces):
        self.location+=num_spaces
        if self.location >40:
            self.location -=39
            self.balance+=200
        #return self.location
    
    def net_worth(self) -> int:
        worth = 0
        for prop in self.properties:
            if isinstance(prop,City):
                worth+=prop.get_rent+prop.price
            elif isinstance(prop,Company):
                worth+=prop.price
            elif isinstance(prop,Airport):
                worth+=prop.price
        return worth
    
    def buy_property(self,property:Cell) -> None:
        self.properties.append(property)
        
    def remove_property(self,property:Cell) -> None:
        self.properties.remove(property)
        
    def pay(self,amount:int,receiver:'Player') -> None:
        self.balance-=amount
        receiver.balance+=amount
        
    def bankrupted(self):
        self.is_bankrupted = True
        
    def roll_dice(self) -> int:
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        print(f"{self.name} rolled {dice1} and {dice2} ({dice1+dice2})")
        return dice1+dice2
    
    
    def __str__(self) -> str:
        return f"{self.name}\n" \
            f"location: {self.location}\n" \
                f"balance: {self.balance}\n" \
                    f"props: {self.properties}"
    