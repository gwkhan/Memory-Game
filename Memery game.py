# memery game


import random
import os
import time

wins = 0
lose = 0
level = 1
print("put exit to break")
while True:
    
    seqs = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    dificult = min(3 + level//3,10)
    
    first = random.sample(seqs, k=dificult)

    for c in first:
        print(c)
        time.sleep(max(0.2,1.5-level*0.1))

    os.system("cls" if os.name == "nt" else "clear")

    user = input("Enter values in exact sequence (comma separated): ")
    if user == "exit":
    	print(f"Wins: {wins} | Losses: {lose}\n")
    	print(f"your level was: {level}")
    	break
    check = user.strip().split(",")

    
    check = [x.strip() for x in check]
    

    if check == first:
        print("You win")
        wins += 1
    else:
        print("You lose")
        lose += 1
        print(f"Wins: {wins} | Losses: {lose}")
        print(f"your level was: {level}")
        break
    level += 1