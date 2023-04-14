from models.player import Player
from models.cell import City,Company,Jail,Airport,Vacation,EmptyCell,Tax
from enums.group_enums import GroupEnum

class Board:
    def __init__(self) -> None:
        self.locations = [
            EmptyCell("GO",0),
            City("Salvador",1,60,GroupEnum.BRAZIL),
            EmptyCell("Empty",2),
            City("Rio",3,60,GroupEnum.BRAZIL),
            Tax("Income Tax",4),
            Airport("TLV Airport",5,200),
            City("Tel Aviv",6,100,GroupEnum.ISRAEL),
            EmptyCell("Empty",7),
            City("Haifa",8,100,GroupEnum.ISRAEL),
            City("Jerusalem",9,120,GroupEnum.ISRAEL),
            Jail("Jail",10),
            City("Venice",11,140,GroupEnum.ITALY),
            Company("Electric Company",12,150),
            City("Milan",13,140,GroupEnum.ITALY),
            City("Rome",14,160,GroupEnum.ITALY),
            Airport("MUC",15,200),
            City("Frankfurt",16,180,GroupEnum.GERMANY),
            EmptyCell("Empty",17),
            City("Munich",18,180,GroupEnum.GERMANY),
            City("Berlin",19,200,GroupEnum.GERMANY),
            Vacation("Vacation",20),
            City("Shenzhen",21,220,GroupEnum.CHINA),
            EmptyCell("Empty",22),
            City("Beijing",23,220,GroupEnum.CHINA),
            City("Shanghai",24,240,GroupEnum.CHINA),
            Airport("CDG Airport",25,200),
            City("Lyon",26,260,GroupEnum.FRANCE),
            City("Toulouse",27,260,GroupEnum.FRANCE),
            Company("Water Company",28,150),
            City("Paris",29,280,GroupEnum.FRANCE),
            Jail("Go to Jail",30),
            City("Liverpool",31,300,GroupEnum.ENGLAND),
            City("Manchester",32,300,GroupEnum.ENGLAND),
            EmptyCell("Empty",33),
            City("London",34,320,GroupEnum.ENGLAND),
            Airport("JFK Airport",35,200),
            EmptyCell("Empty",36),
            City("San Francisco",37,350,GroupEnum.USA),
            Tax("Luxury Tax",38),
            City("New York",39,400,GroupEnum.USA)
        ]
    
    def print_cell_info(self,index:int) -> None:
        cell = self.locations[index]
        if isinstance(cell,City):
            city:City = cell
            print(f"name: {city.name}, group: {city.group}, price: {city.price}",end="")
        elif isinstance(cell,Company) or isinstance(cell,Airport):
            print(f"name: {cell.name}, price: {cell.price}",end="")
        else:
            print(f"name: {cell.name}",end="")
            
        
    def show_board(self) -> None:
        print(" ___________________________________________________________ ")
        print("|                                                           |")
        print("|                 Monopoly Board Game                        |")
        print("|___________________________________________________________|")
        for i in range(11):
            print("| "+self.print_cell_info(i)+" |",end="")
        for i in range(11,20):
            print(self.print_cell_info(i+20),end="")
            print("                                                                                          ",end="")
            print(self.print_cell_info(i))
            print("___")
        for i in range(31,20,-1):
            print("| "+self.print_cell_info(i)+" |",end="")
            

class Dialog:
    @staticmethod
    def print_():
        pass
        
        
        
         