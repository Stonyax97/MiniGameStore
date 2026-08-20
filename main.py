#CHANGE LOGS ----------------------------------------------------------------------------------------------------------------------------------------------

# V1.5.1:
    #CHANGE LOGS HAVE MATURED!
#- Replaced the if elif structure for the menu with a smaller one.
#- Added Settings page.
#- Settings options get saved to the json save file. If u have any settings suggestions tell report it in issues.
#- Removed Clear library option (Duplicate of clear save).
#- Renamed some menu options.

#Developper notes:
#- The if elif structure in the main menu was so stupid... At first i knew there was an easier approach, but i couldn't get my hands on it.
#I asked AI for a simpler approach, like... HOW TF DID 7 IF ELIFS GO TO 4 LINES... I understood it and rewrote it here. It's crazy how much these machines are capable of.

#----------------------------------------------------------------------------------------------------------------------------------------------------------

import time as t
import msvcrt as m
import json
from games import games
import os

#VARIABLES ------------------------------------------------------------

library=[]
moneyspent=0
p_loading=True #Set to true by default
selected=0
enter=False

    #TEST DATA:
testonoff=False

    #INFO:
version="1.5.1"

file_path="C:\\Users\\Ziyad\\Desktop\\save.json" #absolute file path

default_data={"library":[], "moneyspent":0, "p_loading":True} #structure of the json file

main_options=["Games", "Buy a game", "Total spent", "Library", "Settings", "Exit"]

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

def clear():
    os.system('cls')

def procced():
    print("Press any key to go back to main menu")
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
            if p_loading==True:
                t.sleep(0.2)
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
            settings_options = [
                "Loading Pauses ------------ " + ONOFF(p_loading),
                "Clear save",
                "Reset Settings",
                "Exit",
                "About"
            ]
            clear()
            print("----------- SETTINGS -----------")
            for i in range(len(settings_options)):
                if i==selected:
                    print(">", settings_options[i])
                else:
                    print(" ", settings_options[i])

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
                choice=selected
                enter=False
                selected=0
            else:
                continue

            if choice==0:
                p_loading=not p_loading

            elif choice==1:
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
                            for i in range(len(library)):
                                for game in games:
                                    if game["Name"]==library[i]:
                                        game["Owned"]=False
                            library=[]
                            with open(file_path, "w") as f1:
                                json.dump(default_data, f1, indent=4)
                            print("Cleared save succesfully!")
                            t.sleep(1.5)
                        else:
                            print("Clearing save cancelled")
                            t.sleep(1.5)

            elif choice==2:
                p_loading=True
                print("Reset settings succesfully")

            elif choice==3:
                break

            elif choice==4:
                clear()
                print("------------ ABOUT ------------")
                print("- Version: ",version)
                print("- Developper: Stonyax97")
                print("- More: https://github.com/Stonyax97/MiniGameStore")
                print("\n\n\n- Licensed under no license ;-;\n")
                print("Press any key to go back to settings")
                m.getch()

        save()
            
    elif choice == 5:
        break

    else:
        raise ValueError

    save()
