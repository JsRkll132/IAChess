import ChessEngine
import ChessStates


sample_board = [
            ["Rn","RNn","Cn","An","Tn","Cn","An","Tn","Pn"],
            ["Pn","Pn","Pn","Pn","Pn","Pn","Pn","Pn"],
            ["-","-","-","-","-","-","-","-"],
            ["-","-","-","-","-","-","-","-"],
            ["-","-","-","-","-","-","-","-"],
            ["-","-","-","-","-","-","-","-"],
            ["Pb","Pb","Pb","Pb","Pb","Pb","Pb","Pb"],
            ["Rb","RNb","Cb","Ab","Tb","Cb","Ab","Tb","Pb"]
            ]
board = [
            ["-","-","-","-","Rn","-","An","Tn","Pn"],
            ["Pn","Pn","Pn","Pn","RNb","Pn","Pn","Pn"],
            ["-","-","-","-","-","-","-","-"],
            ["-","-","-","-","-","-","-","-"],
            ["-","-","-","-","-","-","-","-"],
            ["-","-","-","-","-","-","-","-"],
            ["Pb","Pb","Pb","Pb","Pb","Pb","Pb","Pb"],
            ["Rb","-","Cb","Ab","Tb","Cb","Ab","Tb","Pb"]
            ]
ce = ChessEngine.ChessEngine()
new_pos=ce.minmax(board=board,depth=6,maximizing_player=True,maximizing_color='b')
print(new_pos)
print(ce.is_checkmate(board,'n'))
[print(f'{i}\n') for i in board]