from utils.Board import Board
def main():
    print("オセロ対戦へようこそ!")
    return

if __name__ == "__main__":
    bd = Board()
    print(bd.show())
    first_move = False  
    if bd.add_piece(3, 2, first_move):
       pass
    else:
        print("駒を置くことができません。")
    
    print(bd.show())
