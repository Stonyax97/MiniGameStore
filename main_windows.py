#CHANGE LOGS ----------------------------------------------------------------------------------------------------------------------------------------------

# V1.6:

#- WINDOWS ONLY VERSION
#- Fixed a bug where entering a string in buy a game caushes a crash.
#- Implemented classes! (For now only data methods coming later).
#- Added a divider in the store (Can be changed in setttings)
#- You can now customize loading time in the game menu!
#- A lot of code improvements here and there!
#- FOR LATER: ADD BALANCE AND RESTORE PURCHASES!

#----------------------------------------------------------------------------------------------------------------------------------------------------------

import msvcrt as m
import time as t
import json
import os

from games import Game, games

#VARIABLES ------------------------------------------------------------

library=[]
moneyspent=0
wt=1.5 #this is the wait time when getting a text before it goes back to the menu
loading_time=0.2 #Set to 0.2 by default
loading=True #Set to true by default
divider=True #Set to true by default
selected=0
enter=False

    #TEST DATA:
testonoff=False

    #INFO:
version="1.6  Windows"

file_path=os.path.join(os.path.dirname(__file__), "save.json") #now the fie will be created where this .py file is executed.

default_data={"library":[], "moneyspent":0, "loading":True, "divider":True, "loading_time":loading_time} #structure of the json file

main_options=["Games", "Buy a game", "Total spent", "Library", "Settings", "Exit"]

#----------------------------------------------------------------------


#FILE READING -------------------------------------------------

    #CREATING FILE STRUCTURE ------
if not os.path.isfile(file_path): #if it doesn't exist
    with open(file_path, "w") as f1:
        json.dump(default_data, f1, indent=4)

    #UPDATING VARIABLES AND SETTINGS ----------
with open(file_path, "r") as file:
    data=json.load(file)
    library=data["library"]
    moneyspent=data["moneyspent"]
    loading=data["loading"]
    divider=data["divider"]
    loading_time=data["loading_time"]

        #UPDATING GAMES.OWNED ---------
    for i in range(len(data['library'])): 
        for game in games:
            if game.name==data["library"][i]:
                game.owned=True

#FUNCTIONS------------------------------------------------------------------

def save(): #FILE SAVING ------
    data["library"]=library
    data["moneyspent"]=moneyspent
    data["loading"]=loading
    data["divider"]=divider
    data["loading_time"]=loading_time
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

def info(gid):
    print(f"{"\n" if divider==False else "-"*40}\n> {games[gid].name}\n Price: {"FREE" if games[gid].price==0 else f"${games[gid].price:.2f}"}\n Genre: {games[gid].genre}\n Owned: {"Not Owned" if games[gid].owned==False else "Bought"}\n ID: {games[gid].id}\n Developer: {games[gid].developer}{f"\n*{games[gid].minfo}*" if games[gid].minfo is not None else ""}")

def clear():
    os.system('cls')

def procced():
    print("Press any key to return")
    m.getch()

def ONOFF(setting):
    if setting==True:
        return "ON"
    else:
        return "OFF"

assert ONOFF(testonoff)=="OFF"

#BUYING GAME ----------------------------------------------------------------------------------------------------------

def buy_game():
    global moneyspent
    try:
        cgtb=int(input("Enter the ID of the desired game to purchase: "))
    except ValueError:
        print("Choose a valid Game ID")
        t.sleep(wt)
        return

    if cgtb >= len(games) or cgtb < 0:
        print("Choose a valid Game ID")
        t.sleep(wt)
        return
        
    if games[cgtb].owned==True:
        print(f"{games[cgtb].name} has already been purchased")
        t.sleep(wt)
        return

    else:
        print(f"Purchase {games[cgtb].name} for {games[cgtb].price}?(y/N) ")
        buygame=m.getch().decode().lower()
        if buygame != "y":
            print(f"Purchase of {games[cgtb].name} has been cancelled")
            t.sleep(wt)
        else:
            print(f"Purchasing {games[cgtb].name}...")
            if games[cgtb].price==0:
                t.sleep(0.5)
            else:
                moneyspent+=float(games[cgtb].price)
                t.sleep(0.5)
            games[cgtb].owned=True
            library.append(games[cgtb].name)
            print(f"{games[cgtb].name} Purchased succesfully and Added to library")
            t.sleep(wt)
    

