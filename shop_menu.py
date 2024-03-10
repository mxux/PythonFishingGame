from tkinter import *
from time import sleep
import player
from rod import *


def initialize(p1):
    global leave
    global window
    global c
    window = Tk()
    window.title('shop')
    WIDTH = 500
    HEIGHT = 800
    c = Canvas(window, width = WIDTH, height = HEIGHT,bg= '#ADD8E6')
    p1.shop_initialized = True
    Font_tuple = ("Comic Sans MS", 10, "bold")
    Font_tuple1 = ("Comic Sans MS", 20, "bold")
    c.create_text(250, 40, \
            text= 'Shop', fill='white', font= Font_tuple1)
    # insert the fishing rods, baits, etc here
    menu_rod = Button(window, text = "Rods", command = lambda : display_rods(p1))
    menu_rod.place(x = 80, y = 80)
    menu_bait = Button(window, text = "Bait", command = None)
    menu_bait.place(x = 230, y = 80)
    menu_booster = Button(window, text = "Boosters", command = None)
    menu_booster.place(x = 380, y = 80)
    leave = False
    c.bind_all('<KeyPress>', leave_game)
    c.pack()
    main_loop()

def leave_game (event):
    global leave
    global p1
    if event.keysym == 'g':
        window.destroy()
        leave = True
def display_rods(p1):
    global rods_for_sale
    global c
    rods_for_sale = list()
    trash = rod("Trash Touch", "Allows you to\nskip the minigame. \n90% of fished items\nwill be trash.", 70, 50, "brown", "brown")
    rods_for_sale.append(trash)
    good = rod("Good", "Slightly better \n than Basic.", 90, 125, "yellow", "purple")
    rods_for_sale.append(good)
    rods_for_sale_buttons = list()
    Font_tuple = ("Comic Sans MS", 8, "bold")
    for i in range(len(rods_for_sale)):
        c.create_text((i+0.5)*130, 140, text = rods_for_sale[i].description, fill = 'white', font = Font_tuple)
        if p1.cash >= rods_for_sale[i].price:
            button = Button(window, text = rods_for_sale[i].name + " : " + str(rods_for_sale[i].price), command = lambda i = i : buy_rod(p1, rods_for_sale[i]))
            button.place(x = (i+0.1)*150, y = 180)
            rods_for_sale_buttons.append(button)
        else:
            button = Button(window, text = "Price " + str(rods_for_sale[i].price) + " : Too Expensive!", command = None)
            button.place(x = (i+0.1)*150, y = 180)
            rods_for_sale_buttons.append(button)
def buy_rod(p1, rod):
    global window
    global leave
    p1.cash -= rod.price
    p1.inventory.append(rod)
    p1.rod = rod
    window.destroy()
    leave = True

def main_loop():
    global window
    global leave
    while leave != True:
        window.update()
        sleep(0.01)

