name = ''                               #note that an empty string can mean a falsey value, therefore 'not name' would evaluate to true
while not name:
    print('Enter your name: ')
    name = input()
print('How many guests will you have?')
numOfGuests = int(input())              #the same applies for numbers. Falsey input would count as 0, 0.0, ''(empty string)
if numOfGuests:
    print('Be sure to have enough room for all your guests')
print('Done')
