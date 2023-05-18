rows = int(input('Enter rows of chocolate: '))
cols = int(input('Enter columns of chocolate: '))
pieces = int(input('Enter pieces quantity: '))
if rows * cols > pieces and (pieces % rows == 0 or pieces % cols == 0):
    print('yes')
else:
    print('no')