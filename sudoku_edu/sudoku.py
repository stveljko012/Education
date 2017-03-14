# Sudoku [http://en.wikipedia.org/wiki/Sudoku]
# is a logic puzzle where a game
# is defined by a partially filled
# 9 x 9 square of digits where each square
# contains one of the digits 1,2,3,4,5,6,7,8,9.
# For this question we will generalize
# and simplify the game.

class Sudoku():

    def __init__(self, table):
        self.tab = table

    #TODO: Napraviti funkciju koja ispituje da li je matrica kvadratna (n x n)
    def is_square(self):
        pass

    #TODO: Napraviti funkciju koja ispituje da li su elementi matrice brojevi
    def is_valid_elements(self):
        pass

    #TODO: Napraviti funkciju koja ispituje da li su elemnti matrice brojevi od 0 - n
    def is_n_symbols(self):
        pass

    #TODO: Napraviti funckiju koja ispituje da li je matrica popunjena prema SUDOKU pravilu
    def check_sudoku(self):
        passg