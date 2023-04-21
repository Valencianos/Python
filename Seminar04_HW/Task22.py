import random
size_a, size_b = int(input('Enter list "A" length: ')), int(input('Enter list "B" length: '))
my_list_a, my_list_b = [random.randint(1,10) for _ in range(size_a)], [random.randint(1,10) for _ in range(size_b)]
print(my_list_a, my_list_b)

my_list_a, my_list_b = set(my_list_a), set(my_list_b)

my_list = list(my_list_a.intersection(my_list_b))
my_list.sort()
print(my_list)