#----------------------------------------------------------------------------------------------------------------------


#MAIN LOOP ------------------------------------------------------------------------------------------------------------

while True:
    clear()
    for i in range(len(main_options)):
        if i == selected:
            print("> ", main_options[i])
        else:
            print(" ", main_options[i])

    uc=m.getch()
    if uc==b'\r':
        enter=True
    elif uc==b'\xe0':
        key=m.getch()
        if key==b'H': #up key
            if selected>0:
                selected-=1

        elif key==b'P': #down key
            if selected<(len(main_options)-1):
                selected+=1

    if enter==True:
        choice=selected
        enter=False
        selected=0
    else:
        continue

    if choice == 0:
        for banana in range(len(games)):
            info(banana)
            if loading==True:
                t.sleep(loading_time)
        print("\n")
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
        while True:
            settings_options = [{"name":"Loading Pauses ------------ " + ONOFF(loading), "id":0}]

            if loading:
                settings_options.append({"name":f"Customize loading time ---- {loading_time}", "id":1})

            settings_options += [
                {"name": "Divider -------------------- " + ONOFF(divider), "id":2},
                {"name": "Clear save", "id":3},
                {"name":"Reset Settings", "id":4},
                {"name":"Exit", "id" :5},
                {"name":"About", "id":6}
                ]
            
            clear()
            print("----------- SETTINGS -----------")
            for i in range(len(settings_options)):
                if i==selected:
                    print(">", settings_options[i]["name"])
                else:
                    print(" ", settings_options[i]["name"])

            uc=m.getch()
            if uc==b'\r':
                enter=True
            elif uc==b'\xe0':
                key=m.getch()
                if key==b'H': #up
                    if selected>0:
                        selected-=1
                elif key==b'P': #down
                    if selected<(len(settings_options)-1):
                        selected+=1

            if enter==True:
                choice=settings_options[selected]["id"]
                enter=False
                selected=0
            else:
                continue

            if choice==0:
                loading=not loading
                save()

    
            elif choice==1:
                try:
                    loading_time=float(input("Enter the new loading time (in seconds): "))
                    save()
                except ValueError:
                    print("Choose a valid time")
                    t.sleep(wt)

            elif choice==2:
                divider=not divider
                save()

            elif choice==3:
                with open(file_path, "r") as file:
                    checkdata=json.load(file)
                    if checkdata==default_data:
                        print("Save is already empty")
                        t.sleep(wt)
                    else:
                        print("Clear save? (y/N): ")
                        yn=m.getch().decode().lower()
                        if yn!="y":
                            print("Clearing save cancelled")
                            t.sleep(wt)
                        else:
                            moneyspent=0
                            for i in range(len(library)):
                                for game in games:
                                    if game.name==library[i]:
                                        game.owned=False
                            library=[]
                            with open(file_path, "w") as f1:
                                json.dump(default_data, f1, indent=4)
                            print("Cleared save succesfully!")
                            t.sleep(wt)

            elif choice==4:
                loading=True
                divider=True
                loading_time=0.2
                print("Reset settings succesfully")
                t.sleep(wt)
                save()

            elif choice==5:
                break

            elif choice==6:
                clear()
                print("------------ ABOUT ------------")
                print("- Version: ",version)
                print("- Developper: Stonyax97")
                print("- More: https://github.com/Stonyax97/MiniGameStore")
                print("- Requires Windows and Python 3.13 or later.")
                print("\n\n\n- Licensed under no license ;-;\n")
                print("Press any key to return")
                m.getch()
            
    elif choice == 5:
        break

    else:
        raise ValueError

    save()
