#v1.1 Change Logs: Added error handling and user indication when clearing library
#v1.2 Change Logs: Expanded game library, added versitality for expanding the game library (len(games)), Added Purchase confirmation when buying a free game. Fixed a bug where the library was not being updated when buying a free game.
#V1.2.1 (same release): Fixed bug were free games do not get "owned".
#v1.3 Change logs: Added more information about games. Added msvcrt for user-friendliness. Added confirmation when clearing library. Added brief pause before showing the next game (later to be toggled on or off in settings)
#WHAT TO DO NEXT: Buy game in show games menu. save info. new settings page for toggling time pause (very useless but ehh)
#1.3.1 Changelogs: Fixed a bug where the user would be allowed to purchase the game for countless times. Added saving library. Added clearing the save. Improved clearing library (added a pause). Improved some code. Added excepted behavior when clearing an empty save. Fixed a bug where purchasing a free game would not have a pause. Added loading of owned games from save file.
#1.3.2 Changeloges: Added loading library. Fixed a bug where clearing the library won't clear the save. Added saving and loading money spent.

import time
import msvcrt

#CREATING/READING FILES ---------------------------------------------------------------

with open("save.txt", "a") as h:
    pass

with open("money.txt", "a") as file:
    pass

with open("money.txt", "r") as file2:
    whatsinside2=file2.readline()
    if whatsinside2=="":
        with open("money.txt", "w") as file3:
            file3.write("0")
    else:
        pass

with open("money.txt", "r") as file:
    moneyspent=float(file.readline())

#CREATING/READING FILES ---------------------------------------------------------------

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
    print("Press any key to go back to main menu ")
    msvcrt.getch()

#VARIABLES/LISTS -------------------------------------------------------------------

library=[]

#VARIABLES/LISTS -------------------------------------------------------------------

def buy_game():
    global moneyspent
    try:
        cgtb=int(input("Enter the ID of the desired game to purchase: "))
        if cgtb < len(games):
            if games[cgtb]["Owned"]==False:
                print(f"Purchase {games[cgtb]["Name"]} for {games[cgtb]["Price"]}?(y/N) ")
                buygame=msvcrt.getch().decode().lower()
                if buygame == "y":
                    print(f"Purchasing {games[cgtb]["Name"]}...")
                    if games[cgtb]["Price"]=="FREE":
                        time.sleep(0.5)
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
                print("This game has already been purchased")
                time.sleep(1.5)
        else:
            print("Error: Choose a valid game ID")
            time.sleep(1.3)
    except ValueError:
        print("Error: Choose a valid game ID")
        time.sleep(1.3)

#FILE SAVING/READING -------------------------------------------------

def save():
    with open("save.txt", "a") as a:
        for n in range(len(library)):
            a.write(library[n]+"\n")

def savemoney():
    with open("money.txt", "w") as file:
        file.write(str(moneyspent))  #WORKS

with open("save.txt", "r") as file:
    length=file.readlines()
    file.seek(0)
    for p in range(len(length)):
        game=file.readline()
        for q in range(len(games)):
            if game.strip()==games[q]["Name"]:
                games[q]["Owned"]=True
            else:
                pass

with open("save.txt", "r") as load:
    library=load.readlines()
for i in range(len(library)):
    library[i]=library[i].strip()

#FILE SAVING/READING -------------------------------------------------

while True:
    print("1-Show Games")
    print("2-Buy a game")
    print("3-Show total spent")
    print("4-Show library")
    print("5-Clear library")
    print("6-Save (ONLY WHEN EXITING)")
    print("7-Clear save")
    print("8-Exit")
    
    try:
        choice=int(input("Choose an option: "))
    
        if choice == 1:
            for banana in range(len(games)):
                info(banana)
                time.sleep(0.2)
            procced()
    
        elif choice == 2:
            buy_game()
            
        elif choice == 3:
            print(f"${moneyspent:.2f}")
            procced()
          
        elif choice == 4:
            if library==[]:
                print("['----------Empty----------']")
                procced()
            else:
                print(library)
                procced()
        
        elif choice == 5:
            if library==[]:
                print("Library is already empty")
                time.sleep(1.5)
            else:
                print("Clear library? (y/N): ")
                yn=msvcrt.getch().decode().lower()
                if yn=="y":
                    library.clear()
                    with open("save.txt", "w") as file:
                        file.write("")
                    print("Library cleared succesfully!")
                    time.sleep(1.5)
                else:
                    print("Clearing library cancelled")
                    time.sleep(1.5)
        
        elif choice ==6:
            print("PLEASE ONLY DO THIS AT THE END OF YOUR SESSION\n")
            savingchoice=input("Procced to save? (y/N): ").lower()
            if savingchoice=="y":
                save()
                savemoney()
                print("Library has been succesfully saved")
                time.sleep(1.5)
            else:
                print("Saving canceled")
                time.sleep(1.5)

        elif choice == 7:
            with open ("save.txt","r") as isfilempty:
                whatsinside=isfilempty.read()
            if whatsinside=='':
                print("Save is already empty")
                time.sleep(1.5)
            else:
                clearchoice=input("Clear save? (y/N): ").lower()
                if clearchoice=="y":
                    print("Clearing save...")
                    time.sleep(0.4)
                    library=[]
                    with open ("save.txt", "w") as clearfile:
                        clearfile.write("")
                    print(f"Cleared {len(library)} games succesfully")
                    time.sleep(1.5)
                else:
                    print("Clearing file has been canceled")
                    time.sleep(1.2)

        elif choice ==8:
            break
    
        else:
            print("Error: Choose a valid option")
            time.sleep(1.5)
            
    except ValueError:
        print("Error: Choose a valid option")
        time.sleep(1.5)
