
class Game_logic():
    
    def __init__(self):
        pass
    def print_scoreboard(score_board):
        return "print score board"
     # Function to check if any player has won
    def check_win(self,player_pos, cur_player):
    
        # All possible winning combinations
        soln = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    
        # Loop to check if any winning combination is satisfied
        for x in soln:   
            if all(y in player_pos[cur_player] for y in x):
    
                # Return True if any winning combination satisfies
                return True
        # Return False if no combination is satisfied       
        return False       
    def single_game():
        pass    