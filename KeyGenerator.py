from random import randint, choices
import string
def key_generator(length):
    return "".join(choices(string.printable[:-38], k=length))
    

print(key_generator(10))

