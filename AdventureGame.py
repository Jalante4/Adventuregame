name = input("type your name: ")
print("welcome", name, "to this adventure")

answer = input("You wake up in a cell. Do you pick the lock or wait? (pick/wait) ").lower()


if answer == "pick":
    answer = input("You made it out. There is two paths left or right, which way do you go? (left/right) ").lower()

    if answer == "left":
       answer = input("you went left and got caught by guards. Do you run or hide? (run/hide) ")
       if answer == "run" :
        print("You win.")
    elif answer == "right": 
        print("you went right and got killed by guards.")
    else: 
        print("not a valid option. you lose.")

elif answer == "wait":
    print("you died of old age.")
else:
    print("not a valid option. you lose.")

print("thank you for playing.")