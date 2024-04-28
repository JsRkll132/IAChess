import ChessItems
import random

class ChessStates() : 
    def isvalidPositition(self,randompieces = []) :
        t_index = [i for i, x in enumerate(randompieces) if x == "Tb"]
        r_index = [i for i, x in enumerate(randompieces) if x == "Rb"]
        a_index = [i for i, x in enumerate(randompieces) if x == "Ab"]
        if t_index[0]<r_index[0] and r_index[0] < t_index[1] and (a_index[1]-a_index[0])%2!=0  :
            return True
        return False

    def generatePositions(self) :
        whites = ChessItems.Chessitems().getWhiteItems()[0:8]
        positions  = []
        for i in range(0,8) : 
            
            item  = random.choice(whites)
            positions.append(item)
            whites.remove(item)
        return positions
    def getPositions(self) :
         
        while True :
            positions = self.generatePositions()
            if self.isvalidPositition(positions) :
                return positions
            
    def getBoard(self) : 
        return self.tablero
    
    def isKilled(self,board = [],new_pos = [],curr_pos = []) : 
        if board[new_pos[0]][new_pos[1]][-1] =='n' and board[curr_pos[0]][curr_pos[1]][-1] =='b'  or board[new_pos[0]][new_pos[1]][-1] =='b' and board[curr_pos[0]][curr_pos[1]][-1] =='n' : 
            return True
        return False
    def toKill(self, board = [],new_pos = [],curr_pos = []) : 
        pass

    def PbMove(self,board, curr_pos, new_pos):
        curr_x, curr_y = curr_pos
        new_x, new_y = new_pos

        # Verificar si la posición actual contiene un peón blanco
        if board[curr_x][curr_y] != 'Pb':
            print("La posición actual no contiene un peón blanco.")
            return False

        # Verificar si la nueva posición está dentro del tablero
        if not (0 <= new_x < 8 and 0 <= new_y < 8):
            print("La nueva posición está fuera del tablero.")
            return False

        # Verificar si el movimiento es válido
        if new_y == curr_y and board[new_x][new_y] == '-' and curr_x-new_x == 1:
            return True  # Movimiento hacia adelante una casilla
        elif (curr_x -new_x==2 or curr_x-new_x == 1 )  and curr_x == 6 and board[new_x][new_y] == '-' and board[curr_x - 1][curr_y] == '-':
            return True  # Movimiento hacia adelante dos casillas en el primer movimiento
        elif (new_x, new_y) in [(curr_x - 1, curr_y - 1), (curr_x - 1, curr_y + 1)] and board[new_x][new_y][-1] == 'n':
            return True  # Captura en diagonal
        else:
            print("Movimiento no válido para el peón blanco.")
            return False
    def Tmove(self,board, curr_pos, new_pos) : 
        curr_x, curr_y = curr_pos
        new_x, new_y = new_pos  
        if curr_x == new_x and new_y!=curr_y :
            return True
        elif curr_y == new_y and  new_x!=curr_x :
            return True 
        else :
            return False
        pass
    def __init__(self) -> None:
        whitesPieces = self.getPositions()
        blackPieces = [p.replace('b','n') for p in whitesPieces] 
        self.tablero = [
            blackPieces,
            ["Pn","Pn","Pn","Pn","Pn","Pn","Pn","Pn"],
            ["-","-","-","-","-","-","-","-","-","-"],
            ["-","-","-","-","-","-","-","-","-","-"],
            ["-","-","-","-","-","-","-","-","-","-"],
            ["-","-","-","-","-","-","-","-","-","-"],
            ["Pb","Pb","Pb","Pb","Pb","Pb","Pb","Pb"],
            whitesPieces
        ]
        
        