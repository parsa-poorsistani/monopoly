from models.player import Player
from actions import ACTIONS
from board import Board
from models.cell import *

# Define the Monopoly game class
class Game:
    def __init__(self,player1:Player,player2:Player) -> None:
        # Initializing the game state
        self.current_player = player1  # Index of the current player in the players list
        self.other_player = player2
        self.game_over = False  # Boolean flag to indicate if the game is over
        self.board:Board = Board()


    def take_action(self, action: int) -> None:
        # Updating the game state based on the action taken by the current player

        curr_player = self.current_player
        curr_position = self.current_player.location
        curr_prop = self.board.locations[curr_position]
        # Do the appropriate changes for the action
        if action == 0:
            pass
        elif action == 1:
            curr_player.buy_property(curr_prop)
            if isinstance(curr_prop,City) or isinstance(curr_prop,Company) or isinstance(curr_prop,Airport):
                curr_prop.is_owned = True
        elif action == 2 and (isinstance(curr_prop,City) or isinstance(curr_prop,Company) or isinstance(curr_prop,Airport)) and curr_prop.is_owned:
            current_prop_owner:Player=None
            for prop in self.other_player.properties:
                if prop.name==curr_prop.name:
                    current_prop_owner = self.other_player
            if current_prop_owner!=None:
                if isinstance(curr_prop,City):
                    curr_player.pay(curr_prop.get_rent(),current_prop_owner)
                elif isinstance(curr_prop,Company):
                    curr_player.pay(curr_prop.get_rent(curr_player.last_roll,self.other_player.properties),current_prop_owner)
                elif isinstance(curr_prop,Airport):
                    curr_player.pay(curr_prop.get_rent(self.other_player.properties),current_prop_owner)
            # if isinstance(curr_prop,City):
            #     elif isinstance(curr_prop,Company):
            #     curr_player.pay(curr_prop.get_rent,current_prop_owner)
            # elif isinstance(curr_prop,Airport):
            #     curr_player.pay(curr_prop.get_rent,current_prop_owner)
            # self.other
            # new_players[curr_prop.owner].get_money(curr_prop.rent)
        elif action == 3:
            if isinstance(curr_prop,City):
                curr_prop.upgrade_city()
        elif action == 4:
            curr_player.location = 10
            curr_player.is_in_jail = True
            curr_player.turns_in_jail += 1
        elif action == 5:
            curr_player.turns_in_jail += 1
        elif action == 6:
            curr_player.balance-=50
            curr_player.is_in_jail = False
            curr_player.turns_in_jail = 0
        elif action == 7:
            curr_player.is_in_jail = False
            curr_player.turns_in_jail = 0       
        # return Game(new_board, new_players, self.current_player, self.game_over)
    
    def get_possible_actions(self) -> list:
        # Get the possible actions available to the current player
        curr_player = self.current_player
        curr_position = curr_player.location
        curr_prop = self.board.locations[curr_position]
        if curr_player.is_in_jail:
            if curr_player.rolled_double:
                return [7]
            if curr_player.turns_in_jail >= 3:
                return [6]
            return [5, 6]
        if isinstance(curr_prop,City) or isinstance(curr_prop,Airport) or isinstance(curr_prop,Company):
            if curr_prop in self.current_player.properties:
                if curr_player.balance > curr_prop.price:
                    return [3, 0]
                return [0]
            elif not curr_prop.is_owned:
                if curr_player.balance > curr_prop.price:
                    return [1, 0]
                return [0]
            elif curr_prop.is_owned:
                return [2]
        if isinstance(curr_prop,Jail):
                return [4]
        return [0]
    
    def move_player(self, dice_result:int) -> None:
        # Pass if the player is in jail
        if self.current_player.is_in_jail:
            return
        curr_player = self.current_player
        curr_position = curr_player.location
        # Update the player's position based on the dice roll result
        curr_position = (curr_position + dice_result) % 40
        curr_player.move(dice_result)

    def is_terminal(self) -> bool:
        # Check if the game has reached a terminal state
        if self.current_player.balance <= 0:
            return True
        return False
    
    def evaluate_utility(self) -> int:
        # Evaluate the utility of the current game state for the current player
        return self.current_player.net_worth()

    def switch_player(self):
        # Switch to the next player's turn
        self.current_player,self.other_player = self.other_player,self.current_player
