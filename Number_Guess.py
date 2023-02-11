import random
CompNum = random.randrange(1,101)
User = int(input("Enter Your Number:" ))
if User>CompNum:
    print("Your Computer Number is",CompNum)
    print("Your Guess Number Is To High")
elif CompNum>User:
    print("Your Computer Number is", CompNum)
    print("Your Guess Number Is Too Low")
else:
    print("Your Computer Number is", CompNum)
    print("Your Guess Number Is Equal")