number = int(input('Enter limit: '))
a = 2
power = 1
while a ** power < number:
    print(a**power, end = ' ')
    power += 1