from tkinter import *
import math
import fish
import help_menu
import shop_menu
import inventory_menu
import rod
class player:
    def __init__(self, canvas, player_id, rod):
        self.canvas = canvas
        self.player_id = player_id
        self.PLAYER_V_X = 0
        self.PLAYER_V_Y = 0
        self.player_fish = 0
        self.p_direction = None
        self.angle = 0
        self.line = None
        self.circle = 5
        self.power = None
        self.hook = None
        self.fish_line = None
        self.cash = 0
        self.rod = rod
        self.help_initialized = False
        self.shop_initialized = False
        self.inventory_initialized = False
        self.reverse = False
        self.inventory = list()
        self.inventory.append(self.rod)
    
    def move_up(self):
        self.p_direction = "up"
        self.PLAYER_V_X = 0
        self.PLAYER_V_Y = -2
    def move_down(self):
        self.p_direction = "down"
        self.PLAYER_V_X = 0
        self.PLAYER_V_Y = 2
    def move_left(self):
        self.p_direction = "left"
        self.PLAYER_V_Y = 0
        self.PLAYER_V_X = -2
    def move_right(self):
        self.p_direction = "right"
        self.PLAYER_V_Y = 0
        self.PLAYER_V_X = 2
    def stop(self):
        self.p_direction = None
    def movement(self):
        x, y, w, z = self.canvas.coords(self.player_id)
        if self.p_direction is not None:
                self.canvas.coords(self.player_id, x + self.PLAYER_V_X, y + self.PLAYER_V_Y, w + self.PLAYER_V_X, z + self.PLAYER_V_Y)
    def fish(self):
        if self.player_fish < 4:
            self.player_fish += 1
        else:
            self.player_fish = 0
    def help_menu(self):
        if self.help_initialized != True:
            help_menu.initialize(self)
            self.help_initialized = False
    def shop_menu(self):
        if self.shop_initialized != True:
            shop_menu.initialize(self)
            self.shop_initialized = False
    def inventory_menu(self):
        if self.inventory_initialized != True:
            inventory_menu.initialize(self)
            self.inventory_initialized = False
    def is_fishing(self):
        x, y, w, z = self.canvas.coords(self.player_id)
        if self.player_fish == 0:
                if self.hook != None and self.fish_line != None:
                        self.canvas.delete(self.hook)
                        self.hook = None
                        self.canvas.delete(self.fish_line)
                        self.fish_line = None
        elif self.player_fish == 1:
                if self.line == None:
                    self.line = self.canvas.create_line((x + w)/2, (y + z)/2, (x + w)/2 + math.sin(self.angle), (y + z)/2 + math.cos(self.angle))
                self.canvas.coords(self.line, (x + w)/2, (y + z)/2, (x + w)/2 + math.sin(self.angle/10)*10, (y + z)/2 + math.cos(self.angle/10)*10)
                self.angle += 1
        elif self.player_fish == 2:
                if self.power == None:
                        self.power = self.canvas.create_oval((x + w)/2 - self.circle, (y + z)/2 - self.circle, (x + w)/2 + self.circle, (y + z)/2 + self.circle)
                self.canvas.coords(self.power, (x + w)/2 - self.circle, (y + z)/2 - self.circle, (x + w)/2 + self.circle, (y + z)/2 + self.circle)
                if self.reverse:
                    self.circle -= 1
                else:
                    self.circle += 1
                if self.circle > self.rod.line_length:
                        self.reverse = True
                elif self.circle == 0:
                        self.reverse = False
        elif self.player_fish ==  3:
                if self.hook == None and self.fish_line == None:
                        r = 4
                        self.hook = self.canvas.create_oval((x + w)/2 + math.sin(self.angle/10)*self.circle - 2, (y + z)/2 + math.cos(self.angle/10)*self.circle - 2,\
                                             (x + w)/2 + math.sin(self.angle/10)*self.circle + r - 2, (y + z)/2 + math.cos(self.angle/10)*self.circle + r - 2, fill = self.rod.hook_color)
                        x1, y1, x2, y2 = self.canvas.coords(self.hook)
                        self.fish_line = self.canvas.create_line((x + w)/2, (y + z)/2, (x1 + x2)/2, (y1 + y2)/2, fill = self.rod.line_color)
                self.canvas.delete(self.line)
                self.canvas.delete(self.power)
                self.line = None
                self.power = None
                self.circle = 5
                self.angle = 0
                self.reverse = False
##    #def score():
        
