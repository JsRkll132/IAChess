import pygame
import sys
import ChessStates
import ChessItems
import ChessEngine
import time
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
#board =  CurrentChessGame.getBoard()
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
    best = None
    while True:
        #board_aux = CurrentChessGame.getBoard()
        #next_data = ChessEngine.ChessEngine().minmax(board_aux,1,True,'b')
        #print(next_data)
        if not CurrentChessGame.getTurno() :
                board_aux = [row[:] for row in CurrentChessGame.getBoard()]
                best = ChessEngine.ChessEngine().minmax(board_aux,2,False,'b')
                print(f'This is the best move : {best[0]}')
        if (CurrentChessGame.getTurno() ==False and best != None) : 
            CurrentChessGame.changePieces(best[0][1],best[0][0])
            CurrentChessGame.changeTurno()
            time.sleep(0.5)
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
                legal_moves = CurrentChessGame.generate_legal_moves_for_piece(CurrentChessGame.getBoard(),(y//TAM_CUADRO,x//TAM_CUADRO))
                print("--------------------")
               # print(f"legal moves whites : {CurrentChessGame.count_legal_moves(CurrentChessGame.getBoard(),'b')}")
              #  print(f"legal moves whites : {CurrentChessGame.count_legal_moves(CurrentChessGame.getBoard(),'n')}")
                lg_whites = CurrentChessGame.generate_legal_moves(CurrentChessGame.getBoard(),'b')
                print(f'lfwhites : {lg_whites}')
                CurrentChessGame.generate_legal_moves(CurrentChessGame.getBoard(),'n')
               # board_aux = []


                
                #print("nex data :")
               # print(next_data)
                print(CurrentChessGame.evaluate_board(CurrentChessGame.getBoard()))
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
                if new_pos!= None and curr_pos!=None and CurrentChessGame.verifiedPiece(piece,new_pos,curr_pos,board =  CurrentChessGame.getBoard()) :
                    if CurrentChessGame.getTurno() :
                        time.sleep(0.2)
                    CurrentChessGame.changePieces(new_pos,curr_pos)
                    curr_pos = None 
                    new_pos =None
                    CurrentChessGame.changeTurno()
                elif new_pos!= None and curr_pos!=None and not CurrentChessGame.verifiedPiece(piece,new_pos,curr_pos,board =  CurrentChessGame.getBoard()) :
                    curr_pos = None 
                    new_pos =None
                
                
                
        # Dibujar el tablero
        draw_board(CurrentChessGame.getBoard())

        # Actualizar la pantalla
        pygame.display.flip()

if __name__ == "__main__":
    main()
