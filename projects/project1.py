
#        SNAKE WATER GUN

def GameWin(comp, you):
    # if two values are equal, declare a tie!!
    if comp == you:
        return None
    # check for all possibilitis when comp choose 'w'
    elif comp == 'w':
        if you == 's':
            return True
        if you == 'g':
            return False
# check for all possibilitis when comp choose 's'
    elif comp == 's':
        if you == 'w':
            return False
        if you == 'g':
            return True
# check for all possibilitis when comp choose 'g'
    elif comp == 'g':
        if you == 'w':
            return True
        if you == 's':
            return False

print("Comp turn: Snake(s) Water(w) Gun(g) ?")
import random
randomNo = random.randint(1,3)
if randomNo == 1:
    comp = 's'
elif randomNo == 2:              # Make sure where to use '==' and '=' there is a lot of differece between them
    comp = 'w'
elif randomNo == 3:
    comp = 'g'

you = input("Your turn : Snake(s) Water(w) Gun(g) ?")
a = GameWin(comp, you)

print(f"computer choose {comp}")   # f function is used so that we can directly used {} to use that variable.
print(f"you choose {you}")

if a == None:
    print("The game is tie!")
elif a:
    print("you win")
else:
    print("you loose")


    # CONGRATULATIONS TRO ME !!
    # i have completed my first game