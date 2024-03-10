from tkinter import *
from time import sleep, time
from random import randint
import math
from fish import *
from player import *
from rod import *


HEIGHT = 800
WIDTH = 500
window = Tk()
window.title('dot goes fishing')
c = Canvas(window, width = WIDTH, height = HEIGHT,bg= '#ADD8E6')
player_id = c.create_oval(240, 140, 260, 160, fill = 'white')
fish_pond = list()
basic = rod("Basic", "A basic rod\nfor fishing", 0, 100, "red", "green")
p1 = player(c, player_id, basic)
dock = c.create_polygon(50, 100, 450, 100, 450, 200, 325, 200, 325, 600, 175, 600, 175, 200, 50, 200, fill = '#B1907F')
c.tag_raise(player_id)
c.pack()

universal_hooked = False


def check_bounds(id1, id2):
    global player_id
    x, y, w, z = c.coords(id1)
    x1 = (x + w)/2
    y1 = (y + z)/2
    pos = c.coords(id2)
    if x1 <= pos[0] and pos[15] >= y1 >= pos[1]:
        c.move(player_id, 2, 0)
    if x1 >= pos[2] and pos[15] >= y1 >= pos[1]:
        c.move(player_id, -2, 0)
    if pos[0] <= x1 <= pos[2] and pos[1] >= y1:
        c.move(player_id, 0, 2)
    if pos[14] <= x1 <= pos[12] and pos[15] <= y1:
        c.move(player_id, 0, -2)
    if pos[6] <= x1 <= pos[4] and pos[15] <= y1:
        c.move(player_id, 0, -2)
    if pos[10] <= x1 <= pos[8] and pos[9] <= y1:
        c.move(player_id, 0, -2)


def move_player(event):
    if p1.player_fish == 0:
            if event.keysym == "w":
                p1.move_up()
            elif event.keysym == "s":
                p1.move_down()
            if event.keysym == "a":
                p1.move_left()
            elif event.keysym == "d":
                p1.move_right()
            if event.keysym == "h":
                p1.help_menu()
            if event.keysym == "g":
                p1.shop_menu()
            if event.keysym == "i":
                p1.inventory_menu()
    if event.keysym == 'space':
            p1.fish()
            if universal_hooked == False and p1.player_fish == 4:
                p1.player_fish = 0
            

def stop(event):
    p1.stop()


c.bind_all('<KeyPress>', move_player)
c.bind_all('<KeyRelease>', stop)

c.create_text(50, 30, text='Cash', fill='white')
cash_text = c.create_text(50, 50, fill='white')

def show_cash(cash):
	c.itemconfig(cash_text, text=str(cash))

while True:
        check_bounds(player_id, dock)
        p1.movement()
        p1.is_fishing()
        while len(fish_pond) < 20:
            r = randint(10, 20)
            spawn_x = randint(0, 500)
            spawn_y = randint(0, 800)
            fish_id = c.create_oval(spawn_x, spawn_y, spawn_x + r, spawn_y + r, fill = '#3D426B')
            fish_type = randint(1, 20)
            if 0 < fish_type <=2:
                fish_pond.append(Bass(c, fish_id))
            elif 3 <= fish_type <= 10:
                fish_pond.append(Trout(c, fish_id))
            elif 11 <= fish_type <= 16:
                fish_pond.append(Salmon(c, fish_id))
            elif 17 <= fish_type <= 19:
                fish_pond.append(RedSnapper(c, fish_id))
            if fish_type == 20:
                c.itemconfig(fish_id, fill = '#d4af37')
                fish_pond.append(UltraRareGoldenFish(c, fish_id))
            c.tag_raise(dock)
            c.tag_raise(player_id)
            
        for i in range(len(fish_pond)):
            if fish_pond[i].hooked != True:
                fish_pond[i].move_fish(p1, universal_hooked)
            if fish_pond[i].hooked == True:
                universal_hooked = True
                fish_pond[i].move_hooked_fish(p1)
                if fish_pond[i].hooked == False:
                    universal_hooked = False
            if fish_pond[i].caught == True:
                c.delete(fish_pond[i].fish_id)
                del fish_pond[i]
                r = randint(10, 20)
                spawn_x = randint(0, 500)
                spawn_y = randint(0, 800)
                fish_id = c.create_oval(spawn_x, spawn_y, spawn_x + r, spawn_y + r, fill = '#3D426B')
                fish_type = randint(1, 20)
                if 0 < fish_type <=2:
                    fish_pond.append(Bass(c, fish_id))
                elif 3 <= fish_type <= 10:
                    fish_pond.append(Trout(c, fish_id))
                elif 11 <= fish_type <= 16:
                    fish_pond.append(Salmon(c, fish_id))
                elif 17 <= fish_type <= 19:
                    fish_pond.append(RedSnapper(c, fish_id))
                elif fish_type == 20:
                    c.itemconfig(fish_id, fill = '#d4af37')
                    fish_pond.append(UltraRareGoldenFish(c, fish_id))
                c.tag_raise(dock)
                c.tag_raise(player_id)
        if p1.hook != None:
                x1, y1, x2, y2 = c.coords(p1.hook)
                x = (x1 + x2)/2
                y = (y1 + y2)/2
                #pos = c.coords(dock)
                top_t =  50 < x < 450 and 100 < y < 200
                bottom_t = 175 < x < 325 and 200 < y < 600
                on_dock = top_t or bottom_t
                if on_dock:
                    p1.player_fish = 0
        show_cash(p1.cash)
        window.update()
        sleep(0.01)
