import random
qty = int(input('Enter bushes number: '))
bushes = [random.randint(1,100) for _ in range(qty)]
print(bushes)

crop = bushes[-2] + bushes[-1] + bushes[0]
for i in range(len(bushes) - 1):
    if bushes[i - 1] + bushes[i] + bushes[i + 1] > crop:
        crop = bushes[i - 1] + bushes[i] + bushes[i + 1]

print(crop)