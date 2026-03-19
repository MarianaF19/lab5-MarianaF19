from utils import *

menssage = input("Please type your menssage\n")
codified = flip(menssage) + str(count_letters(menssage, 'a'))

print(f"Your encoded menssage is: {codified}")