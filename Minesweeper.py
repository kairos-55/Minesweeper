from random import randrange

"""class Table:

    height = 0
    width = 0
    mines = 0

    def __init(self, height, width, mines):
        self.height = height
        self.width = width
        self.mines = mines

def mine_sweeper(bombs, num_rows, num_cols):
    field = [[0 for i in range(num_cols)] for j in range(num_rows)]

    for bomb_location in bombs:
        (bomb_row, bomb_col) = bomb_location
        field[bomb_row][bomb_col] = -1

        row_range = range(bomb_row - 1, bomb_row + 2)
        col_range = range(bomb_col - 1, bomb_col + 2)

        for i in row_range:
            for j in col_range:
                if(0 <= i < num_rows and 0 <= j < num_cols and field[i][j] != -1):
                    field[i][j] += 1

    return field

print(mine_sweeper([[0,0],[1,2]], 3, 4))"""

class Board:
    height = 0
    width = 0
    mines = 0
    list_pos_mines = []
    board = []
    game_over = False
    
    def generate_pos(self):
        random_list = []
        i = 0
        while i < self.mines:            
            mine_pos = [randrange(self.height), randrange(self.width)]
            if not (mine_pos in random_list):                 
                random_list.append(mine_pos)
                i = i + 1

        print('Bombs:')       
        print(random_list)

        return random_list

    def generate_board(self):
        board = [[Cell() for i in range(self.width)] for j in range(self.height)]

        for mine_location in self.list_pos_mines:
            (mine_row, mine_col) = mine_location
            board[mine_row][mine_col].set_mine(True)
            board[mine_row][mine_col].set_number(-1)

            row_range = range(mine_row - 1, mine_row + 2)
            col_range = range(mine_col - 1, mine_col + 2)

            for i in row_range:
                for j in col_range:
                    if(0 <= i < self.height and 0 <= j < self.width and not board[i][j].get_mine()):                       
                        board[i][j].set_number(board[i][j].get_number()+1)                    

        return board   

    def drawBoard(self):
        str_board = ""
        for i in range(self.height):
            for j in range(self.width):                
                cell = self.board[i][j] 

                if self.game_over:
                    if cell.get_mine():
                        cell.set_unselected(False)
                        cell.set_selected(False)
                        cell.set_flag(False)  
                        str_board += '* '
                       
                if cell.get_flag():
                    str_board += 'P '
                    
                if cell.get_unselected():
                    str_board += '. '
                    
                if cell.get_selected():
                    if cell.get_number() == 0:
                        str_board += '- '
                        
                    else: 
                        str_board += str(cell.get_number())+" "
                
                                        
            str_board+="\n"

        print(str_board)  

    def start_game(self):
        while not self.game_over:
            pos_x, pos_y, action = map(str, input().split())
            row = int(pos_x)
            col = int(pos_y)

            if action == 'U':
                self.board[row][col].set_unselected(False)
                self.board[row][col].set_selected(True)
                self.board[row][col].set_flag(False)                 
            elif action == 'M':
                self.board[row][col].set_flag(True)  
                self.board[row][col].set_unselected(False)
                self.board[row][col].set_selected(False)               

            if self.board[row][col].get_mine() and not self.board[row][col].get_flag():
                self.game_over = True  

            self.drawBoard()    

    def __init__(self, height, width, mines):
        self.height = height
        self.width = width
        self.mines = mines
        self.list_pos_mines = self.generate_pos()
        self.board = self.generate_board()
    
class Cell:
    unselected = True
    disable = False
    mine = False
    flag = False
    number = 0
    selected = False   

    def set_unselected(self, unselected):
        self.unselected = unselected

    def set_disable(self, disable):
        self.disable = disable

    def set_mine(self, mine):
        self.mine = mine

    def set_flag(self, flag):
        self.flag = flag

    def set_number(self, number):
        self.number = number

    def set_selected(self, selected):
        self.selected = selected

    def get_unselected(self):
        return self.unselected

    def get_disable(self):
        return self.disable

    def get_mine(self):
        return self.mine

    def get_flag(self):
        return self.flag

    def get_number(self):
        return self.number

    def get_selected(self):
        return self.selected


def main():
    height, width, mines = map(int, input().split())        
    boardMain = Board(height, width, mines)
    boardMain.drawBoard() 
    boardMain.start_game()

if __name__ == "__main__":
    main()

    
