#CHANGE LOGS ----------------------------------------------------------------------------------------------------------------------------------------------

version="1.7 Portable"
#- Added a balance system and restore purchases!
#- Added support for empty or corrupted JSON files.
#- Added preserving cursor position option.
#- Added a new Userspace! You can now see your balance, moneyspent (since the start of the session), money restored, games owned, and your library! All in one place!
#- Various code improvements.

#----------------------------------------------------------------------------------------------------------------------------------------------------------

import time as t
import json
import os
from games import Game, games

#VARIABLES ------------------------------------------------------------

#VARIABLES ------------------------------------------------------------

    #USER DATA --------
library=[]
moneyspent=0
money_restored=0
games_owned=0
balance=100 #if u want more get a job

wt=1.5 #this is the wait time when getting a text before it goes back to the menu

    #SETTINGS VARIABLES --------
loading_time=0.2 #Set to 0.2 by default
loading=True #Set to true by default
divider=True #Set to true by default
preserve_cursor=True #Set to true by default (yo ik everything is set to true but hey all these features are lwk W)

    #TEST DATA:
testonoff=False

file_path=os.path.join(os.path.dirname(__file__), "save.json") #now the fie will be created where this .py file is executed.

default_data={"library":[], "moneyspent":0, "balance": 100, "money_restored": money_restored, "loading":True, "divider":True, "loading_time":loading_time, "preserve_cursor":True, "purchase_times":[]} #structure of the json file

main_options=["1-Games", "2-Buy a game", "3-Restore purchase", "4-User space", "5-Settings", "6-Exit"]

#----------------------------------------------------------------------


#FILE READING -------------------------------------------------

    #CREATING FILE STRUCTURE ------
if not os.path.isfile(file_path) or os.path.getsize(file_path)==0: #if it doesn't exist OR is empty
    with open(file_path, "w") as file:
        json.dump(default_data, file, indent=4)

    #CHECKING FOR CORRUPTED FILE -------
with open(file_path, "r") as file:
    try:
        json.load(file)
    except json.JSONDecodeError:
        print("File is corrupted... Formating file.")
        with open (file_path, "w") as file:
            json.dump(default_data, file, indent=4)
        t.sleep(wt)

    #UPDATING VARIABLES AND SETTINGS ----------
with open(file_path, "r") as file:
    data=json.load(file)
    library=data["library"]
    moneyspent=data["moneyspent"]
    loading=data["loading"]
    divider=data["divider"]
    loading_time=data["loading_time"]
    balance=data["balance"]
    preserve_cursor=data["preserve_cursor"]
    money_restored=data["money_restored"]

        #UPDATING GAMES.OWNED ---------
    for i in range(len(data['library'])): 
        for game in games:
            if game.name==data["library"][i]:
                game.owned=True

#FUNCTIONS------------------------------------------------------------------

def save(): #FILE SAVING ------
    with open(file_path, "r") as file:
        data = json.load(file) #loading the file so that the other games.py can write and not get rewritten by this save func

    data["library"]=library
    data["moneyspent"]=moneyspent
    data["loading"]=loading
    data["divider"]=divider
    data["loading_time"]=loading_time
    data["balance"]=balance
    data["preserve_cursor"]=preserve_cursor
    data["money_restored"]=money_restored
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

def info(gid):
    print(f"{"\n" if divider==False else "-"*40}\n> {games[gid].name}\n Price: {"FREE" if games[gid].price==0 else f"${games[gid].price:.2f}"}\n Genre: {games[gid].genre}\n Owned: {"Not Owned" if games[gid].owned==False else "Bought"}\n ID: {games[gid].id}\n Developer: {games[gid].developer}{f"\n*{games[gid].minfo}*" if games[gid].minfo is not None else ""}")

def clear():
    try:
        os.system('cls')
    except:
        os.system('clear')

def procced():
    input("Press Enter to return: ")

def ONOFF(setting):
    if setting==True:
        return "ON"
    else:
        return "OFF"

assert ONOFF(testonoff)=="OFF"

#PURCHASES ----------------------------------------------------------------------------------------------------------

def buy_game():
    global moneyspent
    global balance
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

    if balance<games[cgtb].price:
        print("Get a job to get more money")
        t.sleep(wt)
        return

    else:
        buygame=input(f"Purchase {games[cgtb].name} for {"FREE" if games[cgtb].price==0 else games[cgtb].price}?(y/N): ").lower()
        if buygame != "y":
            print(f"Purchase of {games[cgtb].name} has been cancelled")
            t.sleep(wt)
        else:
            print(f"Purchasing {games[cgtb].name}...")
            if games[cgtb].price==0:
                t.sleep(0.5)
            else:
                moneyspent+=float(games[cgtb].price)
                balance-=float(games[cgtb].price)
                t.sleep(0.5)
            games[cgtb].owned=True
            library.append(games[cgtb].name)
            games[cgtb].timer()
            print(f"{games[cgtb].name} Purchased succesfully and Added to library")
            t.sleep(wt)

