import random

print("Welcome to the start of my code")
print("I am a random dice generator, in case you don't have any or a few at home!")

dices = int(input("How many dices do you need (numbers only)? "))

for dice in range(dices):
    roll = random.randint(1, 6)
    print(f"Dice #{dice + 1} results: {roll}")
    
print("Here you go, thank you for using my dice program to generate what you need :)")
# My own self-generated program for people who need dices at home :)
