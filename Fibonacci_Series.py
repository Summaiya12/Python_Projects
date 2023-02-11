#Python program of fibacci numbers
number = int(input("Enter the number of series till you want: "))
a = 0
b = 1
c = 0
print(a)
print(b)
i = 1
while i < number:
    c = a+b
    a = b
    b = c
    i = i+1
    print(c)
print("The Fibonacci Sequence for the given number " +str(number)+ " is :" ,c)
