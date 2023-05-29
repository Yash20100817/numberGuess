import random
print("Number Guess")
number= random.randint(1, 9)
chances = 0
print("Guess the number (It is between 1-9)")
while chances>5
guess=int(input("Enter the guess:-"))
if guess==number:
    print("Congrats! Your guess was correct!!")

if guess>number:
    print("Your guess was too high, try going with a lower number")
if guess<number:
    print("Your guess was too low, try going with a higher number")
if chances>5:
    print("You lost!! ;( The number was", number)