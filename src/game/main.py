from game import Game
from agent.agent import expectiminimax
from actions import ACTIONS

def play(state: Game) -> None:
        num_of_rounds = 0
        # Main game loop to play the game
        while not state.game_over:
            # Get current player from state
            curr_player = state.players[state.current_player]
            print(f"{curr_player.name} is on {curr_player.position} and has {curr_player.money}$,")
            
            if curr_player.is_in_jail:
                print(f"turns in jail {curr_player.turns_in_jail}")
            
            total_dice = curr_player.roll_dice()
            # Moving the player based on the dice outcome
            state.move_player(total_dice)
            print(f"{curr_player.name} lands on {curr_player.position}!", end=" ")

            # Determining the best possible action
            _, best_action = expectiminimax(state.current_player, state)
            
            # Taking the best action
            state = state.take_action(best_action)
            print(f"{curr_player.name} {ACTIONS[best_action]}.")
            print(state.players[state.current_player])
            print(f"Current net worth: {state.evaluate_utility()}")

            if state.is_terminal():
                state.game_over = True
            else:
                state.switch_player()
            num_of_rounds += 1
            print(f"Round: {num_of_rounds}")
            print("====================================================")
        print(f"{state.players[0 if state.current_player else 1].name} Won!")   

# Driver code to start the Monopoly game
if __name__ == "__main__":
    game = Game()
    p1:str = "Player"
    p2 = "Agent"
    game.initialize_players(p1,p2)
    play(game)