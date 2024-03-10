from tkinter import *
from time import sleep
import player
from rod import *


def initialize(p1):
    global leave
    global window
    global c
    window = Tk()
    window.title('inventory')
    WIDTH = 300
    HEIGHT = 600
    c = Canvas(window, width = WIDTH, height = HEIGHT,bg= '#ADD8E6')
    p1.inventory_initialized = True
    Font_tuple = ("Comic Sans MS", 20, "bold")
    c.create_text(150, 40, \
            text= 'Inventory', fill='white', font= Font_tuple)
    display_inventory(p1)
    leave = False
    c.bind_all('<KeyPress>', leave_game)
    c.pack()
    main_loop()

def leave_game (event):
    global leave
    global p1
    if event.keysym == 'i':
        window.destroy()
        leave = True
def display_inventory(p1):
    global c
    normal_font = ("Comic Sans MS", 10, "bold")
    small_font = ("Comic Sans MS", 8, "bold")
    c.create_text(50, 70, \
            text= 'Name', fill='white', font= normal_font)
    c.create_text(150, 70, \
            text= 'Description', fill='white', font= normal_font)
    
    for i in range(len(p1.inventory)):
        c.create_text(50, 90 + i*50, text = p1.inventory[i].name, fill = 'white', font = small_font)
        c.create_text(150, 100 + i*50, text = p1.inventory[i].description, fill = 'white', font = small_font)
        if p1.inventory[i] != p1.rod:
            button = Button(window, text = "Equip", command = lambda i = i : equip_rod(p1, p1.inventory[i]))
            button.place(x = 220, y = 90+i*50)
        else:
            button = Button(window, text = "Equipped", command = None)
            button.place(x = 220, y = 90+i*50)

def equip_rod(p1, rod):
    global window
    global leave
    p1.rod = rod
    window.destroy()
    leave = True

def main_loop():
    global window
    global leave
    while leave != True:
        window.update()
        sleep(0.01)

