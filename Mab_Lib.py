# user input
adj1 = input("Give an  first adjective: ")
noun1 = input("Give a  first noun: ")
verb1 = input("Give a first verb past tense: ")
adverb1 = input("Give a first adverb: ")
adj2 = input("Give a second adjective: ")
noun2 = input("Give a second noun: ")
noun3 = input("Give a third noun: ")
adj3 = input("Give a third adjective: ")
verb2 = input("Give a second verb: ")
adverb2 = input("Give a second adverb: ")
verb3 = input("Give a second verb past tense: ")
adj4 = input("Give a fourth adjective: ")
# actual sentence

madlib=f"Today I went to the zoo. I saw a(n) {adj1} {noun1} jumping up and down in its tree. \
 He {verb1} {adverb1} through the large tunnel that led to its {adj2} {noun2}. \
 I got some peanuts and passed them through the cage to a gigantic gray {noun3} towering above my head. \
  Feeding that animal made me hungry. I went to get a {adj3} scoop of ice cream. It filled my stomach.  \
  Afterwards I had to {verb2} {adverb2} to catch our bus. When I got home I {verb3} my mom for a {adj4} day at the zoo."
print(madlib)