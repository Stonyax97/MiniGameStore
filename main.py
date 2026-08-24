#CHANGE LOGS -----------
version="1.8"

#- Discarded the msvcrt windows version, later, curses will be implemented.

#- Transtitioning into a cleaner and better project strucuture
#- Fixed a bug where purchase time stamps were saved when buying free games.
#- Fixed a bug where purchase time stamps were not deleted after a succesful restore
#- Removed preserve cursor from the main version (theres none)
#- Improved user space

#----------------------------------------------------

import time as t
import json
import os

from games import Game, games

class User:
    def __init__(self, library, balance, money_spent, money_restored):
        self.library = library
        self.balance = balance
        self.money_spent = money_spent
        self.money_restored = money_restored


#VARIABLES ------------------------------------------

    #SETTINGS VARIABLES --------
loading=True #Set to true by default

file_path=os.path.join(os.path.dirname(__file__), "save.json") #now the fie will be created where this .py file is executed.

default_data={"library":[], 
              "balance": 100, 
              "money_restored": 0, 
              "money_spent":0, 
              "loading":True,  
              "purchase_times":[]
        } #structure of the json file

main_options=["1-Games", "2-Buy a game", "3-Restore purchase", "4-User space", "5-Settings", "6-Exit"]


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
        t.sleep(1.5)

    #UPDATING VARIABLES AND SETTINGS ----------
with open(file_path, "r") as file:
    data=json.load(file)
    user = User(data["library"], data["balance"], data["money_spent"], data["money_restored"])
    loading=data["loading"]

        #UPDATING GAMES.OWNED ---------
    for i in range(len(data['library'])): 
        for game in games:
            if game.name==data["library"][i]:
                game.owned=True

#FUNCTIONS------------------------------------------------------------------

def save(): #FILE SAVING ------
    with open(file_path, "r") as file:
        data = json.load(file)

    data["library"]=user.library
    data["balance"]=user.balance
    data["money_spent"]=user.money_spent
    data["money_restored"]=user.money_restored
    data["loading"]=loading
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

def record_purchase(game):
    game.purchase_time=t.time()
    with open(file_path, "r") as file:
        data=json.load(file)
        data["purchase_times"].append({"name":game.name,"time_stamp":game.purchase_time})
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

def clear():
    if hasattr(os, "system"):
        os.system("cls" if os.name=="nt" else "clear")

def wait():
    t.sleep(1.5)

def procced():
    input("Press Enter to return: ")

def on_off(setting):
    if setting==True:
        return "ON"
    else:
        return "OFF"

def buy_game():
    try:
        game_id=int(input("Enter the ID of the desired game to purchase: "))
    except ValueError:
        print("Choose a valid Game ID")
        wait()
        return

    if game_id >= len(games) or game_id < 0:
        print("Choose a valid Game ID")
        wait()
        return
        
    if games[game_id].owned==True:
        print(f"{games[game_id].name} has already been purchased")
        wait()
        return

    if user.balance<games[game_id].price:
        print("Get a job to get more money")
        wait()
        return

    else:
        buygame=input(f"Purchase {games[game_id].name} for {"FREE" if games[game_id].price==0 else games[game_id].price}?(y/N): ").lower()
        if buygame != "y":
            print(f"Purchase of {games[game_id].name} has been cancelled")
            wait()
        else:
            print(f"Purchasing {games[game_id].name}...")
            if games[game_id].price==0:
                t.sleep(0.5)
            else:
                user.money_spent+=float(games[game_id].price)
                user.balance-=float(games[game_id].price)
                t.sleep(0.5)
                record_purchase(games[game_id])
            games[game_id].owned=True
            user.library.append(games[game_id].name)
            print(f"{games[game_id].name} Purchased succesfully and Added to library")
            wait()

