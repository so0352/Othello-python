import numpy as np

# オセロの盤面情報を保持するクラス
class Board():
    def __init__(self) -> None:
        self.board = np.zeros((8, 8), dtype=np.int8)
        self.board[3, 3] = self.board[4, 4] = 1
        self.board[3, 4] = self.board[4, 3] = 2
        self.turn = 1
        self.passed = False
        self.finished = False