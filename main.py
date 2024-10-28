from utils.Board import Board
from algorithm.max_frip import max_frip
import sys


## 座標を受け取って盤面に適用する関数
def input_coordinate(board: Board, first_move: bool):
    while True:
        print("置きたい場所の座標をスペース区切りで入力してください.入力は半角.")
        print("値は0~7の整数で入力")
        try:
            y, x = map(int, input("縦 横 \n").split())
            # 指定した範囲内の座標なら
            if 0 <= y < 8 and 0 <= x < 8:
                add_return = board.add_piece(y, x, first_move)
                if add_return == False:
                    print("エラー: その場所には駒を置けません。")
                    continue
                else:
                    print("駒を置きました。")
                    board.show()
                    start_num, next_num = board.count_pieces()
                    print(f"先手: {start_num} 後手: {next_num}")
                    break
            else:
                print("エラー: 0~7の整数で入力してください。")
                continue
            
        except ValueError:
            print("エラー: スペースで区切った2つの数字を入力してください。")
        except KeyboardInterrupt:
            print("\nプログラムを終了します。")
            sys.exit()


def main():
    print("オセロゲームを開始します．")
    first_move = True if int(input("先手なら0,後手なら1を入力してください. \n")) == 0 else False
    board = Board(first_move=first_move)
    board.show()
    start_num, next_num = board.count_pieces()
    print(f"先手: {start_num} 後手: {next_num}")

    # 人間が先手なら
    if first_move:
        while True:
            # 人間側
            if board.show_available_coordinates(first_move) == []:
                print("あなたはパスします.")
                first_move = False # AIの手番に移る
            else:   
                input_coordinate(board=board, first_move=first_move)
                first_move = False # AIの手番に移る
            # AI側
            (max_y, max_x), max_frip_num = max_frip(board, board.show_available_coordinates(first_move), first_move) # 最適手を取得
            if max_frip_num == 0:
                print("AIはパスします.")
                first_move = True # 人間の手番に移る
            else:
                print(f"AIの手: {max_y} {max_x}", f"ひっくり返す数: {max_frip_num}")
                if max_frip_num == -1:
                    print("AIはパスします.")
                    first_move = True # 人間の手番に移る
                else:
                    add_return = board.add_piece(max_y, max_x, first_move)

                    if add_return == False:
                        print("エラー: AIの手が正しくありません.")
                        sys.exit()
                    else:
                        print("AIの手を置きました.")
                        board.show()
                        start_num, next_num = board.count_pieces()
                        print(f"先手: {start_num} 後手: {next_num}")
                        first_move = True # 人間の手番に移る

            # ゲーム終了判定
            if board.finished:
                board.show()
                start_num, next_num = board.count_pieces()
                print(f"先手: {start_num} 後手: {next_num}")
                print("ゲーム終了")
                break
    
    # AIが先手なら   
    elif first_move == False:
        while True:
            # AI側
            (max_y, max_x), max_frip_num = max_frip(board, board.show_available_coordinates(first_move), first_move) # 最適手を取得
            if max_frip_num == 0:
                print("AIはパスします.")
                first_move = True # 人間の手番に移る
            else:
                print(f"AIの手: {max_y} {max_x}", f"ひっくり返す数: {max_frip_num}")
                if max_frip_num == -1:
                    print("AIはパスします.")
                    first_move = True
                else:
                    add_return = board.add_piece(max_y, max_x, first_move)
                    if add_return == False:
                        print("エラー: AIの手が正しくありません.")
                        sys.exit()
                    else:
                        print("AIの手を置きました.")
                        board.show()
                        start_num, next_num = board.count_pieces()
                        print(f"先手: {start_num} 後手: {next_num}")
                        first_move = True # 人間の手番に移る
            
            # 人間側
            if board.show_available_coordinates(first_move) == []:
                print("あなたはパスします.")
                first_move = False # AIの手番に移る
            else:   
                input_coordinate(board=board, first_move=first_move)
                first_move = False # AIの手番に移る
            
            # ゲーム終了判定
            if board.finished:
                board.show()
                start_num, next_num = board.count_pieces()
                print(f"先手: {start_num} 後手: {next_num}")
                print("ゲーム終了")
                break

    sys.exit()
if __name__ == "__main__":
    main()