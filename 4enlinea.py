import unittest

class OcupadoException(Exception):
    pass

class Game:

    def __init__(self):

        self.board = [[0 for _ in range(8)] for _ in range(8)]
        self.winner=True
        self.current_turn = 1

    def set(self, col):

        self.row = self.calculte_position(col)

        if self.board [col]!=0:
            raise OcupadoException('La columna está llena')
        self.change_turn()

    def change_turn(self):
        
        if self.current_turn == 1:
            self.current_turn = 2
        else:
            self.current_turn = 1
    
    def calculte_position(self, col):
        
        for row in reversed(self.board):
            if self.board[row][col] == 0:
                self.board[row][col]=self.current_turn
        #self.row=row
        return self.row

class TestGame(unittest.TestCase):
    def test_create_board(self):
        game = Game()
        self.assertEqual(len(game.board), 8)
        self.assertEqual(len(game.board[0]), 8)
        
    def test_change_turn(self):
        game=Game()
        game.change_turn()
        self.assertEqual(game.current_turn, 2)
    
    def est_calculate_position(self):
        game=Game()
        game.calculte_position(1)
        self.assertEqual(game.board[0][1],1)


if __name__ == '__main__':
    unittest.main()