def restore():
    global moneyspent
    global balance
    global money_restored
    try:
        cgtr=int(input("Enter the ID of the desired game to restore its purchase: "))
    except ValueError:
        print("Choose a valid Game ID")
        t.sleep(wt)
        return

    if cgtr >= len(games) or cgtr < 0:
        print("Choose a valid Game ID")
        t.sleep(wt)
        return

    if games[cgtr].owned==False:
        print(f"You do not own {games[cgtr].name}")
        t.sleep(wt)
        return
    
    if games[cgtr].price==0:
        print("You cannot restore the purchase of a free game.")
        t.sleep(wt)
        return

    if balance>100:
        print("yo bro why are u changing code")
        t.sleep(wt)
        return

    with open(file_path, "r") as file:
        data=json.load(file)
    purchase_times=data["purchase_times"]
    for i in range(len(purchase_times)):
        for purchase_time in purchase_times:
            if purchase_time["name"]==games[cgtr].name:
                time_stamp=purchase_time["time_stamp"]
                elapsed=t.time()-time_stamp

    else:
        yn=input(f"Restore purchase of {games[cgtr].name} and get {games[cgtr].price/2 if elapsed>7200 else games[cgtr].price}?(y/N): ")
        toaddinbalance=games[cgtr].price/2 if elapsed>7200 else games[cgtr].price
        if yn != "y":
            print(f"Restore purchase of {games[cgtr].name} has been cancelled")
            t.sleep(wt)
        else:
            print(f"Restoring {games[cgtr].name}...")
            balance+=float(toaddinbalance)
            money_restored+=float(toaddinbalance)
            games[cgtr].owned=False
            library.remove(games[cgtr].name)
            t.sleep(0.5)
            print(f"Restored purchase of {games[cgtr].name}. ${toaddinbalance:.2f} added to your balance.")
            t.sleep(wt+0.5)

#----------------------------------------------------------------------------------------------------------------------


#MAIN LOOP ------------------------------------------------------------------------------------------------------------

while True:
    clear()
    for banana in range(len(main_options)):
        print(main_options[banana])
    try:
        choice=int(input("Choose an option: "))
    except ValueError:
        print("Choose a valid option")
        t.sleep(wt)
        continue
    
    if choice == 1:
        for banana in range(len(games)):
            info(banana)
            if loading==True:
                t.sleep(loading_time)
        procced()

    elif choice == 2:
        buy_game()

    elif choice == 3:
        restore()

    elif choice == 4:
        games_owned=len(library)
        print("---------- USER SPACE ----------")
        print(f"- Balance: ${balance:.2f}")
        print(f"- Money spent: ${moneyspent:.2f}")
        print(f"- Money restored: ${money_restored:.2f}")
        print(f"- Games owned: {games_owned}")
        print("\n- Library:")
        if library==[]:
            print("---------- Empty ----------")
        else:
            for i in range(len(library)):
                print(f" -{library[i]}")
        procced()
        
    elif choice == 5:
        while True:
            settings_options = [{"name":"1-Loading Pauses ------------ " + ONOFF(loading), "id":0}]

            if loading:
                settings_options.append({"name":f"2-Customize loading time ---- {loading_time}", "id":1})

            settings_options += [
                {"name":"3-Preserve cursor position--- " + ONOFF(preserve_cursor), "id":2},
                {"name":"4-Divider ------------------- " + ONOFF(divider), "id":3},
                {"name":"5-Clear save", "id":4},
                {"name":"6-Reset Settings", "id":5},
                {"name":"7-Exit", "id" :6},
                {"name":"8-About", "id":7}
                ]
            
            clear()
            print("----------- SETTINGS -----------")
            for banana in range(len(settings_options)):
                print(settings_options[banana]["name"])
            try:
                    choice=int(input("Choose an option: "))
            except:
                print("Choose a valid option")
                t.sleep(wt)
                continue

            if choice==1:
                loading=not loading
                save()

            elif choice==2:
                try:
                    loading_time=float(input("Enter the new loading time (in seconds): "))
                    save()
                except ValueError:
                    print("Choose a valid time")
                    t.sleep(wt)

            elif choice==3:
                preserve_cursor= not preserve_cursor
                save()

            elif choice==4:
                divider=not divider
                save()

            elif choice==5:
                with open(file_path, "r") as file:
                    checkdata=json.load(file)
                    if checkdata==default_data:
                        print("Save is already empty")
                        t.sleep(wt)
                    else:
                        yn=input("Clear save? (y/N): ").lower()
                        if yn!="y":
                            print("Clearing save cancelled")
                            t.sleep(wt)
                        else:
                            moneyspent=0
                            balance=100
                            for i in range(len(library)):
                                for game in games:
                                    if game.name==library[i]:
                                        game.owned=False
                            library=[]
                            with open(file_path, "w") as f1:
                                json.dump(default_data, f1, indent=4)
                            print("Cleared save succesfully!")
                            t.sleep(wt)

            elif choice==6:
                loading=True
                divider=True
                loading_time=0.2
                preserve_cursor=True
                print("Reset settings succesfully")
                t.sleep(wt)
                save()

            elif choice==7:
                break

            elif choice==8:
                clear()
                print("------------ ABOUT ------------")
                print("- Version: ",version)
                print("- Developper: Stonyax97")
                print("- More: https://github.com/Stonyax97/MiniGameStore")
                print("- Requires Python 3.13 or later. ")
                print("\n\n- Licensed under: MyImaginaryLicense3.0\n")
                procced()
            
    elif choice == 6:
        break

    else:
        print("Choose a valid option")
        t.sleep(wt)
        continue

    save()
