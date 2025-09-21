import random

def art():
    logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
    return logo
    
def r(c):
    cards = [11,2,3,4,5,6,7,8,9,10,10,10]
    c.append(random.choice(cards))
    return c  
def blackjack():
    ch =input(" Do you want to call another hand ? Press [y] for yes [n] for no ")
    if ch == "y":
        print(f"your hand : {r(l1)} Current Score : {sum(l1)}")
        print(f"Dealers First hand : {l2}")
        if sum(l1) >21:
            return()

        blackjack()
    


def dealer():
    if   sum(l1)<21 and sum(l2) < sum(l1):
        r(l2)
        dealer()
    else:
        return()
def play():
    print(art())
    global l1
    global l2
    l1 = []
    l2 = []

    r(l1)
    print(f"your first hand : {r(l1)} Current Score : {sum(l1)}")

    print(f"Dealers first  hand : {r(l2)}")
    
    
    while True:
        blackjack()
        dealer()
        print(f"Your final hand : {l1} Final Score : {sum(l1)}")
        print(f"Dealers  final hand : {l2} Final Score : {sum(l2)}")

        if(sum(l2) > sum(l1) and sum(l2) <= 21 or sum(l1)>21):
            print("Dealer win!")
        elif(sum(l1) <= 21 and sum(l1)>sum(l2) or sum(l2)>21):
            print("You win!")
        elif(sum(l1)==sum(l2)):
            print("DRAW")


        d = input("Do you want to play  another round ? Press [y] for yes [n] for no ")
        if d == "y":
            play()
        elif d == "n":
            return()
        
play()










