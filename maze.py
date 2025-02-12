import os
import time
from stack import Stack


class maze:
    def __init__(self) -> None:
        self.maze = [["X", "X", "X", "X", "X", "X", "X"],
                     ["X", " ", " ", " ", "X", " ", "X"],
                     ["X", " ", "X", " ", "X", " ", " "],
                     ["X", " ", "X", " ", "X", " ", "X"],
                     ["X", " ", "X", " ", " ", " ", "X"],
                     ["X", " ", "X", "X", "X", "X", "X"]]
        self.ply = pos(5, 1)
        self.end = pos(2, 6)
        self.maze[self.ply.y][self.ply.x] = "P"
        self.maze[self.end.y][self.end.x] = "E"
        self.num_rows = len(self.maze)
        self.num_cols = len(self.maze[0])
        self.visited = [[False] * self.num_cols for i in range(self.num_rows)]

    def isInBound(self, y, x):
        if y >= 0 and x >= 0 and y < len(self.maze) and x < len(self.maze[0]):
            return True
        else:
            return False

    def print(self):
        os.system("cls")
        print("\n\n\n")
        for row in self.maze:
            for col in row:
                print(col, " ", end="")
            print("")
        print("\n\n\n")

    def printEND(self):
        os.system("cls")
        print("\n\n\n")
        print(">>>>> Congraturation!!! <<<<<")
        print("\n\n\n")

#เพิ่มการทำงานการเคลื่อนที่
    def find_next_move(self, curr_pos):
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dir in dirs:
            next_move = pos(curr_pos.y + dir[0], curr_pos.x + dir[1])
            if self.isInBound(next_move.y, next_move.x) \
               and self.visited[next_move.y][next_move.x] == False \
                    and self.maze[next_move.y][next_move.x] != "X":
                return next_move
        return None
#ฟังก์ชันการทำงานโดยอัตโนมัติ
    def move_auto(self):
        stack = Stack()
        stack.push(self.ply)
        self.visited[self.ply.y][self.ply.x] = True
        while not stack.isEmpty():
            curr_pos = stack.peek()
            next_move = self.find_next_move(curr_pos)
            if next_move is not None:
                self.maze[self.ply.y][self.ply.x] = " "
                self.maze[next_move.y][next_move.x] = "P"
                self.ply = next_move
                time.sleep(0.25)

                stack.push(next_move)
                self.visited[next_move.y][next_move.x] = True

                self.print()

                if next_move == self.end:
                    time.sleep(0.25)
                    self.printEND()
                    return
            else:
                prev_move = stack.pop()
                self.ply = stack.peek()

                self.maze[prev_move.y][prev_move.x] = " "
                self.maze[self.ply.y][self.ply.x] = "P"
                time.sleep(0.25)
                self.print()


class pos:
    def __init__(self) -> None:
        self.y = None
        self.x = None

    def __init__(self, y, x) -> None:
        self.y = y
        self.x = x

    def __eq__(self, other) -> bool:
        return self.y == other.y and self.x == other.x

# ------------------------ #
# ===== MAIN PROGRAM ===== #
# ------------------------ #


m = maze()
m.print()
m.move_auto()
