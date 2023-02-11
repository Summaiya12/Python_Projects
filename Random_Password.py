import random
import string
print("Welcome to our Random Generator")
def main():

    lenght = int(input("Enter the lenght of password you want : "))
    lowerD = string.ascii_lowercase
    upperD = string.ascii_uppercase
    digitD = string.digits
    symbolsD = string.punctuation
    combine = lowerD+upperD+digitD+symbolsD
    x=random.sample(combine,lenght)
    password="".join(x)
    print(password)
    main()
main()
