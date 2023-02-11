import random


#words = ["UMBRELLA", "TELESCOPE", "SMARTPHONE", "COMPUTER"]
f = open("words.txt", "r")
data = f.readline()
words = data.split()
word = random.choice(words)
word = word.upper()
total_chances = 7
guess_word = "-"*len(word)

while total_chances !=0:
    print(guess_word)
    letter = input("Guess a letter: ").upper()
    if letter in word:
        for index in range(len(word)):
            if word[index]==letter:
                guess_word = guess_word[:index]+letter+guess_word[index+1:]
            #print(guess_word)

        if guess_word == word:
            print("Congratulations you won....!")
            break
    else:
        total_chances -= 1
        print("Incorrect Guess")
        print("The remaining chances are: ",total_chances)
else:
    print("Game over")
    print("You Lose")
    print("All the are exhausted")
print("The correct word is",word)
