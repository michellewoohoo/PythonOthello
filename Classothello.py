#GAME LOGIC
#Michelle Woo 31203664 Project 5

import collections

class NonexistentRowError(Exception):
    '''raised whenever a user puts in an invalid row number'''
    pass
class NonexistentColumnError(Exception):
    '''raised whenever a user puts in an invalid column number'''
    pass
class InvalidMove(Exception):
    '''raised whenever a user doesn't put in 2 numbers as a move'''
    pass


class GameState():

    def __init__(self,  rows: int, columns: int, whoseturn: str, position: str, winning:str):
        self._rows=rows
        self._columns=columns
        self._whoseturn=0
        self._winning=winning
        if(whoseturn==2):
            self._whoseturn=2
        else:
            self._whoseturn=1
        self._position=position
        self._board = GameState._new_game_board(self)

    def return_turn(self):
        return self._whoseturn

    def _new_game_board(self):
        
        '''Creates a new game board.'''
        board = []
        for r in range(self._rows):
            board.append([])
            for c in range(self._columns):
                board[-1].append(0)
        if self._position==1:
            board[int(((self._rows)/2)-1)][int(((self._columns)/2)-1)]=1
            board[int((self._rows/2))][int((self._columns)/2)]=1
            board[int(((self._rows)/2)-1)][int(((self._columns)/2))]=2
            board[int((self._rows)/2)][int(((self._columns)/2)-1)]=2

        if self._position==2:
            board[int(((self._rows)/2)-1)][int(((self._columns)/2)-1)]=2
            board[int((self._rows/2))][int((self._columns)/2)]=2
            board[int(((self._rows)/2)-1)][int(((self._columns)/2))]=1
            board[int((self._rows)/2)][int(((self._columns)/2)-1)]=1


        self._board=board
            
    def place_disc(self,themove:list):
        """Takes the input and splits it into row and column. Checks to see if it is a valid move,
and if it is, flips all the discs to the same color as the turn. After that, it switches the turn."""

        move=themove
        coordinates=move.split()
        if len(coordinates)<2 or len(coordinates)>2:
            raise InvalidMove("Must be 2 numbers")
        row=int(coordinates[0])
        col=int(coordinates[1])
        coordinates=[row,col]
        if self._whoseturn==1:
            x=valid_direction(self,row,col)
            if len(_check_opp_move(self,x, row, col))!=0:
                
                row2=int(coordinates[0])-1
                
                column2=int(coordinates[1])-1
                
                (self._board[row2][column2])=1
                self._board=flip(self,(_check_opp_move(self,x, row, col)),row,col)
                
                self._opposite_turn()
         
        elif self._whoseturn==2:
            x=valid_direction(self,row,col)
            if len(_check_opp_move(self,x, row, col))!=0:
                row2=int(coordinates[0])-1
                column2=int(coordinates[1])-1
                
                (self._board[row2][column2])=2
                self._board=flip(self,(_check_opp_move(self,x, row, col)),row,col)
                self._opposite_turn()
           
        
    
    def _opposite_turn(self):
        '''Given the player whose turn it is now, returns the opposite player'''
        if self._whoseturn == 1:
            self._whoseturn=2
        else:
            self._whoseturn=1
  


def opposite_turn_for_direction(game_state:GameState):
    '''Given the player whose turn it is now, returns the opposite player. Specifically for valid_direction function'''
    if game_state._whoseturn == 1:
        return 2
    else:
        return 1
def valid_direction(game_state:GameState, row: int, col: int)->list:
    """Returns the valid direction"""
    
    directions=[[0,1],[0,-1], [1,0], [-1,0], [-1,-1], [-1,1], [1,-1], [1,1]]
    whichdirections=[[0,1],[0,-1], [1,0], [-1,0], [-1,-1], [-1,1], [1,-1], [1,1]]

    validmoves=[]
    moves=[]
    if game_state._board[row-1][col-1]==0:
        for item in directions:
            validmoves.append([row+item[0],col+item[1]])
        i=0         
        while True:
            if len(validmoves) == 0 or i>= len(validmoves):
                break
            if validmoves[i][0] > game_state._rows or validmoves[i][1] > game_state._columns or validmoves[i][0] <= 0 or validmoves[i][1] <= 0:       
                validmoves.remove(validmoves[i])
                whichdirections.remove(whichdirections[i])
            else:
                if i >= len(validmoves):
                    break
                else:
                    i += 1

        for item in range(len((validmoves))):
            if game_state._board[validmoves[item][0]-1][validmoves[item][1]-1] == opposite_turn_for_direction(game_state):
                moves.append(whichdirections[item])
    else:
        pass

    return(moves)

def _check_opp_move(game_state:GameState, validmoves:list, row:int, col:int)->list:
    """Uses the valid direction from valid_move and keeps adding that "valid direction"
to the move until it hits a disc that is the same as the turn, and appends to the "valid" list.
If the move hits NONE or the game border, it breaks out of the loop. In the end, if the
valid list is greater than 0, the move is valid"""

    valid=[]    
    for item in validmoves:
        changingrow=item[0]
        changingcol=item[1]
        therows=(row+changingrow)-1
        thecol=(col+changingcol)-1
        while True:
            try:
                if game_state._board[therows][thecol]==game_state._whoseturn:
                    valid.append(item)
                    break
            except:
                break
            if game_state._board[therows][thecol]==0:
                break
            therows+=changingrow
            thecol+=changingcol
            if therows<0 or thecol<0:
                break

    return valid

def flip(game_state:GameState, newlist:list, row:int, col:int)->list:
    '''Flips all the discs between the two same colored discs into that color'''

    gamestate=game_state._board   
    for item in newlist:
        changingrow=item[0]
        changingcol=item[1]
        therows=(row+changingrow)-1
        thecol=(col+changingcol)-1
        while True:            
            if gamestate[therows][thecol]==game_state._whoseturn:                
                break                
            else:                
                gamestate[therows][thecol]=game_state._whoseturn            
            therows+=changingrow
            thecol+=changingcol
            if therows<0 or thecol<0:
                break
  
    return gamestate

def check_valid(game_state: GameState)->list:
    '''checks to see for empty slots'''
    valid=[]
    for col in range(len(game_state._board)):
        for row in range(len(game_state._board[0])):
            if game_state._board[row][col]==0:
                valid.append([row,col])
    return valid



def winner(game_state: GameState)->int:
    '''adds up how many black discs and white discs and returns the winner'''
    blacks=0
    whites=0
    for item in game_state._board:
        for element in item:
            if element==1:
                blacks+=1
            if element==2:
                whites+=1
    if game_state._winning==">":
        if blacks>whites:
            return(1)
        elif blacks<whites:
            return(2)
        
        elif blacks==whites:
            return(0)
    if game_state._winning=="<":
        if blacks>whites:
            return(2)
        elif blacks<whites:
            return(1)
        
        elif blacks==whites:
            return(0)

def full_board(game_state: GameState):
    '''checks to see if the board has no empty spaces. Returns true if there are empty spaces'''
    openspaces=[]
    for row in range(len(game_state._board)):
        for col in range(len(game_state._board[0])):
            if game_state._board[row][col]==0:
                openspaces.append([row,col])
    if len(openspaces)!=0:
        return True
    else:
        return False
            
                
                
            
            
                
            
            
            
        
        
        
        
        
    
                
  
                
 
                

