class Game:
    def __init__ (self, name, price, genre, owned, id, developer, minfo):
        self.name = name
        self.price = price
        self.genre = genre
        self.owned = owned
        self.id = id
        self.developer = developer
        self.minfo = minfo

games = [
    Game("Minecraft", 29.99, "Adventure", False, 0, "Mojang Studios", None),
    Game("Grand Theft Auto V", 59.99, "Action-Adventure", False, 1, "Rockstar Games", "Contains in-app purchases"),
    Game("FIFA", 59.99, "Sports", False, 2, "EA Sports", "Contains in-app purchases"),
    Game("Tetris", 1.99, "Retro", False, 3, "PlayStudios", None),
    Game("Roblox", 0, "Lobby-Game", False, 4, "Roblox Corporation", "Contains in-app purchases"),
    Game("Geometry Dash", 4.99, "Action-Platformer", False, 5, "RobTop Games", "Contains in-app purchases"),
    Game("Among Us", 0.99, "Social-Deduction, Party", False, 6, "Innersloth", "Contains in-app purchases"),
    Game("Snake", 0, "Classic", False, 7, "Nokia", None),
    Game("eFootball", 0, "Sports", False, 8, "KONAMI", "Contains in-app purchases"),
    Game("Fortnite", 0, "3D-Shooter, Battle", False, 9, "Epic Games", "Contains in-app purchases")
]
