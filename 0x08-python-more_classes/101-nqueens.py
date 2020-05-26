#!/usr/bin/python3
"""N Queens"""


class nQueens:

    def __init__(self, n):
        """ set the n variable """
        self.n = n

    def play(self, n):
        """ play game """
        chess_board = [[0 for i in range(n)] for y in range(n)]
        for i in range(n):
            self.solve(chess_board, i)

    def solve(self, cb, col):
        """ recursive """
        for row in range(self.n):
            if col >= self.n:
                if self.check_num_queens(cb):
                    self.matrix_to_list(cb)
                    return
            else:
                cb[row][col] = 1

            if (self.safety_check(cb, row, col)):
                self.solve(cb, col + 1)
            if col >= self.n:
                    return
            cb[row][col] = 0

    def matrix_to_list(self, cb):
        """ changes a matrix """
        queen_list = []
        for i in range(len(cb)):
            for j in range(len(cb)):
                if cb[i][j] == 1:
                    queen_list.append([j, i])
        print(queen_list)

    def check_num_queens(self, cb):
        """ number of queens"""
        count = 0
        for i in range(len(cb)):
            for j in range(len(cb)):
                if cb[i][j] == 1:
                    count += 1
        if count == len(cb):
            return True

    def safety_check(self, cb, row, col):
        """ if there are queens """
        count_a = 0
        count_b = 0
        for i in cb[row]:
            if i == 1:
                count_a += 1
            if count_a == 2:
                return False
        for r in cb:
            count = 0
            for item in r:
                if count == col:
                    if item == 1:
                        count_b += 1
                    if count_b == 2:
                        return False
                count += 1
        for i in range(len(cb)):
            for j in range(len(cb)):
                if cb[i][j] == 1:
                    height = row - i
                    width = col - j
                    if width != 0:
                        slope = abs(height / width)
                        if slope == 1:
                            return False
        if col == len(cb):
            exit(1)
        return True

    @property
    def n(self):
        """ get the n """
        return self.__n

    @n.setter
    def n(self, value):
        """ set the n """
        if value < 4:
            print("N must be at least 4")
            exit(1)
        self.__n = value

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    try:
        n = int(sys.argv[1])
    except:
        print("N must be a number")
        exit(1)
    nQueens = nQueens(n)
    nQueens.play(n)
