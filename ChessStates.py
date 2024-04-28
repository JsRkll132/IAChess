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
        
        