import pyray
from raylib import colors
import random
import math

pos = [
    (0, 0),
    (45, 100), (195, 100), (375, 100), (465, 100), (645, 100), (795, 100),
    (45, 220), (195, 220), (285, 220), (375, 220), (465, 220), (555, 220), (645, 220), (795, 220),
    (45, 310), (195, 310), (285, 310), (375, 310), (465, 310), (555, 310), (645, 310), (795, 310),
    (285, 400), (375, 400), (465, 400), (555, 400),
    (195, 500), (285, 500), (555, 500), (645, 500),
    (285, 590), (555, 590),
    (45, 680), (195, 680), (285, 680), (375, 680), (465, 680), (555, 680), (645, 680), (795, 680),
    (45, 770), (105, 770), (195, 770), (285, 770), (375, 770), (465, 770), (555, 770), (645, 770), (735, 770), (795, 770),
    (45, 860), (105, 860), (195, 860), (285, 860), (375, 860), (465, 860), (555, 860), (645, 860), (735, 860), (795, 860),
    (45, 950), (375, 950), (465, 950), (795, 950)
]
graph = [
    [],#0 nothing (numeration goes from left up to right, like you read letters)
    #line 1
    [2, 7],#1
    [1, 3, 8],#2
    [2, 10],#3
    [5, 11],#4
    [4, 6, 13],#5
    [5, 14],#6
    #line 2
    [1, 8, 15],#7
    [2, 7, 9, 16],#8
    [8, 10, 17],#9
    [3, 9, 11],#10
    [4, 10, 12],#11
    [11, 13, 20],#12
    [5, 12, 14, 21],#13
    [6, 13, 22],#14
    #line 3
    [7, 16],#15
    [8, 15, 27],#16
    [9, 18],#17
    [17, 24],#18
    [20, 25],#19
    [12, 19],#20
    [13, 22, 30],#21
    [14, 21],#22
    #line 4
    [24, 28],#23
    [18, 23, 25],#24
    [19, 24, 26],#25
    [25, 29],#26
    #line 5
    [16, 28, 34],#27 and a tunnel 30 i if(ed)
    [23, 27, 31],#28
    [26, 30, 32],#29
    [21, 29, 39],#30 and a tunnel to 27 i if(ed)
    #line 6
    [28, 32, 35],#31
    [29, 31, 38],#32
    #line 7
    [34, 41],#33
    [27, 33, 35, 43],#34
    [31, 34, 36],#35
    [35, 45],#36
    [38, 46],#37
    [32, 37, 39],#38
    [30, 38, 40, 48],#39
    [39, 50],#40
    #line 8
    [33, 42],#41
    [41, 52],#42
    [34, 44, 53],#43
    [43, 45, 54],#44
    [36, 44, 46],#45
    [37, 45, 47],#46
    [46, 48, 57],#47
    [39, 47, 58],#48
    [50, 59],#49
    [40, 49],#50
    #line 9
    [52, 61],#51
    [42, 51, 53],#52
    [43, 52],#53
    [44, 55],#54
    [54, 62],#55
    [57, 63],#56
    [47, 56],#57
    [48, 59],#58
    [49, 58, 60],#59
    [59, 64],#60
    #line 10
    [51, 62],#61
    [55, 61, 63],#62
    [56, 62, 64],#63
    [60, 63]#64
]
class Knot:
    def __init__(self, x: int, y: int, r: int = 27, color=colors.GREEN) -> None:
        self.x = x
        self.y = y
        self.r = r
        self.status = 0
        self.color = color
    def draw(self) -> None:
        pyray.draw_rectangle(self.x, self.y, self.r, self.r, self.color)
    def repr(self) -> str:
        return f'Knot({self.x}, {self.y})'

