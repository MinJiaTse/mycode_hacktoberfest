from random import randint

print("Welcome to the start of my code")
print("I am a random dice generator, in case you don't have any or a few at home!")

number_of_dices = int(input("How many dices do you need? (Type in numbers only!)"))

for i in range(number_of_dices):
  n = randint(1, 6)
  print(f"Dice {str(i+1)} results {str(n)}")

  print("Here you go, thank you for using my dice program to generate what you need :)")
  
# My Own Self-generated program for people who need dices at home :)
