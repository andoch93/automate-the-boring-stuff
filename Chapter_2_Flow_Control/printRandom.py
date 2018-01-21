#importing the random module will allow you the use of it's features
import random

#you can also import several modules at once like so
import sys, os, math

#the following program will print 5 random numbers within the range of 1-10 inclusive
for i in range(5):
    print(random.randint(1, 10))