class ghost:
    def __init__(self, up_1, up_2, l_1, l_2, r_1, r_2, down_1, down_2, sc_up_1, sc_up_2, sc_l_1, sc_l_2, sc_r_1, sc_r_2, sc_down_1, sc_down_2):
        self.pac_x = 0
        self.pac_y = 0
        self.up_1 = up_1
        self.up_2 = up_2
        self.l_1 = l_1
        self.l_2 = l_2
        self.down_1 = down_1
        self.down_2 = down_2
        self.r_1 = r_1
        self.r_2 = r_2
        self.sc_up_1 = sc_up_1
        self.sc_up_2 = sc_up_2
        self.sc_l_1 = sc_l_1
        self.sc_l_2 = sc_l_2
        self.sc_r_1 = sc_r_1
        self.sc_r_2 = sc_r_2
        self.sc_down_1 = sc_down_1
        self.sc_down_2 = sc_down_2
        self.x_move = -5
        self.y_move = 0
        self.cur_anim = 1
        self.visual = colors.WHITE
        self.pos = pyray.Vector2(602, 500)
        self.next_point = 29
        self.prev_point = 30
        self.status = 0
        self.scared = 0
        self.dead = 0
    def draw(self):
        if (self.scared == 0):
            if (self.x_move == 5 and self.cur_anim == 1):
                pyray.draw_texture(self.r_1, int(self.pos.x + self.r_1.width // 2),  int(self.pos.y + 4), self.visual)
            elif (self.x_move == 5 and self.cur_anim == -1):
                pyray.draw_texture(self.r_2, int(self.pos.x + self.r_2.width // 2),  int(self.pos.y + 4), self.visual)
            elif (self.x_move == -5 and self.cur_anim == 1):
                pyray.draw_texture(self.l_1, int(self.pos.x + self.l_1.width // 2),  int(self.pos.y + 4), self.visual)
            elif (self.x_move == -5 and self.cur_anim == -1):
                pyray.draw_texture(self.l_2, int(self.pos.x + self.l_2.width // 2),  int(self.pos.y + 4), self.visual)
            elif (self.y_move == -5 and self.cur_anim == 1):
                pyray.draw_texture(self.up_1, int(self.pos.x + self.up_1.width // 2),  int(self.pos.y + 4), self.visual)
            elif (self.y_move == -5 and self.cur_anim == -1):
                pyray.draw_texture(self.up_2, int(self.pos.x + self.up_2.width // 2),  int(self.pos.y + 4), self.visual)
            elif (self.y_move == 5 and self.cur_anim == 1):
                pyray.draw_texture(self.down_1, int(self.pos.x + self.down_1.width // 2),  int(self.pos.y + 4), self.visual)
            elif (self.y_move == 5 and self.cur_anim == -1):
                pyray.draw_texture(self.down_2, int(self.pos.x + self.down_2.width // 2),  int(self.pos.y + 4), self.visual)   
        else:
            if (self.x_move == 5 and self.cur_anim == 1):
                pyray.draw_texture(self.sc_r_1, int(self.pos.x + self.sc_r_1.width // 2),  int(self.pos.y + 4), self.visual)
            elif (self.x_move == 5 and self.cur_anim == -1):
                pyray.draw_texture(self.sc_r_2, int(self.pos.x + self.sc_r_2.width // 2),  int(self.pos.y + 4), self.visual)
            elif (self.x_move == -5 and self.cur_anim == 1):
                pyray.draw_texture(self.sc_l_1, int(self.pos.x + self.sc_l_1.width // 2),  int(self.pos.y + 4), self.visual)
            elif (self.x_move == -5 and self.cur_anim == -1):
                pyray.draw_texture(self.sc_l_2, int(self.pos.x + self.sc_l_2.width // 2),  int(self.pos.y + 4), self.visual)
            elif (self.y_move == -5 and self.cur_anim == 1):
                pyray.draw_texture(self.sc_up_1, int(self.pos.x + self.sc_up_1.width // 2),  int(self.pos.y + 4), self.visual)
            elif (self.y_move == -5 and self.cur_anim == -1):
                pyray.draw_texture(self.sc_up_2, int(self.pos.x + self.sc_up_2.width // 2),  int(self.pos.y + 4), self.visual)
            elif (self.y_move == 5 and self.cur_anim == 1):
                pyray.draw_texture(self.sc_down_1, int(self.pos.x + self.sc_down_1.width // 2),  int(self.pos.y + 4), self.visual)
            elif (self.y_move == 5 and self.cur_anim == -1):
                pyray.draw_texture(self.sc_down_2, int(self.pos.x + self.sc_down_2.width // 2),  int(self.pos.y + 4), self.visual)   

    def move_logic_red(self, super_active = 0):
        if (self.pos.x != pos[self.next_point][0] - 27 // 2 or self.pos.y != pos[self.next_point][1]):
            self.pos.x += self.x_move
            self.pos.y += self.y_move
            self.cur_anim *= -1
        else:
            new_p = self.next_point
            while True:
                new_p = graph[self.next_point][random.randint(0, len(graph[self.next_point]) - 1)]
                if (new_p != self.prev_point):
                    break
            self.prev_point = self.next_point
            self.next_point = new_p
            if (pos[self.next_point][0] - 27 // 2 > self.pos.x):
                self.x_move = 5
                self.y_move = 0
            elif (pos[self.next_point][0] - 27 // 2 < self.pos.x):
                self.x_move = -5
                self.y_move = 0
            elif (pos[self.next_point][1] > self.pos.y):
                self.x_move = 0
                self.y_move = 5
            else:
                self.x_move = 0
                self.y_move = -5
            #print(self.next_point)
        if (super_active > 0):
            self.scared = 1
        else:
            self.scared = 0
    def move_logic_yellow(self, hero, super_active = 0):
        if (super_active == 0):
            self.scared = 0
            if (self.status == 0):
                self.status = 1
                self.pac_x = hero.x
                self.pac_y = hero.y
            if (self.pac_x - 27 <= self.pos.x and self.pos.x <= self.pac_x and self.pos.y >= self.pac_y - 27 and self.pac_y >= self.pos.y and self.status == 1):
                self.status = 0
            if (self.status == 1):
                if (self.pac_x - 27 >= self.pos.x):
                    self.pos.x += 3
                    self.x_move = 5
                elif (self.pac_x - 20 <= self.pos.x):
                    self.pos.x -= 3
                    self.x_move = -5
                if (self.pac_y - 20 >= self.pos.y):
                    self.pos.y += 3
                    self.y_move = 5
                elif (self.pac_y - 10 <= self.pos.y):
                    self.pos.y -= 3
                    self.y_move = -5
                self.cur_anim *= -1
        else:
            self.status = 0
            self.scared = 1
            self.pac_x = 400
            self.pac_y = 500
            if (self.pac_x  - 27 >= self.pos.x):
                self.pos.x += 3
                self.x_move = 5
            elif (self.pac_x  - 20 <= self.pos.x):
                self.pos.x -= 3
                self.x_move = -5
            if (self.pac_y - 20 >= self.pos.y):
                self.pos.y += 3
                self.y_move = 5
            elif (self.pac_y - 10 <= self.pos.y):
                self.pos.y -= 3
                self.y_move = -5
            self.cur_anim *= -1
            

def knot_drawer(self):
    for knot in pos:
            kn = Knot(*knot)
            kn.draw()
class Wall:
    def __init__(self, x: int, y: int, w: int, h: int, color=colors.SKYBLUE): 
        self.x = x
        self.y = y 
        self.w = w
        self.h = h 
        self.color = color  
    def draw(self):
        pyray.draw_rectangle(self.x, self.y, self.w, self.h, self.color)
walls = [
    # левые боковые 
    Wall(1_8, 73, 27, 931), 
    Wall(822, 73, 27, 931), 

    # нижняя большая стена 
    Wall(4_5, 977, 780, 27), 
 
    # big left wall 1 
    Wall(4_5, 337, 150, 163), 
 
    # big left wall 2 
    Wall(4_5, 527, 150, 153), 
 
    # big right wall 1 
    Wall(672, 337, 150, 163), 
 
    # big right wall 2 
    Wall(672, 527, 150, 153), 
 
 
    Wall(4_5, 7_3, 780, 2_7),  # upper 
    Wall(7_2, 127, 123, 9_3), 
    Wall(222, 127, 153, 9_3), 
    Wall(402, 100, 6_3, 120), 
    Wall(492, 127, 153, 9_3), 
    Wall(672, 127, 123, 9_3), 
 
    Wall(7_2, 247, 123, 6_3), 
    Wall(222, 247, 6_3, 253), 
    Wall(312, 247, 243, 6_3),  # 
    Wall(285, 337, 9_0, 6_3), 
    Wall(402, 310, 6_3, 9_0), 
    Wall(582, 247, 6_3, 253), 
    Wall(492, 337, 9_0, 6_3), 
    Wall(672, 247, 123, 6_3), 
 
    Wall(312, 427, 243, 164),  # big ponos in the middle 
    Wall(222, 527, 6_3, 153), 
    Wall(582, 527, 6_3, 153), 
    Wall(312, 617, 243, 6_3),  # (285, 680) 
    Wall(402, 680, 6_3, 9_0),  # (375, 220) 
 
    Wall(7_2, 707, 123, 6_3), 
    Wall(222, 707, 153, 6_3), 
    Wall(492, 707, 153, 6_3), 
    Wall(672, 707, 123, 6_3), 
 
    Wall(132, 770, 6_3, 9_0), 
    Wall(672, 770, 6_3, 9_0), 
 
    Wall(222, 797, 6_3, 9_0), 
    Wall(312, 797, 243, 6_3), 
    Wall(582, 797, 6_3, 9_0), 
 
    Wall(7_2, 887, 303, 6_3), 
    Wall(492, 887, 303, 6_3), 
    Wall(402, 860, 6_3, 9_0), 
 
    # small wall below: 1 
    Wall(4_5, 797, 6_0, 6_3), 
    # small wall below: 2 
    Wall(762, 797, 6_0, 6_3),  
 ]
def wall_drawer():
     for wall in walls:
         wall.draw()


class point:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.eaten = False
        self.super = False
    def check_eat(self, hero):
        if (self.eaten != 1 and hero.x + 10 > self.x and hero.x - 10 < self.x and hero.y + 10 > self.y and hero.y - 10 < self.y):
            self.eaten = 1
            if (self.super):
                return 12, 0.02
            else:
                return 0, 0.02
        return 0, 0
        
    def draw(self):
        if (self.super == False):
            pyray.draw_circle(self.x, self.y, 5, pyray.WHITE)
        else:
            pyray.draw_circle(self.x, self.y, 5 + 2, pyray.YELLOW)
    
class pacman:
    def __init__(self):
        self.x = 290
        self.closing = True
        self.direction = "right"
        self.y = 500 + 13
        self.size = 20
        self.x1 = 1
        self.y1 = 1
        self.speed = 5 #скорость этой чурки
    def draw_pacman(self):
        pyray.draw_circle(self.x, self.y, self.size // 2, pyray.YELLOW)
        # Определяем треугольник в зависимости от направления
        if self.direction == "left":
            triangle_points = [
                (self.x - 20, self.y - self.y1),
                (self.x - 20, self.y + self.y1),
                (self.x + 3, self.y)
            ]
        elif self.direction == "right":
            triangle_points = [
                (self.x + 20, self.y + self.y1),
                (self.x + 20, self.y - self.y1),
                (self.x - 3, self.y)
            ]
        elif self.direction == "down":
            triangle_points = [
                (self.x - self.x1, self.y + 20),
                (self.x + self.x1, self.y + 20),
                (self.x, self.y)
            ]
        elif self.direction == "up":
            triangle_points = [
                (self.x + self.x1, self.y - 20),
                (self.x - self.x1, self.y - 20),
                (self.x, self.y)
            ]
        else:
            return

        pyray.draw_triangle(triangle_points[0], triangle_points[1], triangle_points[2], pyray.BLACK)

    def pacman_logic(self):
        # Обработка движения Pacman
        if self.direction == "left":
            self.x -= self.speed
            if self.closing:
                self.y1 -= 1
            else:
                self.y1 += 1
        elif self.direction == "right":
            self.x += self.speed
            if self.closing:
                self.y1 -= 1
            else:
                self.y1 += 1
        elif self.direction == "down":
            self.y += self.speed
            if self.closing:
                self.x1 -= 1
            else:
                self.x1 += 1
        elif self.direction == "up":
            self.y -= self.speed
            if self.closing:
                self.x1 -= 1
            else:
                self.x1 += 1
        #коллизия пакмана
        for i in walls:
            if (self.x + self.size / 2 > i.x and self.x - self.size / 2 < i.x + i.w and self.y + self.size / 2 > i.y and self.y - self.size / 2 < i.y + i.h):
                #print(i.x, i.y, i.w, i.h)
                if (self.direction == "left"):
                    self.x += self.speed
                elif (self.direction == "right"):
                    self.x -= self.speed
                elif (self.direction == "up"):
                    self.y += self.speed
                else:
                    self.y -= self.speed
                break
        # Проверка состояния "закрытия" рта
        if self.x1 < 1 or self.y1 < 1:
           # print(self.y1, self.x1, 1)hopefully fixed
            self.closing = False
            self.x1 = 1
            self.y1 = 1
        elif self.x1 > 29 or self.y1 > 29:
            #print(self.y1, self.x1, 2)
            self.closing = True
            self.x1 = 29
            self.y1 = 29
        
        # Управление направлением
        if pyray.is_key_down(pyray.KEY_A):
            self.direction = "left"
        elif pyray.is_key_down(pyray.KEY_D):
            self.direction = "right"
        elif pyray.is_key_down(pyray.KEY_S):
            self.direction = "down"
        elif pyray.is_key_down(pyray.KEY_W):
            self.direction = "up"
    def catch_check(self, ghosty):
        if (ghosty.scared == 0):
            if (ghosty.pos.x + 40 >= self.x and ghosty.pos.x <= self.x and ghosty.pos.y + 40 >= self.y and ghosty.pos.y <= self.y):
                #print('loser'):((((((((
                return True
            return False
        else:
            global accum_time
            accum_time = 5
            if (ghosty.pos.x + 40 >= self.x and ghosty.pos.x <= self.x and ghosty.pos.y + 40 >= self.y and ghosty.pos.y <= self.y):
                ghosty.dead = 1
            return False
class timer():
    def __init__(self):
        self.sec = 0
        self.min = 0
    def timer_go(self):
        self.sec += 0.035
        if self.sec >= 60:
            self.min +=1
            self.sec = 0
        pyray.draw_text(f"{self.min:02}.{int(self.sec):02}", 300, 40, 30, colors.WHITE)


def create_points():
    points_array = []
    for i in range(2, 28):#fin
        points_array.append([])
        for j in range(3, 33):
            a = point()
            a.x = i * 30#fin
            a.y = j * 30 - 2#fin
            super_check = random.randint(1, 100)
            if (super_check == 100):
                a.super = True
            points_array[i - 2].append(a)

    return points_array#all in all  there are 


def main():
    width = 845
    height = 1000
    pyray.init_audio_device()
    pyray.init_window(width, height, "Main")
    pyray.set_target_fps(30)
    game_music = pyray.load_sound("ruin.mp3")
    #pyray.set_sound_volume(game_music,1)
    death_music = pyray.load_sound("death.mp3")
    #pyray.set_sound_volume(death_music,1)
    main_menu_music = pyray.load_sound("menu.mp3")
    hard_music = pyray.load_sound("hard_time.mp3")
    #pyray.set_sound_volume(main_menu_music,1)
    #scary begin(too lazy for function)
    f = pyray.load_image("scared_up_1.png")
    scared_up_1 = pyray.load_texture_from_image(f)
    f = pyray.load_image("scared_up_2.png")
    scared_up_2 = pyray.load_texture_from_image(f)
    f = pyray.load_image("scared_left_1.png")
    scared_left_1 = pyray.load_texture_from_image(f)
    f = pyray.load_image("scared_left_2.png")
    scared_left_2 = pyray.load_texture_from_image(f)
    f = pyray.load_image("scared_right_1.png")
    scared_right_1 = pyray.load_texture_from_image(f)
    f = pyray.load_image("scared_right_2.png")
    scared_right_2 = pyray.load_texture_from_image(f)
    f = pyray.load_image("scared_down_1.png")
    scared_down_1 = pyray.load_texture_from_image(f)
    f = pyray.load_image("scared_down_2.png")
    scared_down_2 = pyray.load_texture_from_image(f)
    pyray.unload_image(f)
    #red begin(too lazy for function)
    f = pyray.load_image("red_up_1.png")
    up_1 = pyray.load_texture_from_image(f)
    f = pyray.load_image("red_up_2.png")
    up_2 = pyray.load_texture_from_image(f)
    f = pyray.load_image("red_left_1.png")
    left_1 = pyray.load_texture_from_image(f)
    f = pyray.load_image("red_left_2.png")
    left_2 = pyray.load_texture_from_image(f)
    f = pyray.load_image("red_right_1.png")
    right_1 = pyray.load_texture_from_image(f)
    f = pyray.load_image("red_right_2.png")
    right_2 = pyray.load_texture_from_image(f)
    f = pyray.load_image("red_down_1.png")
    down_1 = pyray.load_texture_from_image(f)
    f = pyray.load_image("red_down_2.png")
    down_2 = pyray.load_texture_from_image(f)
    pyray.unload_image(f)
    red = ghost(up_1, up_2, left_1, left_2, right_1, right_2, down_1, down_2, scared_up_1, scared_up_2, scared_left_1, scared_left_2, scared_right_1, scared_right_2, scared_down_1, scared_down_2)
    #red ghost copys
    red_2 = ghost(up_1, up_2, left_1, left_2, right_1, right_2, down_1, down_2, scared_up_1, scared_up_2, scared_left_1, scared_left_2, scared_right_1, scared_right_2, scared_down_1, scared_down_2)
    red_3 = ghost(up_1, up_2, left_1, left_2, right_1, right_2, down_1, down_2, scared_up_1, scared_up_2, scared_left_1, scared_left_2, scared_right_1, scared_right_2, scared_down_1, scared_down_2)
    #red end
    #green begin
    f = pyray.load_image("green_up_1.png")
    up_1 = pyray.load_texture_from_image(f)
    f = pyray.load_image("green_up_2.png")
    up_2 = pyray.load_texture_from_image(f)
    f = pyray.load_image("green_left_1.png")
    left_1 = pyray.load_texture_from_image(f)
    f = pyray.load_image("green_left_2.png")
    left_2 = pyray.load_texture_from_image(f)
    f = pyray.load_image("green_right_1.png")
    right_1 = pyray.load_texture_from_image(f)
    f = pyray.load_image("green_right_2.png")
    right_2 = pyray.load_texture_from_image(f)
    f = pyray.load_image("green_down_1.png")
    down_1 = pyray.load_texture_from_image(f)
    f = pyray.load_image("green_down_2.png")
    down_2 = pyray.load_texture_from_image(f)
    pyray.unload_image(f)
    green = ghost(up_1, up_2, left_1, left_2, right_1, right_2, down_1, down_2, scared_up_1, scared_up_2, scared_left_1, scared_left_2, scared_right_1, scared_right_2, scared_down_1, scared_down_2)
    #green ghost copys
    green_2 = ghost(up_1, up_2, left_1, left_2, right_1, right_2, down_1, down_2, scared_up_1, scared_up_2, scared_left_1, scared_left_2, scared_right_1, scared_right_2, scared_down_1, scared_down_2)
    green_3 = ghost(up_1, up_2, left_1, left_2, right_1, right_2, down_1, down_2, scared_up_1, scared_up_2, scared_left_1, scared_left_2, scared_right_1, scared_right_2, scared_down_1, scared_down_2)
    #green end
    #yellow begin
    f = pyray.load_image("yellow_up_1.png")
    up_1 = pyray.load_texture_from_image(f)
    f = pyray.load_image("yellow_up_2.png")
    up_2 = pyray.load_texture_from_image(f)
    f = pyray.load_image("yellow_left_1.png")
    left_1 = pyray.load_texture_from_image(f)
    f = pyray.load_image("yellow_left_2.png")
    left_2 = pyray.load_texture_from_image(f)
    f = pyray.load_image("yellow_right_1.png")
    right_1 = pyray.load_texture_from_image(f)
    f = pyray.load_image("yellow_right_2.png")
    right_2 = pyray.load_texture_from_image(f)
    f = pyray.load_image("yellow_down_1.png")
    down_1 = pyray.load_texture_from_image(f)
    f = pyray.load_image("yellow_down_2.png")
    down_2 = pyray.load_texture_from_image(f)
    pyray.unload_image(f)
    yellow = ghost(up_1, up_2, left_1, left_2, right_1, right_2, down_1, down_2, scared_up_1, scared_up_2, scared_left_1, scared_left_2, scared_right_1, scared_right_2, scared_down_1, scared_down_2)
    #yellow end
    hero = pacman()
    tim = timer()
    pac_cur_next = 28
    parser = 0
    #clones logic
    red_counter = 1
    green_counter = 1
    #lives = 1
    multiplayer = 1
    #super
    super_active = 0
    accum_time = 0
    #points things you eat
    points_array = create_points()#298 points are visible and eatable
    while not pyray.window_should_close() and pyray.get_key_pressed() == 0:
       pyray.begin_drawing()
       if (not pyray.is_sound_playing(main_menu_music)):
           pyray.play_sound(main_menu_music)
       pyray.draw_text("MAIN MENU", 200, 100, 100, colors.WHITE)
       pyray.draw_text("Controls:", 100, 200, 40, colors.WHITE)
       pyray.draw_text("W - go up", 120, 250, 40, colors.WHITE)
       pyray.draw_text("A - go left", 120, 300, 40, colors.WHITE)
       pyray.draw_text("S - go down", 120, 350, 40, colors.WHITE)
       pyray.draw_text("D - go right", 120, 400, 40, colors.WHITE)
       pyray.draw_text("P - pause", 120, 450, 40, colors.WHITE)
       pyray.draw_text("Each point gives you 0.02 seconds", 120, 500, 40, colors.WHITE)
       pyray.draw_text("Claiming all points is cool", 120, 550, 40, colors.WHITE)
       pyray.draw_text("Super lasts 12 seconds", 120, 600, 40, colors.WHITE)
       pyray.draw_text("You can't scare clo...(oops)", 120, 650, 40, colors.WHITE)
       pyray.draw_text("Press any key to continue", 150, 750, 40, colors.WHITE)
       pyray.draw_text("IF you close this window, you LOSE", 50, 800, 40, colors.RED)
       pyray.clear_background(colors.BLACK)
       pyray.end_drawing()
    #pyray.close_window()
    #pyray.init_window(width, height, "Game")
    pyray.stop_sound(main_menu_music)
    all_points = 0
    while not pyray.window_should_close() and parser == 0:
        pyray.begin_drawing()
        pyray.clear_background(colors.BLACK)
        #timer logic
        tim.timer_go()
        tim.sec += accum_time
        if (not pyray.is_sound_playing(game_music) and not pyray.is_sound_playing(hard_music)):#music
            if (red_counter >= 2):
                pyray.stop_sound(game_music)
                pyray.play_sound(hard_music)
            else:
                pyray.play_sound(game_music)

        hero.pacman_logic()#pacman
        hero.draw_pacman()
        
        for i in points_array:
            for j in i:
                if (j.eaten == 0):
                    j.draw()
                all_points += j.eaten
                alpha, betta = j.check_eat(hero)
                accum_time += betta#POINTSSSSSSSSSS
                super_active = max(super_active, alpha)
        if (all_points == 298):
            all_points = 0
            for i in points_array:
                for j in i:
                    j.super = False
                    angleses = random.randint(1, 100)
                    if (angleses == 1):
                        j.super = True
                    j.eaten = 0
            multiplayer += 1
        # knot_drawer(pos)#knots
        wall_drawer()#wall
        #SUPER TIMER
        super_active = max(0, super_active - 0.035)
        #SUPER_TIMER_END
        #print(red.scared)

        if (red.dead == 0):
            red.move_logic_red(super_active)#red
            red.draw()

        if (green.dead == 0):
            green.move_logic_red(super_active)#green
            green.draw()

        #clones_red
        if (red_counter >= 2):
            red_2.move_logic_red()#red clone 1
            red_2.draw()
        if (red_counter >= 3):
            red_3.move_logic_red()#red clone 2
            red_3.draw()
        #clones_green
        if (green_counter >= 2):
            green_2.move_logic_red()#green clone 1
            green_2.draw()
        if (green_counter >= 3):
            green_3.move_logic_red()#green clone 2
            green_3.draw()

        #timer clone logic
        if (tim.min == 1):
            red_counter = 2
        elif (tim.min == 2):
            green_counter = 2
        elif (tim.min == 3):
            red_counter = 2
        elif (tim.min == 4):
            green_counter = 3
        

        #pause screen
        if (pyray.get_key_pressed() == 80):
            pyray.end_drawing()
            while (pyray.get_key_pressed() == 0):
                pyray.begin_drawing()
                pyray.clear_background(colors.BLACK)
                pyray.draw_text("PAUSED", 200, 400, 100, colors.WHITE)
                pyray.end_drawing()
            pyray.begin_drawing()
        
        #supers
        pyray.draw_text("Score multi by " + str(multiplayer), 400, 40, 30, colors.WHITE)

        if (yellow.dead == 0):
            yellow.move_logic_yellow(hero, super_active)#yellow
            yellow.draw()

        
        accum_time = 0
        if (hero.catch_check(red) or hero.catch_check(green) or hero.catch_check(yellow)):
            parser = 1
        if ((hero.catch_check(red_3) and red_counter >= 3) or hero.catch_check(red_2) and red_counter >= 2):
            parser = 1
        if (hero.catch_check(green_2) and green_counter >= 2 or hero.catch_check(green_3) and green_counter >= 3):
            parser = 1

        if (super_active == 0):
            yellow.dead = 0
            red.dead = 0
            green.dead = 0

        
        pyray.end_drawing()

    #game done
    pyray.close_window()
    pyray.init_window(width + 800, height, "your soul")
    your_name = ""
    cur_key = pyray.KeyboardKey(0)
    pyray.stop_sound(game_music)
    pyray.stop_sound(hard_music)
    while (not pyray.window_should_close() and cur_key != 257):
        if (not pyray.is_sound_playing(death_music)):#music
           pyray.play_sound(death_music)
        pyray.begin_drawing()
        pyray.draw_text("Enter your name : " + your_name, 100, 400, 50, colors.WHITE)
        pyray.draw_text("Press Enter to continue", 100, 600, 20, colors.WHITE)

        cur_key = pyray.get_key_pressed()
        if (cur_key != 257 and cur_key != 0 and cur_key != 259):
            your_name += chr(cur_key)
        if (cur_key == 259 and len(your_name) > 0):
            your_name = your_name[:-1]
        pyray.clear_background(colors.BLACK)
        pyray.end_drawing()
    pyray.stop_sound(death_music)
    
    pyray.close_window()
    pyray.init_window(width, height, "you lost")
    #запись результата в файл
    f = open("scores.txt", "r")
    f1 = open("scores.txt", "a")
    a = f.readlines()
    if (len(a) != 0):
        a[len(a) - 1] += ("\n")
    a2 = {}
    for i in a:
        name, score = i.split(":")
        score = score[:-1]
        a2[name] = int(score)
    a2[your_name] = round((tim.min * 60 + tim.sec) * multiplayer)
    #print(a2)
    #f1.write("\n" + your_name + ":" + str(round(tim.min * 60 + tim.sec)))
    f1.close()
    f.close()
    a2 = dict(sorted(a2.items(), key = lambda x: x[1], reverse = True))
    while not pyray.window_should_close():
        pyray.begin_drawing()
        if (not pyray.is_sound_playing(death_music)):#music
           pyray.play_sound(death_music)
        pyray.draw_text("Your time being alive: "+f"{tim.min:02}.{int(tim.sec):02}", 200, 50, 30, colors.WHITE)
        pyray.draw_text("GAME OVER", 100, 400, 100, colors.WHITE)
        pyray.draw_text("Leaderboard(seconds):", 50, 570, 20, colors.WHITE)
        counter = 0
        for i in a2:
            pyray.draw_text(i + " : " + str(a2[i]), 60, counter * 20 + 600, 20, colors.WHITE)
            counter += 1
            
        pyray.end_drawing()
    pyray.stop_sound(death_music)
    pyray.close_window()
if __name__ == "__main__":
    main()
