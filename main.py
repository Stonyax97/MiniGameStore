import time

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
        "ID" : 1
    },
    {
        "Name": "FIFA",
        "Price": "59.99$",
        "Genre": "Sports",
        "Owned": False,
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
        "ID" : 4
    },
    {
        "Name" : "Geometry dash",
        "Price" : "4.99$",
        "Genre" : "Action-Platformer",
        "Owned" : False,
        "ID" : 5
    }
]

def info(gid):
    if games[gid]["Owned"] == False :
        print(f"> {games[gid]["Name"]}\n Price: {games[gid]["Price"]}\n Genre: {games[gid]["Genre"]}\n Owned: Not Owned\n ID: {games[gid]["ID"]}")
    else:
        print(f"> {games[gid]["Name"]}\n Price: {games[gid]["Price"]}\n Genre: {games[gid]["Genre"]}\n Owned: Bought\n ID: {games[gid]["ID"]}")

def procced():
    input("Go back to main menu? ")

library=[]
moneyspent=0
    
while True:
    print("1-Show Games")
    print("2-Buy a game")
    print("3-Show total spent")
    print("4-Show library")
    print("5-Clear library")
    print("6-Exit")
    
    choice=int(input("Choose an option: "))
    
    if choice == 1:
        for banana in range(6):
            info(banana)
        procced()
    
    elif choice == 2:
        cgtb=int(input("Enter the ID of the desired game to purchase: "))
        if cgtb <= 5:
            buygame=str(input(f"Purchase {games[cgtb]["Name"]} for {games[cgtb]["Price"]}?(Y/N)")).lower()
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
        library.clear()
        
    elif choice ==6:
        break
    
    else:
        print("Error: Choose a valid option")
        time.sleep(1.2)