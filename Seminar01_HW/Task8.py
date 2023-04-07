m = int(input('Enter rows of chocolate: '))
n = int(input('Enter columns of chocolate: '))
k = int(input('Enter pieces quantity: '))
if k % m == 0 or k % n == 0:
    print('yes')
else:
    print('no')