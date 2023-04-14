from models.player import Player
from models.cell import City,Company,Jail,AirPort,Vacation

class Board:
    def __init__(self) -> None:
        self.locations = [None]*40
    
    def show_board(self) -> None:
        pass