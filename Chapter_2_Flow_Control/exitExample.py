#we will be demonstrating the use of the sys.exit() function which automatically terminates a program when it reaches the end of its instructions
#note that you have to import the sys module in order to make use of this function
import sys

while True:
    print("Type 'exit' to exit this program")
    response = input()
    if response == 'exit':
        print('Program succesfully terminated')
        sys.exit()
    print('You typed ' + response + '.')

