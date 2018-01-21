#first argument: start of for loop
#second argument: end of for loop
#third argument: 'step argument' or amount that the variable is increased by after each iteration
print('For loop counting up by 2')
for i in range(0, 10, 2):
    print(i)

print()

print('For loop counting backwards by -1 until it reaches -1 but does not include -1')
#making a for loop count down instead of up
for i in range(5, -1, -1):
    print(i)
