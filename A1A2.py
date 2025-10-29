import random

def show_board(hit, miss, comp):
    global score

    print("       Battleship Game", "\n")
    print("       0  1  2  3  4")
    print(f"score: {score}")

    place = 0
    huruf = ['A', 'B', 'C', 'D', 'E']
    for x in range(5):
        row = ""
        for y in range(5):
            ch = " _ "
            if place in miss:
                ch = " X "
            elif place in hit:
                ch = " o "
            elif place in comp:
                ch = " O "
            row += ch
            place += 1
        print(huruf[x], " ", row)

