from models.cell import Cell

class Player:
    
    def __init__(self,name:str) -> None:
        self.name = name
        self.balance = 1500
        self.location = 0
        self.is_bankrupted = False
        self.properties:list = []
        
    def move(self,num_spaces):
        self.location+=num_spaces
        if self.location >=40:
            self.location -=40
            self.balance+=200
        #return self.location
    
    def buy_property(self,property:Cell) -> None:
        self.properties.append(property)
        
    def remove_property(self,property:Cell) -> None:
        self.properties.remove(property)
        
    def pay(self,amount:int,receiver:'Player') -> None:
        self.balance-=amount
        receiver.balance+=amount
        
    def bankrupted(self):
        self.is_bankrupted = True
    
    
    