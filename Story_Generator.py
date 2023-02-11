import random
while True:
    print("Hello Reader")
    name = input("Enter Your Name : ")
    print("Hello" , name)
    names = ["Zara" , "Ben" , "Andrew" , "Sam" , "Aisha"]
    places = ["China" , "Iran" , "Dubai" , "USA"]
    quest = ["seek the holy grail" , "return thr ring" , "slay the dragon"]
    roles = ["knight" ,"Amazon warrior" , "orge" , "witch"]
    randomname = random.choice(names)
    randomplaces = random.choice(places)
    randomquets = random.choice(quest)
    randomrole = random.choice(roles)
    story = "Once upon a time there was a  "  +  randomrole  +  " called  "  +  randomname  +  "."
    print(story)