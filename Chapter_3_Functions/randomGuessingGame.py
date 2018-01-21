import random, sys

def prompts():
    print('random number: ' + str(randomNumber))
    print('You guessed: ' + str(userGuess))

def randomNumberGenerator():
    r = random.randint(0,9)
    return r

while True:
    print('think of a number from 0-9')
    randomNumber = randomNumberGenerator()
    userGuess = input()
    if str(userGuess) == str(randomNumber):
        prompts()
        print('you are correct!')
        sys.exit()
        break
    prompts()
    print('try again')
    
    
    
