from utils.Board import Board
def main():
    print("オセロ対戦へようこそ!")
    return

if __name__ == "__main__":
    bd = Board()
    print(bd.show())
    first_move = True
    if bd.add_piece(2, 3, first_move):
       pass
    else:
        print("駒を置くことができません。")
    
    print(bd.show())
    print(bd.show_available_coordinates(first_move))