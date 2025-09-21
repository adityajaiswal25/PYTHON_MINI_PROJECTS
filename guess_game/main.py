import random
import art
import game_data

def compare(cs,a,b,c):


    if c == 'a':
        if a['follower_count']>b['follower_count']:
            cs+=1
            print(f"your current score is {cs}")

        else:
            print(art.logo)
            print(f" Sorry that's Wrong ! your final score is {cs}")
            cs =False
    elif c == 'b':
        if b['follower_count']>a['follower_count']:
            cs+=1
            print(f"your current score is :{cs}")
        else:

            print(art.logo)
            print(f" Sorry that's Wrong ! your final score is :{cs}")
            cs =False

    return cs
def game():
    print(art.logo)
    cs = 0
    # a = random.choice(game_data.data)
    b = random.choice(game_data.data)
    while True:
        # if b['follower_count']>a['follower_count']:
        #     a = b
        #     b = random.choice(game_data.data)
        # elif b['follower_count']<a['follower_count']:
        #     b = a
        #     a = random.choice(game_data.data)
        a = b
        b = random.choice(game_data.data)

        print(f"COMPARE A : {a['name']} a {a['description']} from {a['country']}")
        print(art.vs)
        print(f"AGAINST B :  {b['name']} a {b['description']} from {b['country']}")
        c = input("Who has more followers? Type [A] or [B] : ").lower()
        cs =(compare(cs,a,b,c))


        if cs ==False:

            break

    n = input("Do you want to play again? (y/n): ")
    if n == 'y':
        game()




game()
























