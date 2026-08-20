#CHANGE LOGS --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#v1.1 Change Logs: Added error handling and user indication when clearing library
#v1.2 Change Logs: Expanded game library, added versitality for expanding the game library (len(games)), Added Purchase confirmation when buying a free game. Fixed a bug where the library was not being updated when buying a free game.
#V1.2.1 (same release): Fixed bug were free games do not get "owned".
#v1.3 Change logs: Added more information about games. Added msvcrt for user-friendliness. Added confirmation when clearing library. Added brief pause before showing the next game (later to be toggled on or off in settings)
#WHAT TO DO NEXT: Buy game in show games menu. new settings page for toggling time pause (very useless but ehh)
#1.3.1 Changelogs: Fixed a bug where the user would be allowed to purchase the game for countless times. Added saving library. Added clearing the save. Improved clearing library (added a pause). Improved some code. Added excepted behavior when clearing an empty save. Fixed a bug where purchasing a free game would not have a pause. Added loading of owned games from save file.
#1.3.2 Changeloges: Added loading library. Fixed a bug where clearing the library won't clear the save. Added saving and loading money spent.
#v1.4: Various code improvements for easier reading and unified some values. Removed .txt file saving. Added json file saving and loading. Added guidlines for each part for ease of readablity. Added auto saving. Added moneyspent clearing. Added clearing save. Fixed a bug where clearing the library and buying the games that were cleared would not be allowed as the systeme still thinks the games are owned.
#V1.4 split version: splitting the projecti into 2 (for fun :)).... After further inspection it feels like im gonna acc split it for real. Split the project into 2 parts. one with the games library and one with all the code and changelogs. made the alias of time as t for easier typing (too lazy to add 3 caracters)
#V1.4.1 = V1.4 split version.
#V1.5: Removed the old input menu for a brand new terminal like experience! Constructing a setting page. Fixed a bug where clearning the library would show the user the save file structure. #SETTINGS DO NOT WORK YET... PLEASE WAIT FOR STABLE 1.5.1
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

import time as t
import msvcrt as m
import json
from games import games
import os

#VARIABLES ------------------------------------------------------------

library=[]
moneyspent=0
file_path="C:\\Users\\Ziyad\\Desktop\\save.json" #absolute file path
default_data={"library":[], "moneyspent":0, "p_loading":True} #structure of the json file

p_loading=True #Set to true by default

selected=0
enter=False

options=["Show games", "Buy a game", "Show total spent", "Show library", "Clear library", "Clear save", "Settings", "Exit"]

#----------------------------------------------------------------------


#FILE READING -------------------------------------------------

    #CREATING SAVE FILE -------
with open(file_path, "a") as file:
    pass

    #CHECK FILE COMPONENTS ------
with open(file_path, "r") as file:
    components=file.readline()

    #CREATING FILE STRUCTURE ------
    if components=="":
        with open(file_path, "w") as f1:
            json.dump(default_data, f1, indent=4)
        


    #RUN FILE READING -----------
with open(file_path, "r") as file:

        #UPDATING LIBRARY AND MONEYSPENT AND SETTINGS ----------
    data=json.load(file)
    library=data["library"]
    moneyspent=data["moneyspent"]
    p_loading=data["p_loading"]


        #UPDATING GAMES["OWNED"] ---------
    for i in range(len(data['library'])): 
        for game in games:
            if game["Name"]==data["library"][i]: #the current dict's the one being checked
                game["Owned"]=True

#FUNCTIONS------------------------------------------------------------------

def save(): #FILE SAVING ------
    data["library"]=library
    data["moneyspent"]=moneyspent
    data["p_loading"]=p_loading
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)


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

def settings():
    print("----------- SETTINGS -----------")
    t.sleep(0.5)
    print(">"+" Game store")
    print("Coming soon")
    global selected

    for i in range(10):
        uk=m.getch()
        if uk==b'\xe0':
            key=m.getch()
            if key==b'H':
                selected+=1
            elif key==b'P':
                selected-=1
                os.system('cls')
                print("Game store")
                print(">"+" Coming soon")

        t.sleep(2)

def clear():
    os.system('cls')

def procced():
    print("Press any key to go back to main menu")
    m.getch()

def clear_ownedvalue():
    for i in range(len(library)):
        for game in games:
            if game["Name"]==library[i]:
                game["Owned"]=False

#BUYING GAME ----------------------------------------------------------------------------------------------------------

