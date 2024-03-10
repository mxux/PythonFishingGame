from tkinter import *
from time import sleep, time
from random import randint
import fish
import player


def initialize(player, fish):
        global player_id
        global fish_stick
        global c
        global PLAYER_V_X
        global PLAYER_V_Y
        global p_direction
        global window
        HEIGHT = 100
        WIDTH = 500
        p_direction = None
        PLAYER_V_X = 0
        PLAYER_V_Y = 0
        window = Tk()
        window.title('hooked')
        c = Canvas(window, width = WIDTH, height = HEIGHT,bg= '#ADD8E6')
        x = 240
        y = 65
        difficulty = fish.size*5
        fish_stick = c.create_rectangle(250 - difficulty, 65, 250 + difficulty, 35, fill="green")
        player_id = c.create_polygon(x, y, x + 20, y, x + 10, y - 30, fill = 'white')
        c.bind_all('<KeyPress>', move_player)
        c.bind_all('<KeyRelease>', stop)
        c.pack()
        create_text()
        win = hooked(player, fish)
        window.destroy()
        return win
def move_player (event):
        global p_direction
        global PLAYER_V_X
        global PLAYER_V_Y
        global c
        pos = c.coords(player_id)
        if event.keysym == "Left":
                p_direction = "left"
                PLAYER_V_Y = 0
                PLAYER_V_X = -6
        elif event.keysym == "Right":
                p_direction = "right"
                PLAYER_V_Y = 0
                PLAYER_V_X = 6

def stop(event):
    global p_direction
    p_direction = None

def isinbox(player, box):
        global c
        pos = c.coords(player)
        x1, y1, x2, y2 = c.coords(box)
        if pos[0] > x1 and pos[2] < x2:
                return True
        else:
                return False
def create_text():
        global time_text
        global c
        c.create_text(20, 10, text='Timer', fill='white')
        time_text = c.create_text(20, 20, fill='white')

def show_time(time):
        global c
        global time_text
        c.itemconfig(time_text, text=str(time))

def hooked(player, fish):
        global player_id
        global fish_stick
        global window
        global c
        catch_time = time() - 5
        caught = time()-catch_time
        reel_timer = 1
        reel_challenge = int(300/(fish.value*fish.size))
        while caught < 20 and caught > 0:
                caught = time()-catch_time
                show_time(int(caught))
                pos = c.coords(player_id)
                if pos[0] < 0:
                        c.move(player_id, 6, 0)
                if pos[2] > 500:
                        c.move(player_id, -6, 0)
                pos = c.coords(player_id)
                if p_direction is not None:
                        c.coords(player_id, pos[0] + PLAYER_V_X, pos[1] + PLAYER_V_Y, pos[2] + PLAYER_V_X, pos[3] + PLAYER_V_Y, pos[4] + PLAYER_V_X, pos[5] + PLAYER_V_Y)
                if randint(1, reel_challenge) == 1:
                        reel_timer = reel_timer * -1
                c.move(fish_stick, fish.size/5 * reel_timer, 0)
                x1, y1, x2, y2 = c.coords(fish_stick)
                if (x1 < 5):
                        c.move(fish_stick, fish.size/5, 0)
                if (x2 > 495):
                        c.move(fish_stick, -1 * fish.size/5, 0)
                if isinbox(player_id, fish_stick):
                        pass
                else:
                        if fish.value < 1:
                                 catch_time += fish.value*fish.size/500
                        else:
                                catch_time += fish.value*fish.size/1000
                window.update()
                sleep(0.01)
        if caught >= 20:
                return True
        elif caught <= 0:
                return False
