a = int(input('Enter 3-digits number: '))
print(a % 10 + a // 10 % 10 + a // 100 % 10)