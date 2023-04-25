first_element = int(input('Enter first element: '))
step = int(input('Enter step: '))
quantity = int(input('Enter quantity of elements: '))

sequence = []
for i in range(1, quantity + 1):
    sequence.append(first_element + (i - 1) * step)
print(sequence) 