def buy_game():
    global moneyspent
    try:
        cgtb=int(input("Enter the ID of the desired game to purchase: "))
        if cgtb < len(games):
            if games[cgtb]["Owned"]==False:
                print(f"Purchase {games[cgtb]["Name"]} for {games[cgtb]["Price"]}?(y/N) ")
                buygame=m.getch().decode().lower()
                if buygame == "y":
                    print(f"Purchasing {games[cgtb]["Name"]}...")
                    if games[cgtb]["Price"]=="FREE":
                        t.sleep(0.5)
                    else:
                        moneyspent=moneyspent+float(games[cgtb]["Price"].replace("$", " "))
                        t.sleep(0.5)
                    games[cgtb]["Owned"]=True
                    library.append(games[cgtb]["Name"])
                    print(f"{games[cgtb]["Name"]} Purchased succesfully and Added to library")
                    t.sleep(1.5)
                else:
                    print(f"Purchase of {games[cgtb]["Name"]} has been cancelled")
                    t.sleep(1)
            else:
                print("This game has already been purchased")
                t.sleep(1.5)
        else:
            print("Error: Choose a valid game ID")
            t.sleep(1.3)
    except ValueError:
        print("Error: Choose a valid game ID")
        t.sleep(1.3)

#----------------------------------------------------------------------------------------------------------------------


#MAIN LOOP ------------------------------------------------------------------------------------------------------------

while True:
    clear()
    if selected==0:
        print("> ",options[selected])
        for i in range(1,8):
            print(options[i])

    elif selected==1:
            print(options[0])
            print("> ",options[selected])
            for i in range(2,8):
                print(options[i])

    elif selected==2:
        for i in range(2):
            print(options[i])
        print("> ",options[selected])
        for i in range (3,8):
            print(options[i])

    elif selected==3:
        for i in range(3):
            print(options[i])
        print("> ",options[selected])
        for i in range (4,8):
            print(options[i])

    elif selected==4:
        for i in range(4):
            print(options[i])
        print("> ",options[selected])
        for i in range (5,8):
            print(options[i])

    elif selected==5:
        for i in range(5):
            print(options[i])
        print("> ",options[selected])
        for i in range (6,8):
            print(options[i])

    elif selected==6:
        for i in range(6):
            print(options[i])
        print("> ",options[selected])
        for i in range (7,8):
            print(options[i])

    elif selected==7:
        for i in range(7):
            print(options[i])
        print("> ",options[selected])

    uc=m.getch()
    if uc==b'\r':
        enter=True
    elif uc==b'\xe0':
        key=m.getch()
        if key==b'H': #up key
            if selected>0:
                selected-=1

        elif key==b'P': #down key
            if selected<(len(options)-1):
                selected+=1

    if enter==True:
        choice=selected
        enter=False
        selected=0
        pass
    else:
        continue

    if choice == 0:
        for banana in range(len(games)):
            info(banana)
            if p_loading==True:
                t.sleep(0.2)
            else:
                pass
        procced()

    elif choice == 1:
        buy_game()
        
    elif choice == 2:
        print(f"${moneyspent:.2f}")
        procced()
        
    elif choice == 3:
        if library==[]:
            print("['----------Empty----------']")
            procced()
        else:
            print(library)
            procced()
    
    elif choice == 4:
        if library==[]:
            print("Library is already empty")
            t.sleep(1.5)
        else:
            print("Clear library? (y/N): ")
            yn=m.getch().decode().lower()
            if yn=="y":
                clear_ownedvalue()
                library.clear()
                print("Library cleared succesfully!")
                t.sleep(0.8)
                print("Clear moneyspent too? (y/N) ")
                yn=m.getch().decode().lower()
                if yn=="y":
                    moneyspent=0
                    print("Moneyspent cleared succesfully!")
                else:
                    print("*Clearing moneyspent ignored*")
                t.sleep(1.5)
            else:
                print("Clearing library cancelled")
                t.sleep(1.5)
    
    elif choice == 5:
        with open(file_path, "r") as file:
            checkdata=json.load(file)
            if checkdata==default_data:
                print("Save is already empty")
                t.sleep(1.5)
            else:
                print("Clear save? (y/N): ")
                yn=m.getch().decode().lower()
                if yn=="y":
                    moneyspent=0
                    clear_ownedvalue()
                    library=[]
                    with open(file_path, "w") as f1:
                        json.dump(default_data, f1, indent=4)
                    print("Cleared save succesfully!")
                    t.sleep(1.5)
                else:
                    print("Clearing save cancelled")
                    t.sleep(1.5)

    elif choice == 6:
        settings()

    elif choice == 7:
        break

    else:
        raise ValueError

save()
