from tkinter import *
from time import sleep
import player


def initialize(p1):
    global leave
    global window
    window = Tk()
    window.title('help')
    WIDTH = 500
    HEIGHT = 300
    c = Canvas(window, width = WIDTH, height = HEIGHT,bg= '#ADD8E6')
    p1.help_initialized = True
    Font_tuple = ("Comic Sans MS", 10, "bold")
    Font_tuple1 = ("Comic Sans MS", 20, "bold")
    c.create_text(250, 40, \
            text= 'How to play', fill='white', font= Font_tuple1)
    c.create_text(250, 80, \
            text= 'WASD to move', fill='white', font= Font_tuple)
    c.create_text(250, 100, \
            text= 'Press SPACE to launch your hook.', fill='white', font= Font_tuple)
    c.create_text(250, 120, \
            text= 'First press to choose angle, second press to choose power.', fill='white', font= Font_tuple)
    c.create_text(250, 140, \
            text= 'On the third space press, you launch the hook.', fill='white', font= Font_tuple)
    c.create_text(250, 160, \
            text= 'If you feel a bite, press space to reel it in.', fill='white', font= Font_tuple)
    c.create_text(250, 180, \
            text= 'Keep the arrow between the green bar to catch the fish.', fill='white', font= Font_tuple)
    c.create_text(250, 200, \
            text= 'Press G to open up the shop.', fill='white', font= Font_tuple)
    c.create_text(250, 220, \
            text= 'Press I to open up your inventory.', fill='white', font= Font_tuple)
    c.create_text(250, 240, \
            text= 'Have a great time and press H to exit.', fill='white', font= Font_tuple)
    leave = False
    c.bind_all('<KeyPress>', leave_game)
    c.pack()
    main_loop()

def leave_game (event):
    global leave
    global p1
    if event.keysym == 'h':
        window.destroy()
        leave = True

def main_loop():
    global window
    global leave
    while leave != True:
        window.update()
        sleep(0.01)

