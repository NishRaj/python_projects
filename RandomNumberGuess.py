import random

def guessRandomNumber():
    start = input("Enter the start of the range: ")
    while not start.isdigit():
         print("Please enter a valid number.")
         start = input("Enter the start of the range: ")  
    end = input("Enter the end of the range: ")
    while not end.isdigit() or int(end) < int(start):
        print("Please enter a valid number.")
        end = input("Enter the end of the range: ")
    val = random.randint(int(start),int(end))
    counter = 0
    while True:
        guessedNumber = input("Guess a number: ")
        if not guessedNumber.isdigit():
            print("Please enter a valid number.")
            continue
        counter += 1
        if int(guessedNumber) == int(val):
            break
    suffix = ""
    if counter > 1:
        suffix = "s"
    print(f"You guessed the number in {counter} attempt{suffix}")

guessRandomNumber()