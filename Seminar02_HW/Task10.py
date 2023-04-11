import random
coins = int(input('Enter coins quantity: '))
heads, tails = 1, 0
heads_sum, tails_sum = 0, 0
for i in range(coins):
    collection = random.randint(0,1)
    print(collection, end = ' ')
    if collection == heads:
        heads_sum += 1
    else:
        tails_sum += 1
if heads_sum > tails_sum:
    print(f'\nYou should turn over {tails_sum} coins with tails')
else:
    print(f'\nYou should turn over {heads_sum} coins with heads')
