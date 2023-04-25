import random

list_a = [random.randint(-20, 20) for _ in range(20)]
print(list_a)
min_value = -5
max_value = 5
for i in range(len(list_a)):
    if min_value < list_a[i] < max_value:
        print(i, end=' ')