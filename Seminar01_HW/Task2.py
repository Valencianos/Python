num = int(input('Enter 3-digits number: '))
print(f'Your sum: {num % 10 + num // 10 % 10 + num // 100 % 10}')