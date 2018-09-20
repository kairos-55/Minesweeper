from random import randrange

class Board:
    height = 0
    width = 0
    mines = 0
    list_pos_mines = [] # Lista de posiciones donde se van a encontrar las minas
    list_pos_flags = [] # Lista de posiciones donde se van a encontrar las banderas
    board = [] # Lista de objetos tipo celda
    str_board = [] # Lista de strings
    game_over = False
    game_wined = False
    
    # Método que genera la posición pseudo-aleatoria de cada mina
    def generate_pos(self):
        random_list = []
        i = 0
        while i < self.mines:            
            mine_pos = [randrange(self.height), randrange(self.width)]
            if not (mine_pos in random_list):                 
                random_list.append(mine_pos)
                i = i + 1

        return random_list

    # Método que inicializa la lista de celdas y la lista de strings
    def generate_board(self):
        board = [[Cell() for i in range(self.width)] for j in range(self.height)]
        self.str_board = [['.' for i in range(self.width)] for j in range(self.height)]        

        for mine_location in self.list_pos_mines:
            (mine_row, mine_col) = mine_location
            board[mine_row][mine_col].set_mine(True)
            board[mine_row][mine_col].set_number(-1)

            # Rango donde se buscaran las minas adyacentes a cada celda
            row_range = range(mine_row - 1, mine_row + 2)
            col_range = range(mine_col - 1, mine_col + 2)

            # Ciclo que permite encontrar el número de minas adyacentes a cada celda
            for i in row_range:
                for j in col_range:
                    if(0 <= i < self.height and 0 <= j < self.width and not board[i][j].get_mine()):                       
                        board[i][j].set_number(board[i][j].get_number()+1)                    

        return board   

    # Método que permite descubrir expansivamente las celdas que no tiene mina    
    def flood_fill(self, x, y):
        for xoff in [-1, 0, 1]:
            i = x + xoff
            if i < 0 or i >= self.height:
                continue
            for yoff in [-1, 0, 1]:
                j = y + yoff
                if j < 0 or j >= self.width:
                    continue
                if not self.board[i][j].get_mine() and not self.board[i][j].get_selected() and not self.board[x][y].get_mine():
                    self.board[i][j].set_selected(True)
                    self.board[i][j].set_unselected(False)
                    if self.board[i][j].get_number() == 0:
                        self.flood_fill(i, j)

    # Método que actualiza la lista de celdas y la de strings
    def updateBoard(self):
        for i in range(self.height):
            for j in range(self.width):                
                cell = self.board[i][j] 
                
                if self.game_over:
                    if cell.get_mine():
                        cell.set_unselected(False)
                        cell.set_selected(False)
                        cell.set_flag(False)  
                        self.str_board[i][j] = '*'
                       
                if cell.get_flag():
                    self.str_board[i][j] = 'P'
                                    
                if cell.get_selected():
                    if cell.get_number() == 0:
                        self.str_board[i][j] = '-'                        
                    else: 
                        self.str_board[i][j] = str(cell.get_number())
        
    # Método que imprime en consola el tablero del juego
    def drawBoard(self):
        show = ""
        for i in range(self.height):
            for j in range(self.width):
                show += self.str_board[i][j] + " "
            show += '\n'

        if self.game_wined:
            show += '¡You Win!'
        if self.game_over:
            show += '¡You Lost!'

        print(show) 


    # Método que permite al usuario seleccionar la celda y la accion en cada turno
    # Además de evaluar el fin del juego 
    def start_game(self):
        while not self.game_over and not self.game_wined:
            pos_x, pos_y, action = map(str, input().split())
            row = int(pos_x)
            col = int(pos_y)
            cell = self.board[row][col]

            if action == 'U':

                self.flood_fill(row, col)

                cell.set_unselected(False)
                cell.set_selected(True)
                cell.set_flag(False)                  

                if [row,col] in self.list_pos_flags:
                    self.list_pos_flags.remove([row,col])

            elif action == 'M' and not cell.get_selected():
                cell.set_flag(True)  
                cell.set_unselected(False)
                cell.set_selected(False)
                self.list_pos_flags.append([row,col])               

            if cell.get_mine() and not cell.get_flag():
                self.game_over = True  
            elif len(self.list_pos_flags) == len(self.list_pos_mines):
                if self.list_pos_flags == self.list_pos_mines:
                    self.game_wined = True

            self.updateBoard() 
            self.drawBoard()   

    # Constructor de la clase Board
    def __init__(self, height, width, mines):
        self.height = height
        self.width = width
        self.mines = mines
        self.list_pos_mines = self.generate_pos()
        self.board = self.generate_board()
    
class Cell:

    # Atributos de la clase
    unselected = True
    disable = False
    mine = False
    flag = False
    number = 0
    selected = False   

    # Métodos set
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

    # Métodos get
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

    

    


    
