import sys
import os
# プロジェクトのルートディレクトリを取得
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# プロジェクトのルートディレクトリをsys.pathに追加
sys.path.append(project_root)

from utils.Board import Board

def max_frip(board: Board, available_coordinates_list: list, first_move: bool):
    max_frip = 0
    max_x = -1
    max_y = -1
    max_frip = -1
    for (y, x) in available_coordinates_list:
        flip_list = board.check_flip(y, x, first_move) # ひっくり返すことができる方向と個数
        for (dy, dx), num in flip_list:
            if num > max_frip:
                max_frip = num
                max_x = x
                max_y = y
    return (max_y, max_x), max_frip