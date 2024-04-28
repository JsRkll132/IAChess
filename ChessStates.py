import ChessItems
import random

class ChessStates() : 
    def isEmpty(self,board,curr_poss,new_poss,pType) :
        curr_x, curr_y = curr_poss
        new_x, new_y = new_poss    
        if board[new_x][new_y]!='-' and board[new_x][new_y][-1]!=pType :
            return True
        
        if curr_x == new_x : 
            for i in range(min(curr_y,new_y),max(curr_y,new_y)) : 
                if ( board[curr_x][i] !='-' and i!=curr_y )  : 
                    return False
        elif curr_y == new_y : 
            for i in range(min(curr_x,new_x),max(curr_x,new_x)) : 
                print(board[i][curr_y])
                if ( board[i][curr_y]!='-' and i !=curr_x  ) :
                    return False

                    
        """elif (abs(curr_x-new_x)== abs(curr_y-new_y)) :
            for i ,k in range(max(curr_x,new_x)-min(curr_x,new_x)) :
                if board[max(curr_x,new_x)-i][max(curr_y,new_y)-i] != '-':
                    return False"""
        return True    
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
        if new_pos ==None or curr_pos ==None :
            return False
        try : 
            if (board[new_pos[0]][new_pos[1]][-1] =='n' and board[curr_pos[0]][curr_pos[1]][-1] =='b' ) or ( board[new_pos[0]][new_pos[1]][-1] =='b' and board[curr_pos[0]][curr_pos[1]][-1] =='n') : 
                return True
        except : 
            return False
    
    def toKill(self, board = [],new_pos = [],curr_pos = []) : 
        pass
    def PnMove(self,board, curr_pos, new_pos):
        curr_x, curr_y = curr_pos
        new_x, new_y = new_pos
            # Verificar si el movimiento es válido
        if new_y == curr_y and board[new_x][new_y] == '-' and new_x-curr_x == 1:
            return True  # Movimiento hacia adelante una casilla
        elif new_y == curr_y and (new_x-curr_x ==2 or new_x- curr_x == 1 )  and curr_x == 1 and board[new_x][new_y] == '-' and board[curr_x + 1][curr_y] == '-':
            return True  # Movimiento hacia adelante dos casillas en el primer movimiento
        elif (new_x, new_y) in [(curr_x + 1, curr_y + 1), (curr_x + 1, curr_y - 1)] and board[new_x][new_y][-1] == 'b':
            return True  # Captura en diagonal
        else:
            print("Movimiento no válido para el peón negro.")
            return False    
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
        elif new_y == curr_y and (curr_x -new_x==2 or curr_x-new_x == 1 )  and curr_x == 6 and board[new_x][new_y] == '-' and board[curr_x - 1][curr_y] == '-':
            return True  # Movimiento hacia adelante dos casillas en el primer movimiento
        elif (new_x, new_y) in [(curr_x - 1, curr_y - 1), (curr_x - 1, curr_y + 1)] and board[new_x][new_y][-1] == 'n':
            return True  # Captura en diagonal
        else:
            print("Movimiento no válido para el peón blanco.")
            return False
        
    def Tmove(self,board, curr_pos, new_pos,pType) : 
        curr_x, curr_y = curr_pos
        new_x, new_y = new_pos  
        if curr_x == new_x and new_y!=curr_y :
            if self.isEmpty(board,curr_pos,new_pos,pType) :
                return True
        elif curr_y == new_y and  new_x!=curr_x :
            if self.isEmpty(board,curr_pos,new_pos,pType) :
                return True
        else :
            return False
        pass

    def Amove (self , board,curr_pos,new_pos) :
        curr_x, curr_y = curr_pos
        new_x, new_y = new_pos   
        if (abs(curr_x-new_x)== abs(curr_y-new_y)) :
            if (self.isEmpty( board,curr_pos,new_pos)) :
                return True
        return False 
    
    def Cmove(self , board,curr_pos,new_pos) : 
        curr_x, curr_y = curr_pos
        new_x, new_y = new_pos       
        if curr_x + 2 == new_x and curr_y -1 ==new_y  :
            return True
        elif curr_x + 2 == new_x and curr_y +1 == new_y :
            return True
        elif curr_x - 2 == new_x and curr_y +1 == new_y  :
            return True
        elif curr_x - 2 == new_x and curr_y -1 == new_y  :
            return True  
        elif curr_x + 1 == new_x and curr_y -2 ==new_y  :
            return True
        elif curr_x + 1 == new_x and curr_y +2 == new_y :
            return True
        elif curr_x - 1 == new_x and curr_y +2 == new_y  :
            return True
        elif curr_x - 1 == new_x and curr_y -2 == new_y  :
            return True      
        else :
            return False
    
    def RNmove(self,board,curr_pos,new_pos,pType) :
        curr_x, curr_y = curr_pos
        new_x, new_y = new_pos
        if (self.isEmpty(board,curr_pos,new_pos,pType)) :   
            if curr_x == new_x and new_y!=curr_y  :
                return True
            elif curr_y == new_y and  new_x!=curr_x :
                return True 
            elif (abs(curr_x-new_x)== abs(curr_y-new_y)) :
                return True
        else :
            return False
    def Rmove(self,board,curr_pos,new_pos) : 
        curr_x, curr_y = curr_pos
        new_x, new_y = new_pos       
        if curr_x == new_x and abs(new_y-curr_y) == 1 :
            return True
        elif curr_y == new_y and  abs(new_x-curr_x) == 1 :
            return True 
        elif (abs(curr_x-new_x)== 1 and  abs(curr_y-new_y) == 1) :
            return True
        else :
            return False      

                    
         
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
        
        