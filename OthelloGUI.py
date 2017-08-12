import tkinter 
import Classothello
##HAVE MERCY ON ME PLEASE
#Michelle Woo 31203664 Project 5 


DEFAULT_FONT = ('Helvetica', 14)
TITLE_FONT=('Helvetica', 36)

class Menu:
    """Menu window pops up and asks user for inputs. If invalid rol or col input
is put in, error window pops up and warns user"""
    def __init__(self):
        self._dialog_window=tkinter.Tk()
        title_label=tkinter.Label(
            master=self._dialog_window,text='Welcome to Othello!',
            font= TITLE_FONT)
        title_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
##ROW
        row_label=tkinter.Label(master=self._dialog_window,
                                text='Rows:', font=DEFAULT_FONT)
        row_label.grid(row=1, column=0, padx=10, pady=10, sticky=tkinter.W)
        self._row_label_entry=tkinter.Entry(master=self._dialog_window,
                                            width=20, font=DEFAULT_FONT)
        self._row_label_entry.grid(row=1,column=1,padx=10,pady=1,
                                   sticky=tkinter.W+tkinter.E)
        self._row=''
##COL
        
        col_label=tkinter.Label(master=self._dialog_window,
                                text='Columns:', font=DEFAULT_FONT)
        col_label.grid(row=2, column=0, padx=10, pady=10, sticky=tkinter.W)
        self._col_label_entry=tkinter.Entry(master=self._dialog_window,
                                            width=20, font=DEFAULT_FONT)
        self._col_label_entry.grid(row=2,column=1,padx=10,pady=1,
                                   sticky=tkinter.W+tkinter.E)
        self._col=''
##TURN
    
        turn_label=tkinter.Label(master=self._dialog_window,
                                   text='Whose Turn?:', font=DEFAULT_FONT)
        turn_label.grid(row=3, column=0, padx=10, pady=10, sticky=tkinter.W)
        self.turn=tkinter.IntVar()
        self.turn.set(1)
        self._turn_black=tkinter.Radiobutton(master=self._dialog_window,
                                             text="Black", variable=self.turn,
                                             value=1).grid(row=4,column=0)
        self._turn_white=tkinter.Radiobutton(master=self._dialog_window,
                                             text="White", variable=self.turn,
                                             value=2).grid(row=4,column=1)
        self._turn=''
        
##ARRANGEMENT

        arrange_label=tkinter.Label(master=self._dialog_window,
                        text='Arrangement?:', font=DEFAULT_FONT)
        arrange_label.grid(row=5, column=0, padx=10, pady=10, sticky=tkinter.W)

        self.arrange=tkinter.IntVar()
        self.arrange.set(1)
        self._arrange_black=tkinter.Radiobutton(master=self._dialog_window,
                                             text="Black", variable=self.arrange,
                                             value=1).grid(row=6,column=0)
        self._arrange_white=tkinter.Radiobutton(master=self._dialog_window,
                                             text="White", variable=self.arrange,
                                             value=2).grid(row=6,column=1)
        self._arrange=''



##HOW TO WIN
        
        win_label=tkinter.Label(master=self._dialog_window,
                        text='How to Win?:', font=DEFAULT_FONT)
        win_label.grid(row=7, column=0, padx=10, pady=10, sticky=tkinter.W)
        self.winner=tkinter.StringVar()
        self.winner.set('<')
        self._less=tkinter.Radiobutton(master=self._dialog_window,
                                             text="Least", variable=self.winner,
                                             value='<').grid(row=8,column=0)
        self._greater=tkinter.Radiobutton(master=self._dialog_window,
                                             text="Greatest", variable=self.winner,
                                             value='>').grid(row=8,column=1)
        self._win=''
                       

