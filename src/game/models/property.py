from models.player import Player
class Property:
    
    def __init__(self,name:str,price:int,rent:int,group:str) -> None:
        self.name = name
        self.price = price
        self.remt = rent
        self.group = group
        self.owner:Player = None
        self.num_houses = 0
        self.num_hotel = 0
        self.is_mortgaged = False
        
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
    
    def mortgage(self) -> None:
        if self.owner is None:
            return False
        if self.num_houses == 0 and self.num_hotels == 0:
            self.owner.money += self.price * 0.5
            self.owner = None
            self.is_mortgaged = True
            return True
        return False
    
    def unmortgage(self) -> bool:
        if self.is_mortgaged:
            mortgage_value = int(self.price * 0.5 * self.mortgage_rate)
            if self.owner.money >= mortgage_value:
                self.owner.money -= mortgage_value
                self.is_mortgaged = False
                return True
        return False
            