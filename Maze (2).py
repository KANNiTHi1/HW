import turtle
import time
import random

# directions คือทิศทางการเดิน 4 ทิศทาง (ขวา, ซ้าย, ลง, ขึ้น)
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# ขนาดของเขาวงกต (10x10)
maze = [
    "#########################",
    "#S....#.................#",
    "#.##.###.###.#.#######..#",
    "#.#....#.#...#.#........#",
    "#.#.##.#.#.###.#.#####.##",
    "#.#..#...#.#...#.#...#..#",
    "###.##.#.#.#.###.#.######",
    "#...#..#...#...........##",
    "#.###.###.###.#####.#####",
    "#.....#.....#.......#...#",
    "#.#####.###.####.####.#.#",
    "#.#.....#...#.........#.#",
    "#.#.#...#.#.#.#...#.#.#.#",
    "###E#################E###"
]

def setup_screen():
    """ กำหนดการตั้งค่าเริ่มต้นของหน้าจอ Turtle """
    screen = turtle.Screen()  # สร้างหน้าจอ
    screen.title("Maze Explorer AI")  # กำหนดชื่อหน้าต่าง
    screen.bgcolor("white")  # กำหนดสีพื้นหลัง
    screen.setup(width=600, height=600)  # กำหนดขนาดของหน้าจอ
    return screen

def draw_circle(x, y, color):
    """ วาดจุดสีที่ตำแหน่ง (x, y) """
    tile = turtle.Turtle()  # สร้างเต่าสำหรับวาด
    tile.speed(0)  # กำหนดความเร็วให้สูงสุด
    tile.penup()  # ยกปากกาขึ้นเพื่อไม่ให้วาดเส้น
    tile.goto(x, y - 5)  # เคลื่อนเต่าไปที่ตำแหน่ง (x, y)
    tile.shape("circle")  # เปลี่ยนรูปร่างของเต่าเป็นวงกลม
    tile.color(color)  # เปลี่ยนสีเต่าตามที่กำหนด
    tile.shapesize(0.5, 0.5)  # ขนาดของวงกลม
    tile.stamp()  # ตอกตราประทับ (วาดวงกลม)
    tile.hideturtle()  # ซ่อนเต่าหลังจากวาดเสร็จ

def draw_tile(x, y, color):
    """ วาดช่องทางเดินและกำแพง """
    tile = turtle.Turtle()  # สร้างเต่าสำหรับวาด
    tile.speed(0)  # กำหนดความเร็วให้สูงสุด
    tile.penup()  # ยกปากกาขึ้นเพื่อไม่ให้วาดเส้น
    tile.goto(x, y)  # เคลื่อนเต่าไปที่ตำแหน่ง (x, y)
    tile.shape("square")  # เปลี่ยนรูปร่างของเต่าเป็นสี่เหลี่ยม
    tile.color(color)  # เปลี่ยนสีเต่าตามที่กำหนด
    tile.stamp()  # ตอกตราประทับ (วาดสี่เหลี่ยม)
    tile.hideturtle()  # ซ่อนเต่าหลังจากวาดเสร็จ

def build_maze():
    """ สร้างและวาดเขาวงกตบนหน้าจอ Turtle """
    start = None
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            # คำนวณตำแหน่งที่จะแสดงแต่ละเซลล์
            x, y = -200 + col * 21, 200 - row * 21
            if maze[row][col] == "#":
                draw_tile(x, y, "orange")  # กำแพงสีส้ม
            elif maze[row][col] == "S":
                start = (row, col)  # เก็บตำแหน่งเริ่มต้น
            elif maze[row][col] == "." or maze[row][col] == "E":
                draw_tile(x, y, "white")  # ช่องทางเดินหรือจุดออกเป็นสีขาว
    return start  # คืนค่าตำแหน่งเริ่มต้น

def explore_maze(start):
    """ การสำรวจเขาวงกตโดยใช้เทคนิคการเดินทางแบบ DFS """
    stack = [start]  # ใช้ stack เพื่อเก็บตำแหน่งที่ต้องการสำรวจ
    visited = set()  # เซตที่เก็บตำแหน่งที่เยี่ยมชมแล้ว

    ai = turtle.Turtle()  # สร้างเต่าที่จะแสดงการเดิน
    ai.shape("turtle")  # รูปร่างของเต่าคือ "turtle"
    ai.color("blue")  # เต่าสีน้ำเงิน
    ai.penup()  # ยกปากกาขึ้นเพื่อไม่ให้วาดเส้น
    ai.speed(2)  # กำหนดความเร็วในการเดิน

    while stack:  # ขณะที่ยังมีตำแหน่งใน stack
        current = stack[-1]  # ใช้ตำแหน่งที่อยู่บนสุดของ stack
        x, y = -200 + current[1] * 21, 200 - current[0] * 21  # คำนวณตำแหน่งของเต่า
        ai.goto(x, y)  # เคลื่อนเต่าไปที่ตำแหน่ง (x, y)
        draw_circle(x, y, "green")  # วาดจุดสีเขียวที่ตำแหน่งปัจจุบัน
        time.sleep(0.05)  # หน่วงเวลาเพื่อให้เห็นการเดิน

        if maze[current[0]][current[1]] == "E":  # หยุดเมื่อถึงจุดออก (E)
            draw_circle(x, y, "green")  # วาดจุดสีแดงที่จุดออก
            return  # หยุดการทำงานทันที

        visited.add(current)  # เพิ่มตำแหน่งปัจจุบันในเซต visited
        random.shuffle(directions)  # สุ่มทิศทางการเดิน

        # พยายามหาทางเลือกใหม่จากทิศทางที่สุ่มมา
        found_new_path = False
        for d in directions:
            neighbor = (current[0] + d[0], current[1] + d[1])  # คำนวณตำแหน่งของเพื่อนบ้าน

            # เช็คว่าเพื่อนบ้านอยู่นอกเขาวงกตหรือเป็นกำแพงหรือไม่
            if (0 <= neighbor[0] < len(maze)) and (0 <= neighbor[1] < len(maze[0])) and maze[neighbor[0]][neighbor[1]] != "#" and neighbor not in visited:
                stack.append(neighbor)  # ถ้าไม่ใช่ทางตัน ให้เพิ่มเพื่อนบ้านใน stack
                found_new_path = True  # พบทางเลือกใหม่

        # ถ้าไม่มีทางเลือกใหม่ (ทางตัน) ให้ย้อนกลับไปยังจุดก่อนหน้า
        if not found_new_path:
            stack.pop()  # ย้อนกลับไปยังตำแหน่งก่อนหน้าใน stack
            draw_circle(x, y, "red")  # วาดจุดสีแดงที่ทางตันที่ย้อนกลับ

if __name__ == "__main__":
    screen = setup_screen()  # กำหนดการตั้งค่าเริ่มต้นของหน้าจอ
    start = build_maze()  # สร้างเขาวงกตและหาจุดเริ่มต้น
    if start:  # ถ้ามีจุดเริ่มต้น
        explore_maze(start)  # เริ่มการสำรวจเขาวงกต
    screen.mainloop()  # ทำให้หน้าจอไม่ปิดจนกว่าจะคลิก
