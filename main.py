#v1.1 Change Logs: Added error handling and user indication when clearing library
#v1.2 Change Logs: Expanded game library, added versitality for expanding the game library (len(games)), Added Purchase confirmation when buying a free game. Fixed a bug where the library was not being updated when buying a free game.
#V1.2.1 (same release): Fixed bug were free games do not get "owned".
#v1.3 Change logs: Added more information about games. Added msvcrt for user-friendliness. Added confirmation when clearing library. Added brief pause before showing the next game.

import time
import msvcrt

games = [
    {
        "Name": "Minecraft",
        "Price": "29.99$",
        "Genre": "Adventure",
        "Owned": False,
        "ID": 0
    },
    {
        "Name" : "Grand Theft Auto V",
        "Price" : "59.99$",
        "Genre" : "Action-Adventure",
        "Owned" : False,
        "minfo" : "Contains in app-purchases",
        "ID" : 1
    },
    {
        "Name": "FIFA",
        "Price": "59.99$",
        "Genre": "Sports",
        "Owned": False,
        "minfo" : "Contains in app-purchases",
        "ID": 2
    },
    {
        "Name" : "Tetris",
        "Price" : "1.99$",
        "Genre" : "Retro",
        "Owned" : False,
        "ID" : 3
    },
    {
        "Name" : "Roblox",
        "Price" : "FREE",
        "Genre" : "Lobby-Game",
        "Owned" : False,
        "minfo" : "Contains in app-purchases",
        "ID" : 4
    },
    {
        "Name" : "Geometry dash",
        "Price" : "4.99$",
        "Genre" : "Action-Platformer",
        "Owned" : False,
        "minfo" : "Contains in app-purchases",
        "ID" : 5
    },
    {
        "Name" : "Among Us",
        "Price" : "0.99$",
        "Genre" : "Social-Deduction, Party",
        "Owned" : False,
        "minfo" : "Contains in app-purchases",
        "ID" : 6
    },
    {
        "Name" : "Snake",
        "Price" : "FREE",
        "Genre" : "Classic",
        "Owned" : False,
        "ID" : 7
    },
    {
        "Name" : "eFootball",
        "Price" : "FREE",
        "Genre" : "Sports",
        "Owned" : False,
        "minfo" : "Contains in app-purchases",
        "ID" : 8
    },
    {
        "Name" : "Fortnite",
        "Price" : "FREE",
        "Genre" : "3D-Shooter, Battle", 
        "Owned" : False,
        "minfo" : "Contains in app-purchases",
        "ID" : 9
    }
]

def info(gid):
    if "minfo" in games[gid]:
        if games[gid]["Owned"] == False :
            print(f"> {games[gid]["Name"]}\n Price: {games[gid]["Price"]}\n Genre: {games[gid]["Genre"]}\n Owned: Not Owned\n ID: {games[gid]["ID"]}\n *{games[gid]["minfo"]}*")
        else:
            print(f"> {games[gid]["Name"]}\n Price: {games[gid]["Price"]}\n Genre: {games[gid]["Genre"]}\n Owned: Bought\n ID: {games[gid]["ID"]}\n *{games[gid]["minfo"]}*")
    else:
        if games[gid]["Owned"] == False :
            print(f"> {games[gid]["Name"]}\n Price: {games[gid]["Price"]}\n Genre: {games[gid]["Genre"]}\n Owned: Not Owned\n ID: {games[gid]["ID"]}")
        else:
            print(f"> {games[gid]["Name"]}\n Price: {games[gid]["Price"]}\n Genre: {games[gid]["Genre"]}\n Owned: Bought\n ID: {games[gid]["ID"]}")


def procced():
    print("Press any key to go back to main menu...")
    msvcrt.getch()

library=[]
moneyspent=0
    
while True:
    print("1-Show Games")
    print("2-Buy a game")
    print("3-Show total spent")
    print("4-Show library")
    print("5-Clear library")
    print("6-Exit")
    
    try:
        choice=int(input("Choose an option: "))
    
        if choice == 1:
            for banana in range(len(games)):
                info(banana)
                time.sleep(0.2)
            procced()
    
        elif choice == 2:
            try:
                cgtb=int(input("Enter the ID of the desired game to purchase: "))
                if cgtb < len(games):
                    print(f"Purchase {games[cgtb]["Name"]} for {games[cgtb]["Price"]}?(y/N) ")
                    buygame=msvcrt.getch().decode().lower()
                    if buygame == "y":
                        print(f"Purchasing {games[cgtb]["Name"]}...")
                        if games[cgtb]["Price"]=="FREE":
                            moneyspent=moneyspent+0
                        else:
                            moneyspent=moneyspent+float(games[cgtb]["Price"].replace("$", " "))
                            time.sleep(0.5)
                        games[cgtb]["Owned"]=True
                        library.append(games[cgtb]["Name"])
                        print(f"{games[cgtb]["Name"]} Purchased succesfully and Added to library")
                        time.sleep(1.5)
                    else:
                        print(f"Purchase of {games[cgtb]["Name"]} has been cancelled")
                        time.sleep(1)
                else:
                    print("Error: Choose a valid game ID")
                    time.sleep(1.3)
            except ValueError:
                print("Error: Choose a valid game ID")
                time.sleep(1.3)
            
        elif choice == 3:
            print(f"${moneyspent:.2f}")
            procced()
          
        elif choice == 4:
            if library==[]:
                print("         Empty         ")
                procced()
            else:
                print(library)
                procced()
        
        elif choice == 5:
            if library==[]:
                print("Library is already empty")
                time.sleep(1.5)
            else:
                print("Clear library? (y/N)")
                yn=msvcrt.getch().decode().lower()
                if yn=="y":
                    library.clear()
                    print("Library cleared succesfully!")
                    time.sleep(1.5)
                else:
                    print("Clearing library cancelled")
        
        elif choice ==6:
            break
    
        else:
            print("Error: Choose a valid option")
            time.sleep(1.5)
            
    except ValueError:
        print("Error: Choose a valid option")
        time.sleep(1.5)
