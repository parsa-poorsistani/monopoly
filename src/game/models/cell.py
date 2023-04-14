from abc import ABC
from models.player import Player
from enums.group_enums import GroupEnum
from typing import Tuple

class Cell(ABC):
    def __init__(self,name:str,location:int,owner:Player=None) -> None:
        self.name = name
        self.location = location
        self.owner = owner
        self.landed_palyers:list = []
        
class EmptyCell(Cell):
    def __init__(self, name: str, location: int) -> None:
        super().__init__(name, location)
    
class City(Cell):
    def __init__(self, name: str, location: int, price:int, group:GroupEnum) -> None:
        super().__init__(name, location)
        self.price = price
        self.group = group
        self.rent = 0
        self.num_houses = 0
        self.num_hotel = 0
        
    def is_owned(self) -> bool:
        return True if self.owner!=None else False
    
    def get_owner(self) -> Player:
        return self.owner
    
    def buy(self,buyer:Player)->None:
        self.owner = buyer

    def get_rent(self) -> int:
        if self.owner is None:
            return 0
        return self.rent * (2 ** self.num_houses)
    
    def is_monopoly(self) -> bool:
        if self.owner is None:
            return False
        for property in self.owner.properties:
            if property.group==self.group and property.owner!=self.owner:
                return False
        return True

    def buy_house(self) -> bool:
        if self.owner is None:
            return False
        if self.num_houses<4 and self.num_hotel==0:
            self.num_houses+=1
            self.owner.balance-=self.price * 0.5
            return True
        return False
    
    def buy_hotel(self) -> None:
        if self.num_houses == 4 and self.num_hotel == 0:
            self.num_houses = 4
            self.num_hotel = 1
            self.owner.balance -= self.price * 0.5
    
    def sell_house(self) -> bool:
        if self.num_hotel==0 and self.num_houses>0:
            self.num_houses-=1
            self.owner.balance+=self.price * 0.25
            return True
        elif self.num_hotel==1:
            self.num_houses=4
            self.num_hotel=0
            self.owner.balance+=self.price * 0.25
            return True
        return False
    
    def sell(self) -> None:
        self.owner = None
        self.num_houses = 0
        self.num_hotels = 0
        
class Jail(Cell):
    def __init__(self, name: str, location: int) -> None:
        super().__init__(name, location)
        
    def landed_on(self,player:Player) -> None:
        self.landed_palyers.append(player)
    
    def bail_out(self,player:Player) -> bool:
        if player.balance>=50:
            player.balance-=50
            self.landed_palyers.remove(player)
            return True
        return False


# should get complete
class Vacation(Cell):
    def __init__(self, name: str, location: int) -> None:
        super().__init__(name, location)
        
    def landed_on(self,player:Player) -> None:
        self.landed_palyers.append(player)
        
    def lands_off(self,player:Player) -> None:
        self.landed_palyers.remove(player)
        
    def is_is_vacation(self,player:Player) -> bool:
        if player in self.landed_palyers:
            return True
        return False
    
    
class Company(Cell):
    def __init__(self, name: str, location: int,price:int) -> None:
        super().__init__(name, location)
        self.price = price
    
    def get_rent(self,dice_roll:Tuple[int,int]) -> int:
        num_companies = sum([1 for prop in self.owner.properties if isinstance(prop,Company)])
        if num_companies == 1:
            return dice_roll[0]*4
        elif num_companies==2:
            return dice_roll[0]*10
        return 0
        
class Airport(Cell):
    def __init__(self, name: str, location: int, price:int) -> None:
        super().__init__(name, location)
        self.price = price
    
    def get_rent(self) -> int:
        num_airports = sum([1 for prop in self.owner.properties if isinstance(prop,Airport)])
        rent = 25 * 2**(num_airports-1)
        return rent
    

class Tax(Cell):
    def __init__(self, name: str, location: int) -> None:
        super().__init__(name, location)

    def calculate_tax(self,player:Player) -> None:
        if self.name == "Income Tax":
            player.balance -= (player.balance)*0.1
        elif self.name == "Luxury Tax":
            player.balance -= 75