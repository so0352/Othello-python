from utils.Board import Board
def main():
    print("オセロ対戦へようこそ!")
    return

if __name__ == "__main__":
    bd = Board()
    print(bd.show())
    result = bd.check_flip(2, 3, False)
    print(result)
    print(bd.evaluation_matrix)