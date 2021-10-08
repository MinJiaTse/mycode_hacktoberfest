import random


# importing Image class from PIL package
from PIL import Image

# creating a object
im = Image.open(r"C:\Users\System-Pc\Desktop\Dice.jpg")


print("Welcome to the start of my code")
print("I am a random dice generator, in case you don't have any or a few at home!")
number_of_dices = int(input("How many dices do you need? (Type in numbers only!)"))
for i in range(number_of_dices):
  n = random.randint(1, 6)
  im.show()
  print("Dice " + str(i+1) + " results: " + str(n))
print("Here you go, thank you for using my dice program to generate what you need :)")
# My Own Self-generated program for people who need dices at home :)
