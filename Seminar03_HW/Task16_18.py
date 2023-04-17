# Требуется вычислить, сколько раз встречается некоторое число X в списке A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в списке. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

import random
size = int(input('Enter list length: '))
my_list = [random.randint(1,10) for _ in range(size)]
print(*my_list)

find_num = 5
count = 0
for i in range(size):
    if my_list.count(find_num) > 0:
        count = my_list.count(find_num)
print(f'Number {find_num} occurs {count} time(s) in list.')

# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# closer_num = my_list[0]
# for i in range(size):
#     if abs(my_list[i] - find_num) <= abs(closer_num - find_num):
#         closer_num = my_list[i]
# print(f'Number {closer_num} is the nearest number to {find_num}')