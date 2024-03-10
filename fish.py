from tkinter import *
from random import randint
import math
import player
import hooked
class fish:
    def __init__(self, canvas, fish_id):
        #canvas, location, color, size/point value, etc
        self.canvas = canvas
        self.fish_id = fish_id
        x1, y1, x2, y2 = self.canvas.coords(self.fish_id)
        self.size = abs(x2-x1)
        self.movement_timer = 0
        self.vector_x = randint(-1, 1)/2
        self.vector_y = randint(-1, 1)/2
        self.hooked = False
        self.dip = 0
        self.caught = False
        self.value = 1
        self.type = ""
    def check_bounds(self):
        x1, y1, x2, y2 = self.canvas.coords(self.fish_id)
        if x1 < 0:
            self.vector_x = 2
        if x2 > 500:
            self.vector_x = -2
        if y1 < 0:
            self.vector_y = 2
        if y2 > 800:
            self.vector_y = -2

    def move_fish(self, player, universal_hooked):
        self.check_bounds()
        if self.movement_timer < 100:
            self.canvas.move(self.fish_id, self.vector_x, self.vector_y)
            self.movement_timer += 1
        else:
            self.vector_x += randint(-1, 1)/2
            self.vector_y += randint(-1, 1)/2
            if abs(self.vector_x) >= 2:
                self.vector_x = 0
            if abs(self.vector_y) >= 2:
                self.vector_y = 0
            self.movement_timer = 0
        if player.hook != None:
            x1, y1, x2, y2 = player.canvas.coords(player.hook)
            hook_x = (x1 + x2)/2
            hook_y = (y1 + y2)/2
            x3, y3, x4, y4 = self.canvas.coords(self.fish_id)
            fish_x = (x3 + x4)/2
            fish_y = (y3 + y4)/2
            
            if math.sqrt((hook_x - fish_x)**2 + (hook_y - fish_y)**2) < 50 and universal_hooked != True:
                self.hooked = True
                
    def move_hooked_fish(self, player):
            if player.hook != None:
                x1, y1, x2, y2 = player.canvas.coords(player.hook)
                hook_x = (x1 + x2)/2
                hook_y = (y1 + y2)/2
                x3, y3, x4, y4 = self.canvas.coords(self.fish_id)
                fish_x = (x3 + x4)/2
                fish_y = (y3 + y4)/2
                if self.dip < 200:
                    self.canvas.move(self.fish_id, (hook_x - fish_x)/100, (hook_y - fish_y)/100)
                    self.dip += 1
                elif 200 <= self.dip < 400:
                    self.canvas.move(self.fish_id, (fish_x - hook_x)/100, (fish_y - hook_y)/100)
                    self.dip += 1
                else:
                    self.dip = 0
                x3, y3, x4, y4 = self.canvas.coords(self.fish_id)
                fish_x = (x3 + x4)/2
                fish_y = (y3 + y4)/2
                if math.sqrt((hook_x - fish_x)**2 + (hook_y - fish_y)**2) <= 10:
                    if player.player_fish == 4:
                        if player.rod.name != "Trash Touch":
                            win = hooked.initialize(player, self)
                            if win == True:
                                player.cash += self.size * self.value
                                print("You caught a " + str(self.size) + " inch long " + self.type)
                        else:
                            if randint(1, 10) == 10:
                                player.cash += self.size * self.value
                                print("You caught a " + str(self.size) + " inch long " + self.type)
                            else:
                                player.cash += self.size * self.value/10
                                print("Your Trash Touch rod turned the fish into an amogus collectible. It's trash! You suck!")
                        self.caught = True
                        self.hooked = False
                        player.player_fish = 0
                else:
                    if player.player_fish == 4:
                        player.player_fish = 0
            elif player.hook == None:
                self.hooked = False



class Bass(fish):
    def __init__(self, canvas, fish_id):
        super().__init__(canvas, fish_id)
        self.value = 0.5
        self.type = "Bass"
class Trout(fish):
    def __init__(self, canvas, fish_id):
        super().__init__(canvas, fish_id)
        self.value = 0.8
        self.type = "Trout"
class Salmon(fish):
    def __init__(self, canvas, fish_id):
        super().__init__(canvas, fish_id)
        self.value = 1
        self.type = "Salmon"
class RedSnapper(fish):
    def __init__(self, canvas, fish_id):
        super().__init__(canvas, fish_id)
        self.value = 1.5
        self.type = "Red Snapper"
class UltraRareGoldenFish(fish):
    def __init__(self, canvas, fish_id):
        super().__init__(canvas, fish_id)
        self.value = 5
        self.type = "Ultra Rare Golden Fish"
