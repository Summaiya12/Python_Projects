while True:
    ans = input("I am reddit in python do you know (yes/no)")
    if ans.lower().strip() == "yes":
        ans = input("Would you like to become a programmer?(yes/no)")
        if ans == "yes":
         print("Good choice you do really good work")
        if ans == "yes":
          print("You insert a good choice")
        else:
            print("Invalid Choice who don't like to be a programmer")
        ans=input("Would you like to take help of me in problem?(yes/no)")
        if ans == "yes":
            print("Good choice now think like yor work is done")
        else:
            print("Invalid I was come over here to help you")
    elif  ans == "no":
        print("You do bad choice this is bad for you")

    else:
        print("Invalid choice")

    break
