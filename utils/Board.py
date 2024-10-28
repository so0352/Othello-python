import numpy as np

# オセロの盤面情報を保持するクラス
class Board():
    def __init__(self) -> None:
        self.board = np.zeros((8, 8), dtype=np.int8)
        self.board[3, 3] = self.board[4, 4] = 1 # 先手
        self.board[3, 4] = self.board[4, 3] = 2 # 後手
        self.passed = False
        self.finished = False

        self.evaluation_matrix = np.array([
            [100, -20, 10, 5, 5, 10, -20, 100],
            [-20, -50, -2, -2, -2, -2, -50, -20],
            [10, -2, 5, 1, 1, 5, -2, 10],
            [5, -2, 1, 0, 0, 1, -2, 5],
            [5, -2, 1, 0, 0, 1, -2, 5],
            [10, -2, 5, 1, 1, 5, -2, 10],
            [-20, -50, -2, -2, -2, -2, -50, -20],
            [100, -20, 10, 5, 5, 10, -20, 100]
        ])
        
        return
    # おくことができる駒の座標リスト
    def show_available_coordinates(self, first_move: bool) -> list:
        ans_list = []
        for i in range(8):
            for j in range(8):
                if self.check_flip(i, j, first_move=first_move) != []:
                    ans_list.append((i, j))
        return ans_list
    
    # 盤面に駒を置く + 駒をひっくり返す
    def add_piece(self, y: int, x: int, first_move: bool) -> bool:
            if self.board[y, x] != 0:
                return False
            # 先手の時
            if first_move:
                if self.check_flip(y, x, first_move=first_move) == []:
                    return False
                # 駒をひっくり返す
                self.flip_pieces(y, x, first_move=first_move, check_flip_list=self.check_flip(y, x, first_move=first_move))
                self.board[y, x] = 1
            # 後手の時
            else:
                if self.check_flip(y, x, first_move=first_move) == []:
                    return False
                # 駒をひっくり返す
                self.flip_pieces(y, x, first_move=first_move, check_flip_list=self.check_flip(y, x, first_move=first_move))
                self.board[y, x] = 2
            return True
    
    # 駒をひっくり返す
    def flip_pieces(self, y: int, x: int, first_move: bool, check_flip_list: list) -> None:
        for (dy, dx), pieces_num in check_flip_list:
            cur_x, cur_y = x, y
            for _ in range(pieces_num):
                cur_x += dx
                cur_y += dy
                if first_move:
                    self.board[cur_y, cur_x] = 1
                else:
                    self.board[cur_y, cur_x] = 2
                    
    # 盤面の状態を表示する
    def show(self) -> None:
        print("何もない:. 先手の駒:o 後手の駒:x")
        print('  a b c d e f g h')
        for i in range(8):
            print(i + 1, end=' ')
            for j in range(8):
                if self.board[i, j] == 0:
                    print('.', end=' ')
                elif self.board[i, j] == 1:
                    print('o', end=' ')
                elif self.board[i, j] == 2:
                    print('x', end=' ')
            print()
        return
    
    # それぞれの方向に対して何枚ひっくり返せるかを調べる
    def check_flip(self, y: int, x: int, first_move: bool) -> list:
        if self.board[y, x] != 0:
            return []
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        ans_list = []
        for dy, dx in directions:
            piece_num = 0
            cur_x, cur_y = x, y  # x, y の初期値を保存
            start_to_end = False
            while True:
                cur_x += dx
                cur_y += dy
                # 盤面外に出たら終了
                if 0 <= cur_x < 8 and 0 <= cur_y < 8:
                    # 空白マスに出会ったら終了
                    if self.board[cur_y, cur_x] == 0:
                        break
                    # 先手の場合
                    if first_move:
                        # 先手の駒に出会ったらひっくり返せる枚数を記録
                        if self.board[cur_y, cur_x] == 1:
                            start_to_end = True
                            break
                        else:
                            piece_num += 1
                    # 後手の場合
                    else:
                        # 後手の駒に出会ったらひっくり返せる枚数を記録
                        if self.board[cur_y, cur_x] == 2:
                            start_to_end = True
                            break
                        else:
                            piece_num += 1
                else:
                    break
            if start_to_end and piece_num > 0:
                ans_list.append(((dy, dx), piece_num))
        return ans_list

