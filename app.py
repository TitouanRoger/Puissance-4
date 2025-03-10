import pyxel

pyxel.init(63,55,title="Puissance 4")
pyxel.load("res.pyxres")

def update():
    global c, c1, c2, c3, c4, c5, c6, c7
    pyxel.cls(0)
    pyxel.blt(4,1,0,0,0,54,5)
    pyxel.blt(3,29,0,0,17,5,11)
    pyxel.blt(55,29,0,6,17,5,11)
    pyxel.blt(3,41,0,6,7,5,5)
    pyxel.blt(55,41,0,12,7,5,5)
    pyxel.line(10,12,10,48,1)
    pyxel.line(16,12,16,48,1)
    pyxel.line(22,12,22,48,1)
    pyxel.line(28,12,28,48,1)
    pyxel.line(34,12,34,48,1)
    pyxel.line(40,12,40,48,1)
    pyxel.line(46,12,46,48,1)
    pyxel.line(52,12,52,48,1)
    pyxel.line(10,12,52,12,1)
    pyxel.line(10,18,52,18,1)
    pyxel.line(10,24,52,24,1)
    pyxel.line(10,30,52,30,1)
    pyxel.line(10,36,52,36,1)
    pyxel.line(10,42,52,42,1)
    pyxel.line(10,48,52,48,1)
    pyxel.blt(c,8,0,0,13,5,3)
    pyxel.blt(11,13,0,c1[5],7,5,5)
    pyxel.blt(11,19,0,c1[4],7,5,5)
    pyxel.blt(11,25,0,c1[3],7,5,5)
    pyxel.blt(11,31,0,c1[2],7,5,5)
    pyxel.blt(11,37,0,c1[1],7,5,5)
    pyxel.blt(11,43,0,c1[0],7,5,5)
    pyxel.blt(17,13,0,c2[5],7,5,5)
    pyxel.blt(17,19,0,c2[4],7,5,5)
    pyxel.blt(17,25,0,c2[3],7,5,5)
    pyxel.blt(17,31,0,c2[2],7,5,5)
    pyxel.blt(17,37,0,c2[1],7,5,5)
    pyxel.blt(17,43,0,c2[0],7,5,5)
    pyxel.blt(23,13,0,c3[5],7,5,5)
    pyxel.blt(23,19,0,c3[4],7,5,5)
    pyxel.blt(23,25,0,c3[3],7,5,5)
    pyxel.blt(23,31,0,c3[2],7,5,5)
    pyxel.blt(23,37,0,c3[1],7,5,5)
    pyxel.blt(23,43,0,c3[0],7,5,5)
    pyxel.blt(29,13,0,c4[5],7,5,5)
    pyxel.blt(29,19,0,c4[4],7,5,5)
    pyxel.blt(29,25,0,c4[3],7,5,5)
    pyxel.blt(29,31,0,c4[2],7,5,5)
    pyxel.blt(29,37,0,c4[1],7,5,5)
    pyxel.blt(29,43,0,c4[0],7,5,5)
    pyxel.blt(35,13,0,c5[5],7,5,5)
    pyxel.blt(35,19,0,c5[4],7,5,5)
    pyxel.blt(35,25,0,c5[3],7,5,5)
    pyxel.blt(35,31,0,c5[2],7,5,5)
    pyxel.blt(35,37,0,c5[1],7,5,5)
    pyxel.blt(35,43,0,c5[0],7,5,5)
    pyxel.blt(41,13,0,c6[5],7,5,5)
    pyxel.blt(41,19,0,c6[4],7,5,5)
    pyxel.blt(41,25,0,c6[3],7,5,5)
    pyxel.blt(41,31,0,c6[2],7,5,5)
    pyxel.blt(41,37,0,c6[1],7,5,5)
    pyxel.blt(41,43,0,c6[0],7,5,5)
    pyxel.blt(47,13,0,c7[5],7,5,5)
    pyxel.blt(47,19,0,c7[4],7,5,5)
    pyxel.blt(47,25,0,c7[3],7,5,5)
    pyxel.blt(47,31,0,c7[2],7,5,5)
    pyxel.blt(47,37,0,c7[1],7,5,5)
    pyxel.blt(47,43,0,c7[0],7,5,5)

