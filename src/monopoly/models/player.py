from models.cell import Cell,City,Company,Airport
from typing import Tuple
import random

class Player:
    
    def __init__(self,name:str) -> None:
        self.name = name
        self.balance = 1500
        self.location = 0
        self.is_bankrupted = False
        self.is_in_jail = False
        self.last_roll:Tuple[int,int] = None
        self.turns_in_jail = 0
        self.rolled_double = False
        self.properties:list = []
        
    def move(self,num_spaces:int) -> None:
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
        if not property.is_owned:
            if isinstance(property,City) or isinstance(property,Company) or isinstance(property,Airport):
                self.balance-=property.price
                self.properties.append(property)
        
    def remove_property(self,property:Cell) -> None:
        self.properties.remove(property)
        
    def pay(self,amount:int,receiver:'Player') -> None:
        self.balance-=amount
        receiver.balance+=amount
        
    def bankrupted(self):
        self.is_bankrupted = True
        
    def roll_dice(self) -> Tuple[int,int]:
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        if dice1+dice2==12:
            self.rolled_double=True
        else:
            self.rolled_double=False
        print(f"{self.name} rolled {dice1} and {dice2} ({dice1+dice2})")
        self.last_roll = [dice1,dice2]
        return [dice1,dice2]
    
    
    def __str__(self) -> str:
        return f"{self.name}\n" \
            f"location: {self.location}\n" \
                f"balance: {self.balance}\n" \
                    f"props: {self.properties}"
    