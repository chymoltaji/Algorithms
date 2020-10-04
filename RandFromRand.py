# Write a method to generate a random number between 1 and 7, given a method
# that generates a random number between 1 and 5 (i.e., implement rand7() using
# rand5()).

from random import randrange


print((randrange(1,6)*35)//7)