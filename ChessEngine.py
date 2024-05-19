import random
from math import inf

class ChessEngine () :
    def changePieces2 (self,newpos,currpos,board) :
    
        board[newpos[0]][newpos[1]] = board[currpos[0]][currpos[1]]
        board[currpos[0]][currpos[1]] = "-"
    def isEmpty(self,curr_poss,new_poss,pType,board) :
        curr_x, curr_y = curr_poss
        new_x, new_y = new_poss    
        if abs(curr_x - new_x) == abs(curr_y - new_y):
        # Determinar la dirección de movimiento
            dir_x = 1 if new_x > curr_x else -1
            dir_y = 1 if new_y > curr_y else -1

            # Verificar si hay fichas en el camino diagonal
            for i in range(1, abs(curr_x - new_x)):
                check_x = curr_x + i * dir_x
                check_y = curr_y + i * dir_y
                #print(f'chech in {(check_x,check_y)}')
                if board[check_x][check_y] != '-':
                    return False
        if curr_x == new_x : 
            for i in range(min(curr_y,new_y),max(curr_y,new_y)) : 
                if ( board[curr_x][i] !='-' and i!=curr_y )  : 
                    if i == new_y and board[curr_x][i][-1]!=pType :
                        continue
                    return False
        elif curr_y == new_y : 
            for i in range(min(curr_x,new_x),max(curr_x,new_x)) : 
               # print(board[i][curr_y])
                if ( board[i][curr_y]!='-' and i !=curr_x  ) :
                    #print(f"new x {new_x}")
                    if i == new_x and board[i][curr_y][-1]!=pType :
                        continue
                    return False                    
                    #row_pos_valids.append(False)
        if board[new_x][new_y]!='-' and board[new_x][new_y][-1]!=pType :
           return True
        
        return True   
    def PnMove(self, curr_pos, new_pos,board):
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
           # print("Movimiento no válido para el peón negro.")
            return False    
        
    def PbMove(self, curr_pos, new_pos,board):
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
        
    def Tmove(self,curr_pos, new_pos,pType,board) : 
        curr_x, curr_y = curr_pos
        new_x, new_y = new_pos  
        if curr_x == new_x and new_y!=curr_y :
            if self.isEmpty(curr_pos,new_pos,pType,board) :
                return True
        elif curr_y == new_y and  new_x!=curr_x :
            if self.isEmpty(curr_pos,new_pos,pType,board) :
                return True
        else :
            return False
        pass

    def Amove (self ,curr_pos,new_pos,pType,board) :
        curr_x, curr_y = curr_pos
        new_x, new_y = new_pos   
        if (abs(curr_x-new_x)== abs(curr_y-new_y)) and self.isEmpty(curr_pos,new_pos,pType,board) :
            return True
        return False 
    
    def Cmove(self ,curr_pos,new_pos,board) : 
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
    
    def RNmove(self,curr_pos,new_pos,pType,board) :
        curr_x, curr_y = curr_pos
        new_x, new_y = new_pos
        if (self.isEmpty(curr_pos,new_pos,pType,board)) :   
            if curr_x == new_x and new_y!=curr_y  :
                return True
            elif curr_y == new_y and  new_x!=curr_x :
                return True 
            elif (abs(curr_x-new_x)== abs(curr_y-new_y)) :
                return True
        else :
            return False
    def Rmove(self,curr_pos,new_pos,board) : 
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
        
        ################
    def verifiedPiece(self,piece,new_pos,curr_pos,board = []) : 
        pType = piece[-1]
        piece = piece[:-1]
        
        if piece =='P' : 
            if pType =='b' : 
                if self.PbMove(curr_pos,new_pos,board) :
                    return True
            elif pType == 'n' : 
                if self.PnMove(curr_pos,new_pos,board) :
                    return True
                
        elif piece == 'RN' :
            if self.RNmove(curr_pos,new_pos,pType,board):
                return True 
            pass
        elif piece ==  'R' :
            if self.Rmove(curr_pos,new_pos,board) :
                return True
        elif piece == 'A' :
            if self.Amove(curr_pos,new_pos,pType,board) :
                return True
            pass
        elif piece =='T' : 
            if self.Tmove(curr_pos,new_pos,pType,board) : 
                return True 
            pass 
        elif piece == 'C' : 
            if self.Cmove(curr_pos,new_pos ,board) :
                return True
        return False
    def generate_legal_moves_for_piece(self, board, position):
        """
        Genera todos los movimientos legales posibles para una pieza en una posición dada.
        :param board: Tablero actual del juego.
        :param position: Posición (fila, columna) de la pieza en el tablero.
        :return: Lista de posiciones (filas, columnas) a las que la pieza puede moverse legalmente.
        """
        piece = board[position[0]][position[1]]
       # print(f"piece in generate {piece}")
        if piece == '-':
            return []  # No hay movimientos legales para una casilla vacía

        # Obtener el tipo y color de la pieza
        piece_type = piece[:-1]
        player_color = piece[-1]

        legal_moves = []
       # print(len(board))
       # print(len(board[1]))
        # Generar movimientos legales según el tipo de pieza
        for i in range(0,len(board)):
            for j in range(0,len(board[i])):
                new_pos = (i, j)
                #print(f"new pos un fuc {new_pos}")
                if self.verifiedPiece(piece, new_pos, position,board= board) and board[new_pos[0]][new_pos[1]][-1] != player_color:
                    legal_moves.append(new_pos)

        return legal_moves    
        
    def generate_legal_moves(self, board,player_color):
        legal_moves = []
        for i in range(len(board)):
            for j in range(len(board[i])):
                position = (i, j)
                piece = board[position[0]][position[1]]
                if piece != '-' and piece[-1] == player_color:
                    moves_for_piece = self.generate_legal_moves_for_piece(board, position)
                    legal_moves.extend([(position, move) for move in moves_for_piece])
        print(f'legal moves for {player_color}')
        print(legal_moves)
        return legal_moves
     
    def evaluate_board(self, board):
        material_values = {
            'Pb': 1, 'Pn': 1,  # Peones
            'Cb': 3, 'Cn': 3,  # Caballos
            'Ab': 3, 'An': 3,  # Alfiles
            'Tb': 5, 'Tn': 5,  # Torres
            'RNb': 9, 'RNn': 9,  # Reinas
            'Rb': 90, 'Rn': 90  # Reyes
        }

        white_material = 0
        black_material = 0

        for row in board:
            for piece in row:
                if piece != '-':
                    if piece[-1] == 'b':
                        white_material += material_values[piece]
                    else:
                        black_material += material_values[piece]
    
        return white_material ,black_material
    def evaluate(self,board,color) : 
        scores = self.evaluate_board(board)
        if color == 'b' :
            return scores[0] - scores[1]
        else :
            return scores[1] - scores[0]
    def minmax(self, board, depth, maximizing_player, maximizing_color):
        if depth == 0:
            return None, self.evaluate(board, maximizing_color)
        
        if maximizing_player:
            # Maximizing for white pieces
            moves = self.generate_legal_moves(board, 'b')
            max_eval = -inf
            best_move = random.choice(moves)
            for move in moves:
                # Create a copy of the board to apply the move
                board_copy = [row[:] for row in board]
                self.changePieces2(move[1], move[0], board_copy)
                current_eval = self.minmax(board_copy, depth - 1, False, maximizing_color)[1]
                if current_eval > max_eval:
                    max_eval = current_eval
                    best_move = move
            return best_move, max_eval
        else:
            # Minimizing for black pieces
            moves = self.generate_legal_moves(board, 'n')#GENERA MOVIMIENTOS LEGALES FICHAS NEGRAS
            min_eval = inf 
            best_move = random.choice(moves)
            for move in moves:
                # Create a copy of the board to apply the move
                board_copy = [row[:] for row in board]
                self.changePieces2(move[1], move[0], board_copy)
                current_eval = self.minmax(board_copy, depth - 1, True, maximizing_color)[1]
                if current_eval < min_eval:
                    min_eval = current_eval
                    best_move = move
            return best_move, min_eval
  

    def __init__(self) -> None:
        pass

    alt =  """    def minmax(self,board,deph,maximizing_player,maximizing_color) :
        if deph==0 : 
            return None,self.evaluate(board,maximizing_color)
        moves = self.generate_legal_moves(board,'b') + self.generate_legal_moves(board,'n')
      #  print(moves)
        best_move = random.choice(moves)
        if maximizing_player : 
            max_eval = -inf 
            for move in moves : 
                old_board = board
                self.changePieces2(move[1],move[0],board)
                current_eval = self.minmax(board,deph-1,False,maximizing_color)[1]
                board = old_board
                if current_eval>max_eval :
                    max_eval = current_eval
                    best_move = move
            return best_move , max_eval
        else : 
            min_eval = abs(inf) 
            for move in moves : 
                old_board = board
                self.changePieces2(move[1],move[0],board)     
                current_eval = self.minmax(board,deph-1,True,maximizing_color)[1]    
                board = old_board
                if current_eval < min_eval : 
                    min_eval = current_eval 
                    best_move = move
            return best_move , min_eval"""