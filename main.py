import pygame
import sys
import ChessStates
import ChessItems
# Definir algunos colores
BLANCO = (255, 255, 255)
NEGRO = (0, 99, 147)

# Tamaño de la pantalla y tamaño del tablero
ANCHO = 720
ALTO = 720
TAM_CUADRO = ANCHO // 8
IMAGES = {}
TURNO = True
# Inicializar Pygame
pygame.init()
CurrentChessGame = ChessStates.ChessStates()
board =  CurrentChessGame.getBoard()
# Crear la pantalla
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Tablero de Ajedrez")

def loadImages() : 
    blackPieces = sorted(ChessItems.Chessitems().getBlackItems())
    whitePieces = sorted(ChessItems.Chessitems().getWhiteItems())
    for i in blackPieces : 
        IMAGES[i] = pygame.transform.scale(pygame.image.load('ChessGame\GameView\Images\\blackpieces\\'+i+'.png'),(TAM_CUADRO, TAM_CUADRO))
    for i in whitePieces : 
        IMAGES[i] = pygame.transform.scale(pygame.image.load('ChessGame\GameView\Images\\whitepieces\\'+i+'.png'),(TAM_CUADRO, TAM_CUADRO))    
"""
def move_piece(x, y,param_y = TAM_CUADRO,param_x=TAM_CUADRO):
    fila = y // param_y
    columna = x // param_x

    print(f'Moviendo pieza en la fila {fila} y columna {columna}')
    return fila,columna
def changePieces (newpos,currpos) :
    
    board[newpos[0]][newpos[1]] = board[currpos[0]][currpos[1]]
    board[currpos[0]][currpos[1]] = "-"
    [ print(f'{k}\n') for k in board ]"""

"""
def verifiedPiece(piece,board,new_pos,curr_pos) : 
    pType = piece[-1]
    piece = piece[:-1]
    print (TURNO)
    print(pType)
    if TURNO==True and pType !='b' :
        print("El turno actual es de las fichas blancas...")
        return False
    elif TURNO == False and pType !='n' :
        print("El turno actual es de las fichas negras...")
        return False
    
    if piece =='P' : 
        if pType =='b' : 
            if CurrentChessGame.PbMove(board,curr_pos,new_pos) :
                return True
        elif pType == 'n' : 
            if CurrentChessGame.PnMove(board,curr_pos,new_pos) :
                return True
            
    elif piece == 'RN' :
        if CurrentChessGame.RNmove(board,curr_pos,new_pos,pType):
            return True 
        pass
    elif piece ==  'R' :
         if CurrentChessGame.Rmove(board,curr_pos,new_pos) :
             return True
    elif piece == 'A' :
        if CurrentChessGame.Amove(board,curr_pos,new_pos) :
            return True
        pass
    elif piece =='T' : 
        if CurrentChessGame.Tmove(board,curr_pos,new_pos,pType) : 
            return True 
        pass 
    elif piece == 'C' : 
        if CurrentChessGame.Cmove(board,curr_pos,new_pos ) :
            return True
    return False"""



def draw_board( board) :
    for fila in range(8):
        for columna in range(8):
            x = columna * TAM_CUADRO
            y = fila * TAM_CUADRO
            # Dibujar el tablero
            color = BLANCO if (fila + columna) % 2 == 0 else NEGRO
            pygame.draw.rect(pantalla, color, (x, y, TAM_CUADRO, TAM_CUADRO))
            # Dibujar las piezas
            piece = board[fila][columna]
            if piece != '-' :
                try : 
                    pantalla.blit(IMAGES[piece], (x, y))
                except : 
                    pass

def gameLoop(piece = "",curr_pos = None,new_pos = None) : 
    pass



def main():
    global TURNO
    loadImages()
    curr_pos=None
    new_pos= None
    piece = ""
    while True:
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN : 
                x, y = pygame.mouse.get_pos()
                position = CurrentChessGame.move_piece(x,y,TAM_CUADRO,TAM_CUADRO)  # Llamar a la función para mover la pieza
                print("posicion")
                print(position)
                print((x//TAM_CUADRO,y//TAM_CUADRO))
                print(CurrentChessGame.getBoard())
                legal_moves = CurrentChessGame.generate_legal_moves(CurrentChessGame.getBoard(),(y//TAM_CUADRO,x//TAM_CUADRO))
                print("LEGAL MOVES")
                print(legal_moves)
                if CurrentChessGame.getBoard()[position[0]][position[1]] == '-' or CurrentChessGame.isKilled(position,curr_pos) : 
                    new_pos = position
                elif   CurrentChessGame.getBoard()[position[0]][position[1]] != '-': 
                    piece = CurrentChessGame.getBoard()[position[0]][position[1]]
                    curr_pos = position
                print(piece)
                print(curr_pos)
                print(new_pos)
                print(f'turno actual {CurrentChessGame.getTurno()}')
                if new_pos!= None and curr_pos!=None and CurrentChessGame.verifiedPiece(piece,new_pos,curr_pos) :
                    CurrentChessGame.changePieces(new_pos,curr_pos)
                    curr_pos = None 
                    new_pos =None
                    CurrentChessGame.changeTurno()
                elif new_pos!= None and curr_pos!=None and not CurrentChessGame.verifiedPiece(piece,new_pos,curr_pos) :
                    curr_pos = None 
                    new_pos =None

                
                
        # Dibujar el tablero
        draw_board(CurrentChessGame.getBoard())

        # Actualizar la pantalla
        pygame.display.flip()

if __name__ == "__main__":
    main()