### START
        button_frame = tkinter.Frame(master = self._dialog_window)

        button_frame.grid(
            row = 9, column = 0, columnspan = 2, padx = 10, pady = 10,
            sticky = tkinter.E + tkinter.S)
    
        start_button = tkinter.Button(
            master = button_frame, text = 'Start', font = DEFAULT_FONT,
            command= self.start_button)

        start_button.grid(row = 9, column = 0, padx = 10, pady = 10)
        cancel_button = tkinter.Button(
            master = button_frame, text = 'Quit', font = DEFAULT_FONT,
            command = self._on_cancel_button
            )

        cancel_button.grid(row = 9, column = 1, padx = 10, pady = 10)

        self._dialog_window.rowconfigure(0, weight = 1)
        self._dialog_window.rowconfigure(1, weight = 1)
        self._dialog_window.columnconfigure(0, weight = 1)
        self._start_clicked=False


    def error_message(self)->None:
        """ERROR window pops up if user puts in invalid row or col number"""
   
        self._error_window=tkinter.Tk()
        error_frame = tkinter.Frame(master = self._error_window)

        error_frame.grid(
            row = 3, column = 0, columnspan = 2, padx = 10, pady = 10,
            sticky = tkinter.E + tkinter.S)
        error_label=tkinter.Label(
        master=self._error_window,
        text='Invalid input. Row or column number must be an even number between 4 and 16',
        font= DEFAULT_FONT)
        error_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        error_ok_button = tkinter.Button(
        master = error_frame, text = 'Okay', font = DEFAULT_FONT,
        command = self.close_error_message)
        error_ok_button.grid(row = 0, column = 0, padx = 10, pady = 10)
        self._error_window.rowconfigure(0, weight = 1)
        self._error_window.rowconfigure(1, weight = 1)
        self._error_window.columnconfigure(0, weight = 1)

    def close_error_message(self)->None:
        """closes error message"""
        self._error_window.destroy()

        
    def get_row(self)->int:
        """return row"""
        
        return self._row
    
    def get_col(self)->int:
        """return column"""
        return self._col

    def get_turn(self)->int:
        """return turn( 1 or 2)"""
        return self._turn
    
    def get_arrange(self)->int:
        """return arrangement (1 or 2)"""
        return self._arrange
    def get_winner(self)->str:
        """return how the game will determine its winner"""
        return self._win

    def was_start_clicked(self)->bool:
        """ return true or false when start was clicked"""
        return self._start_clicked

    def start_button(self)->None:
        """takes in all the inputs and checks if its valid"""
        self._start_clicked=True
        try:
            row=self._row_label_entry.get()
            row=int(row)
        except:
            self.error_message()
        else:
            try:
                col=self._col_label_entry.get()
                col=int(col)
            except:
                self.error_message()
            else:
                self._turn=self.turn.get()
                self._arrange=self.arrange.get()
                self._win=self.winner.get()
                
                if row<4 or row>16 or (row%2)!=0:
                   self.error_message()
                    
                else:
                    self._row=self._row_label_entry.get()
                    if col<4 or col>16 or (col%2)!=0:
                        self.error_message()
                    else:
                        self._col=self._col_label_entry.get()
                
                        self._dialog_window.destroy()
                        pass
                        
        
    def _on_cancel_button(self)->None:
        """exits the menu window"""
        self._dialog_window.destroy()

