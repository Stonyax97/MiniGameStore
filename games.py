import time as t
import os
import json

minfostr="Contains in-app purchases"
file_path=os.path.join(os.path.dirname(__file__), "save.json")
class Game:
    def __init__ (self, name, price, genre, owned, id, developer, minfo, purchase_time):
        self.name = name
        self.price = price
        self.genre = genre
        self.owned = owned
        self.id = id
        self.developer = developer
        self.minfo = minfo
        self.purchase_time = purchase_time

    def timer(self):
        self.purchase_time=t.time()
        with open(file_path, "r") as file:
            data=json.load(file)
            data["purchase_times"].append({"name":self.name,"time_stamp":self.purchase_time})
        with open(file_path, "w") as file:
            json.dump(data, file)

#before this i tried opening this in "a+" IT WAS A PAIN 2 seek(0)'s and someother things ;-, why python why
#guess what... it wasn't just this. i hade confused self.purchasetime with self.purchase_time and used them both
#which was crazy... i just couldn't spot it
#even crazier... even when it saved... the other save func was lit rewriting the written file.... UGHHH
#yeah i couldn't figure that out on my own i gave it to chatgpt and he told me that it gets rewritten.
#soooo i just load the file before saving :) 

games = [
    Game("Minecraft", 29.99, "Adventure", False, 0, "Mojang Studios", None, None),
    Game("Grand Theft Auto V", 59.99, "Action-Adventure", False, 1, "Rockstar Games", minfostr, None),
    Game("FIFA", 59.99, "Sports", False, 2, "EA Sports", minfostr, None),
    Game("Tetris", 1.99, "Retro", False, 3, "PlayStudios", None, None),
    Game("Roblox", 0, "Lobby-Game", False, 4, "Roblox Corporation", minfostr, None),
    Game("Geometry Dash", 4.99, "Action-Platformer", False, 5, "RobTop Games", minfostr, None),
    Game("Among Us", 0.99, "Social-Deduction, Party", False, 6, "Innersloth", minfostr, None),
    Game("Snake", 0, "Classic", False, 7, "Nokia", None, None),
    Game("eFootball", 0, "Sports", False, 8, "KONAMI", minfostr, None),
    Game("Fortnite", 0, "3D-Shooter, Battle", False, 9, "Epic Games", minfostr, None)
]
