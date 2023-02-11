#Text Based Adventure Game
while True:
    answer = input("What you like to play? (yes/no)" )

    if answer.lower().strip() == "yes":

        answer = input("You reach a crossroad , would you like to left or right?" ).lower().strip()
        if answer == "left":
            answer = input("You encounter a monster , would you like to run or attack" )

            if answer == "attack":
             print("The was not the greatest idea , you lost" )
            else:
             print("Good choice you made it safely" )

             answer = input("You see a car or plane which you like to take? (car/plane)")

             if answer == "plane":
                 print("Unfortunately you don't know how to fly ,GAME OVER....!")
             else:
                 print("Hurray..! You WON")


        elif answer == "right":
         print("You walk aimlessly to the right and fell in to a patch of ice , You injured your leg ,GAME OVER...!" )

        else:
         print("Invalid choice , you lost..!" )


    else:
        print("That's to bad..!" )
        break


