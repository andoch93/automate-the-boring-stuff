while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue    #will take us back to the start of the loop
    print('Hello, Joe. What is the password? (it is a fish)')
    password = input()
    if password != 'swordfish':
        continue
    break
print('Access Granted')