def draw():
    global j, c, c1, c2, c3, c4, c5, c6, c7
    if pyxel.btnp(pyxel.KEY_SPACE):
        j = 1
        c = 29
        c1 = [0,0,0,0,0,0]
        c2 = [0,0,0,0,0,0]
        c3 = [0,0,0,0,0,0]
        c4 = [0,0,0,0,0,0]
        c5 = [0,0,0,0,0,0]
        c6 = [0,0,0,0,0,0]
        c7 = [0,0,0,0,0,0]

    if pyxel.btnp(pyxel.KEY_LEFT) or pyxel.btnp(pyxel.KEY_Q):
        if c > 11:
            c -= 6
    if pyxel.btnp(pyxel.KEY_RIGHT) or pyxel.btnp(pyxel.KEY_D):
        if c < 46:
            c += 6
    
    def update_column(column, player_value):
        for i in range(6):
            if column[i] == 0:
                column[i] = player_value
                return True
        return False

    def handle_player_turn(column, player_value, next_player):
        if update_column(column, player_value):
            global j
            j = next_player
        else:
            return

    columns = {11: c1, 17: c2, 23: c3, 29: c4, 35: c5, 41: c6, 47: c7}

    if j == 1:
        pyxel.blt(3, 47, 0, 5, 13, 5, 3)
        if pyxel.btnp(pyxel.KEY_DOWN) or pyxel.btnp(pyxel.KEY_S):
            if c in columns:
                handle_player_turn(columns[c], 6, 2)

    elif j == 2:
        pyxel.blt(55, 47, 0, 5, 13, 5, 3)
        if pyxel.btnp(pyxel.KEY_DOWN) or pyxel.btnp(pyxel.KEY_S):
            if c in columns:
                handle_player_turn(columns[c], 12, 1)

    def check_four_consecutive(lst, value):
        return any(all(lst[i+j] == value for j in range(4)) for i in range(len(lst) - 3))

    def check_vertical_win(columns, value):
        return any(check_four_consecutive(column, value) for column in columns)

    def check_horizontal_win(columns, value):
        return any(check_four_consecutive([columns[i][j] for i in range(len(columns))], value) for j in range(len(columns[0])))

    def check_diagonal_win(columns, value):
        for i in range(len(columns) - 3):
            for j in range(len(columns[0]) - 3):
                if all(columns[i+k][j+k] == value for k in range(4)) or all(columns[i+3-k][j+k] == value for k in range(4)):
                    return True
        return False

    columns = [c1, c2, c3, c4, c5, c6, c7]

    if check_vertical_win(columns, 6) or check_horizontal_win(columns, 6) or check_diagonal_win(columns, 6):
        j = 3
        winner = "J1"
    elif check_vertical_win(columns, 12) or check_horizontal_win(columns, 12) or check_diagonal_win(columns, 12):
        j = 4
        winner = "J2"
    elif all(all(cell != 0 for cell in column) for column in columns):
        j = 5
        winner = "nul"

    if j == 3 or j == 4:
        pyxel.rectb(2 if j == 3 else 54,28,7,19,11)
        pyxel.text(16,50,f"{winner} a win",8)
    elif j == 5:
        pyxel.rectb(2,28,7,19,13)
        pyxel.rectb(54,28,7,19,13)
        pyxel.text(15,50,f"Match {winner}",8)

j = 1
c = 29
c1 = [0]*6
c2 = [0]*6
c3 = [0]*6
c4 = [0]*6
c5 = [0]*6
c6 = [0]*6
c7 = [0]*6

pyxel.run(update, draw)