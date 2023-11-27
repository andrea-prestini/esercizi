from gtn import guess_the_number
from rps import rock_paper_scissors
from wordle import Wordle
from connect_four import ConnectFour
from tictactoe import TicTacToe

while True:
    txt = """Mini Games! ! !
    - Guess The Number         (1)
    - Sasso, Carta, Forbici    (2)
    - Wordle                   (3)
    - ConnectFour Forza 4      (4)
    - Tic Tac Toe TRIS         (5)
Select a game (press a number or 'q' to quit): """
    value = input(txt)
    if value == '1':
        guess_the_number(100)
    elif value == '2':
        rock_paper_scissors()
    elif value == '3':
        game = Wordle()
        game.play()
    elif value == '4':
        game = ConnectFour()
        game.play()
    elif value == '5':
        game = TicTacToe()
        game.play()
    elif value == 'q':
        break





