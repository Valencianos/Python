sum = int(input('Sum = '))
multiplication = int(input('Multiplication = '))
x = 0
while x < sum:
    x += 1
    if sum - x == multiplication/x:
        print(f'{x} {sum - x}')
        break
