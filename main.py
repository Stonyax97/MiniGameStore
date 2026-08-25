#CHANGE LOGS --------------------
version="1.8.1"

#- This update is mostly huge code and structure improvemnts rather than random features added.

#--------------------------------

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

    def can_buy(self, game_id):
        if game_id >= len(games) or game_id < 0:
            print("Choose a valid Game ID")
            wait()
            return False
                    
        if games[game_id].owned==True:
            print(f"{games[game_id].name} has already been purchased")
            wait()
            return False
            
        if self.balance < games[game_id].price:
            print("Not enough balance")
            wait()
            return False

    def buy(self, game):
            if game.price==0:
                t.sleep(0.5)
            else:
                self.balance-=float(game.price)
                self.money_spent+=float(game.price)
                t.sleep(0.5)

                record_purchase_time(game)

            game.owned=True
            self.library.append(game.name)
            print(f"{games.name} Purchased succesfully and Added to library")
            wait()

    def can_restore(self, game_id):
        if game_id >= len(games) or game_id < 0:
            print("Choose a valid Game ID")
            wait()
            return False

        if games[game_id].owned==False:
            print(f"You do not own {games[game_id].name}")
            wait()
            return False

        if games[game_id].price==0:
            print("You cannot restore the purchase of a free game.")
            wait()
            return False

    def restore(self, game_id):
        self.balance+=float(refund)
        self.money_restored+=float(refund)
        games[game_id].owned=False
        self.library.remove(games[game_id].name)

        for purchase_time in data["purchase_times"]:
            if purchase_time["name"] == games[game_id].name:
                data["purchase_times"].remove(purchase_time)
                break

        with open(FILE_PATH, "w") as file:
            json.dump(data, file, indent=4)


#VARIABLES --------------------

    #SETTINGS VARIABLES --------
loading=True 

FILE_PATH=os.path.join(os.path.dirname(__file__), "save.json")

default_data={"library":[], 
              "balance": 100, 
              "money_restored": 0, 
              "money_spent":0, 
              "loading":True,  
              "purchase_times":[]
        } #structure of the json file

MAIN_OPTIONS=["1-Games", "2-Buy a game", "3-Restore purchase", "4-User space", "5-Settings", "6-Exit"]


#FILE READING --------------------

    #CREATING FILE STRUCTURE ------
if not os.path.isfile(FILE_PATH) or os.path.getsize(FILE_PATH)==0: #if it doesn't exist OR is empty
    with open(FILE_PATH, "w") as file:
        json.dump(default_data, file, indent=4)

    #CHECKING FOR CORRUPTED FILE -------
with open(FILE_PATH, "r") as file:
    try:
        json.load(file)
    except json.JSONDecodeError:
        print("File is corrupted... Formating file.")
        with open (FILE_PATH, "w") as file:
            json.dump(default_data, file, indent=4)
        t.sleep(1.5)

    #UPDATING VARIABLES AND SETTINGS ----------
with open(FILE_PATH, "r") as file:
    data=json.load(file)
    user = User(data["library"], data["balance"], data["money_spent"], data["money_restored"])
    loading=data["loading"]

        #UPDATING GAMES.OWNED ---------
    for game in games:
        if game.name in user.library:
            game.owned=True

#FUNCTIONS --------------------

def save(): #FILE SAVING ------
    with open(FILE_PATH, "r") as file:
        data = json.load(file)

    data["library"]=user.library
    data["balance"]=user.balance
    data["money_spent"]=user.money_spent
    data["money_restored"]=user.money_restored

    data["loading"]=loading
    with open(FILE_PATH, "w") as file:
        json.dump(data, file, indent=4)

def record_purchase_time(game):     
    game.purchase_time=t.time()
    with open(FILE_PATH, "r") as file:
        data=json.load(file)
        data["purchase_times"].append({"name":game.name,"time_stamp":game.purchase_time})
    with open(FILE_PATH, "w") as file:
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
    for banana in range(len(MAIN_OPTIONS)):
        print(MAIN_OPTIONS[banana])
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
        try:
            game_id=int(input("Enter the ID of the desired game to purchase: "))
        except ValueError:
            print("Choose a valid Game ID")
            wait()
            continue

        if user.can_buy(game_id) == False:
            continue

        yn=input(f"Purchase {games[game_id].name} for {"FREE" if games[game_id].price==0 else games[game_id].price}?(y/N): ").lower()
        if yn != "y":
            print(f"Purchase of {games[game_id].name} has been cancelled")
            wait()
        else:
            print(f"Purchasing {games[game_id].name}...")
            user.buy(games[game_id])

        
    elif choice == 3:
        try:
            game_id=int(input("Enter the ID of the desired game to restore its purchase: "))
        except ValueError:
            print("Choose a valid Game ID")
            wait()
            continue

        if user.can_restore(game_id) == False:
            continue

            #CALCULATE ELAPSED TIME OF THE PURCHASED GAME -------
        with open(FILE_PATH, "r") as file:
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

            user.restore(game_id)

            t.sleep(0.5)
            print(f"Restored purchase of {games[game_id].name}. ${refund:.2f} added to your balance.")
            wait()

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
                with open(FILE_PATH, "r") as file:
                    checkdata=json.load(file)
                    if checkdata==default_data:
                        print("Save is already empty")
                        wait()
                    else:
                        yn=input("Clear save?(y/N): ").lower()
                        if yn!="y":
                            print("Clearing save cancelled")
                            continue

                        user.balance=100
                        user.money_restored=0
                        user.money_spent=0
                        for game in games:
                            if game.name in user.library:
                                game.owned=False
                        user.library=[]
                        with open(FILE_PATH, "w") as f1:
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
