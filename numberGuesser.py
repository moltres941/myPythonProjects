import random
from time import sleep
import pyfiglet

art = pyfiglet.figlet_format("THE END")


topOfRange = input("Type a number: ")

if topOfRange.isdigit():
    topOfRange = int(topOfRange)

    if topOfRange <= 0:
        print("Please type a number larger than 0 next time mf")
        quit()

else:
    print("Type a number next time!!")
    quit()



random_number = random.randint(0, topOfRange)
guesses = 0

while True:
    sleep(1)
    guesses += 1
    user_guess = input("Make a guess: ")
    if  user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Type a number next time!!")
        continue

    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:
        print("You were above the number")
    else:
        print("You were below the number")

print(f"You got it in {guesses}, try")
sleep(2)
print(art)