def restore_purchase():
    try:
        game_id=int(input("Enter the ID of the desired game to restore its purchase: "))
    except ValueError:
        print("Choose a valid Game ID")
        wait()
        return

    if game_id >= len(games) or game_id < 0:
        print("Choose a valid Game ID")
        wait()
        return

    if games[game_id].owned==False:
        print(f"You do not own {games[game_id].name}")
        wait()
        return

    if games[game_id].price==0:
        print("You cannot restore the purchase of a free game.")
        wait()
        return

    if user.balance>100:
        print("yo bro why are u changing code")
        wait()
        return

    with open(file_path, "r") as file:
        data=json.load(file)
    purchase_times=data["purchase_times"]
    for purchase_time in purchase_times:
        if purchase_time["name"] == games[game_id].name:
            time_stamp=purchase_time["time_stamp"]
            elapsed=t.time()-time_stamp
            break

    yn=input(f"Restore purchase of {games[game_id].name} and get {games[game_id].price/2 if elapsed>7200 else games[game_id].price}?(y/N): ")
    refund=games[game_id].price / 2 if elapsed > 7200 else games[game_id].price

    if yn != "y":
        print(f"Restore purchase of {games[game_id].name} has been cancelled")
        wait()
    else:
        print(f"Restoring {games[game_id].name}...")

        user.balance+=float(refund)
        user.money_restored+=float(refund)
        games[game_id].owned=False
        user.library.remove(games[game_id].name)

        for purchase_time in data["purchase_times"]: #why are we doing data and not just purchase times?
            if purchase_time["name"] == games[game_id].name:
                data["purchase_times"].remove(purchase_time)
                break

        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)

        t.sleep(0.5)
        print(f"Restored purchase of {games[game_id].name}. ${refund:.2f} added to your balance.")
        t.sleep(2)

def info(gid):
    print("-"*40,
          f"\n> {games[gid].name} - - - - - {"Not Owned" if games[gid].owned==False else "Owned"}"
          f"\n Price: {"FREE" if games[gid].price==0 else f"${games[gid].price:.2f}"}"
          f"\n Genre: {games[gid].genre}"
          f"\n ID: {games[gid].id}"
          f"\n Developer: {games[gid].developer}"
          f"{f"\n*{games[gid].minfo}*" if games[gid].minfo is not None else ""}"
        )

#MAIN LOOP ------------------------------------------------

while True:
    clear()
    for banana in range(len(main_options)):
        print(main_options[banana])
    try:
        choice=int(input("Choose an option: "))
    except ValueError:
        print("Choose a valid option")
        wait()
        continue
    
    if choice == 1:
        for banana in range(len(games)):
            info(banana)
            if loading==True:
                t.sleep(0.2)
        procced()

    elif choice == 2:
        buy_game()

    elif choice == 3:
        restore_purchase()

    elif choice == 4:
        clear()
        games_owned=len(user.library)
        print("---------- USER SPACE ----------")
        print(f"• Balance: ${user.balance:.2f}")
        print(f"• Money spent: ${user.money_spent:.2f}")
        print(f"• Money restored: ${user.money_restored:.2f}")
        print(f"\n• Library             {games_owned}")
        if user.library==[]:
            print("---------- Empty ----------")
        else:
            for i in range(len(user.library)):
                print(f" - {user.library[i]}")
        procced()
        
    elif choice == 5:
        while True:
            settings_options = ["1-Loading Pauses ------------ " + on_off(loading),
                                "2-Clear save",
                                "3-Exit", 
                                "4-About"]
            
            clear()
            print("----------- SETTINGS -----------")
            for banana in range(len(settings_options)):
                print(settings_options[banana])
            try:
                choice=int(input("Choose an option: "))
            except:
                print("Choose a valid option")
                wait()
                continue

            if choice==1:
                loading=not loading
                save()

            elif choice==2:
                with open(file_path, "r") as file:
                    checkdata=json.load(file)
                    if checkdata==default_data:
                        print("Save is already empty")
                        wait()
                    else:
                        yn=input("Clear save?(y/N): ").lower()
                        if yn!="y":
                            print("Clearing save cancelled")
                            wait()
                        else:
                            user.balance=100
                            user.money_restored=0
                            user.money_spent=0
                            for i in range(len(user.library)):
                                for game in games:
                                    if game.name==user.library[i]:
                                        game.owned=False
                            user.library=[]
                            with open(file_path, "w") as f1:
                                json.dump(default_data, f1, indent=4)
                            print("Cleared save succesfully!")
                            wait()

            elif choice==3:
                break

            elif choice==4:
                clear()
                print("------------ ABOUT ------------")
                print("- Version: ",version)
                print("- Developer: Stonyax97")
                print("- More: https://github.com/Stonyax97/MiniGameStore")
                print("- Requires Python 3.13 or later. ")
                print("\n\n- Licensed under: MyImaginaryLicense3.0\n")
                procced()
            
    elif choice == 6:
        break

    else:
        print("Choose a valid option")
        wait()
        continue

    save()
