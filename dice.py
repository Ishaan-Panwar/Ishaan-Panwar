import random
a = input("Type HI to roll the dice or type TOSS for a coin toss: ")
a.lower()
if a.lower() == "hi":
   L1 = [1,2,3,4,5,6]
   print(random.choice(L1))
elif a.lower() == "toss":
    L2 = ["Heads","Tails"]
    print(random.choice(L2))
else:
    print("Bye")