class OthelloGame:
    def __init__(self):
        
        menu=Menu()
        menu._dialog_window.mainloop()
     
        if menu.was_start_clicked()==True:
            
            self._root_window=tkinter.Tk()
            self._canvas=tkinter.Canvas(master=self._root_window,
                                    width=500, height = 500,
                                    background='green')
            self._canvas.rowconfigure(0,weight=1)       

            self._canvas.grid(row=0, column=0, padx=30, pady=30,
                              stick=tkinter.N + tkinter.S+tkinter.W+tkinter.E)   
            self._root_window.rowconfigure(0,weight=1)
            self._root_window.columnconfigure(0, weight=1)
            full_label=tkinter.Label(master=self._root_window,
                                        text='FULL', font=DEFAULT_FONT)
            full_label.rowconfigure(1,weight=1)
            full_label.grid(row=10, column=0, sticky=tkinter.N)
   
                
            rows=int(menu.get_row())
            col=int(menu.get_col())
            turns=int(menu.get_turn())
            arrangement=int(menu.get_arrange())
            winning=(menu.get_winner())
            
            self.rows=int(menu.get_row())
            self.col=int(menu.get_col())
            self.turns=int(menu.get_turn())
            self.arrangement=int(menu.get_arrange())
            self.winning=(menu.get_winner()) 
        
            self._gamestate=Classothello.GameState(rows,col,turns,arrangement,winning)
            
            self._gamestate._new_game_board()     
            
            self._blackpieces=[]
            self._whitepieces=[]
              
            self._eachrow=500/self.rows
            self._eachcol=500/self.col
           
            self._arrayofboxes=[]
        
            self.width=int(self._canvas['width'])
            self.height=int(self._canvas['height'])
            
            self._canvas.bind('<Button-1>', self.on_canvas_clicked)
         
            self.count_discs()    
            self.print_turn()                  
            self.add_circles()
      
    def draw_board(self):
        """draw all the rows and columns"""
        
        for item in range(self.rows):
            self._arrayofboxes.append([])
            for element in range(self.col):
            
                self._canvas.create_rectangle(self._eachcol*(element),self._eachrow*(item), self._eachcol*(element+1),self._eachrow*(item+1),fill='green')
                self._arrayofboxes[-1].append([self._eachcol*(element),self._eachrow*(item), self._eachcol*(element+1),self._eachrow*(item+1)])

    def print_turn(self):
        """prints the turn below the canvas. B or W"""
        if self._gamestate.return_turn()==1:
            
            turn_label1=tkinter.Label(master=self._root_window,
                                        text='TURN: B', font=DEFAULT_FONT)
            turn_label1.grid(row=0, column=0, sticky=tkinter.N)
        if self._gamestate.return_turn()==2:
             turn_label2=tkinter.Label(master=self._root_window,
                                        text='TURN: W', font=DEFAULT_FONT)
             turn_label2.grid(row=0, column=0, sticky=tkinter.N)
        
    def add_circles(self):
        """this looks at the lists of lists in the game logic and checks
for any 1s or 2s. if theres a 1, it will call the print black circle function. if
there is a 2, it will call the print white circle function."""
        self._canvas.delete(tkinter.ALL)
        self.draw_board()
        self._blackpieces=[]
        self._whitepieces=[]
        for row in range(len(self._gamestate._board)):
            for col in range(len(self._gamestate._board[0])):
                if self._gamestate._board[row][col]==1:
                    self._blackpieces.append(self._arrayofboxes[row][col])
                if self._gamestate._board[row][col]==2:
                    self._whitepieces.append(self._arrayofboxes[row][col])
        self.print_black_circles(self._blackpieces)
        self.print_white_circles(self._whitepieces)
       

        
    def print_black_circles(self,circles:[(float,float,float,float)]):
        """prints the black circle given the coordinates"""

        for item in circles:
    
            self._canvas.create_oval(item,fill='black')
    def print_white_circles(self,circles:[(float,float,float,float)]):
        """prints the white circle given the coordinates"""
        for item in circles:
            self._canvas.create_oval(item,fill='white')

    def count_discs(self):
        """Count how many discs of each color there is"""
        blacks=0
        whites=0
        for item in self._gamestate._board:
            for element in item:
                if element==1:
                    blacks+=1
                if element==2:
                    whites+=1
        blacks=str(blacks)
        whites=str(whites)
        count_label=tkinter.Label(master=self._root_window,
                                        text=('B:',blacks, 'W:', whites), font=DEFAULT_FONT)
        
        count_label.grid(row=1, column=0, sticky=tkinter.N)

    def on_canvas_clicked(self, event:tkinter.Event):
        """if senses a click, takes the coordinate and checks if its a valid move.
if the next turn doesnt have any valid moves, the turn does not switch.
the game ends if there arent any valid moves for both players"""
        move=[]
        move.append([int(event.y/(500/(self.rows)))+1,int(event.x/(500/(self.col)))+1])
        for item in move:
            
            x=("{} {}".format(item[0],item[1]))
            self._gamestate.place_disc(x)
            self.add_circles()
            self.print_turn()   
            self.count_discs()
            if Classothello.full_board(self._gamestate)==False:
                
                self.winner_box()
            else:
                valid=[]
                for item in Classothello.check_valid(self._gamestate):
                    x=Classothello.valid_direction(self._gamestate,item[0]+1,item[1]+1)
                    if len(Classothello._check_opp_move(self._gamestate,x,item[0]+1,item[1]+1))!=0:
                        valid.append(item)
                if len(valid)==0:
                    self._gamestate._opposite_turn()
                    self.print_turn()
                    valid2=[]
                    for item in Classothello.check_valid(self._gamestate):
                        x=Classothello.valid_direction(self._gamestate,item[0]+1,item[1]+1)
                        if len(Classothello._check_opp_move(self._gamestate,x,item[0]+1,item[1]+1))!=0:
                            valid2.append(item)
                    if len(valid2)==0:
                        self.winner_box()

    def winner_box(self):
        """Pops up the winner"""
        self._winner_window=tkinter.Tk()
        winner_frame = tkinter.Frame(master = self._winner_window)

        winner_frame.grid(
            row = 3, column = 0, columnspan = 2, padx = 10, pady = 10,
            sticky = tkinter.E + tkinter.S)
        
        if Classothello.winner(self._gamestate)==1:
            winner= "B"
        elif Classothello.winner(self._gamestate)==2:
            winner="W"
        elif Classothello.winner(self._gamestate)==0:
            winner="NONE"  
        winner_label=tkinter.Label(
        master=self._winner_window,
        text="WINNER: {}".format(winner),
        font= DEFAULT_FONT)
        winner_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        winner_ok_button = tkinter.Button(
        master = winner_frame, text = 'Okay', font = DEFAULT_FONT,
        command = self.close_winner_message)
        winner_ok_button.grid(row = 0, column = 0, padx = 10, pady = 10)
        self._winner_window.rowconfigure(0, weight = 1)
        self._winner_window.rowconfigure(1, weight = 1)
        self._winner_window.columnconfigure(0, weight = 1)

   
    def close_winner_message(self)->None:
        """Closes winner box"""
        self._winner_window.destroy()

                
        
if __name__=='__main__':
    OthelloGame()
