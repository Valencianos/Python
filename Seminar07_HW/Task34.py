def rhyme() -> str:
    my_list = input('Enter your rhyme: ').split()
    rhytm = set(map(lambda x: x.count('а'), my_list))
    if len(rhytm) < 2:
        return f'Парам пам-пам'
    return f'Пам парам'

print(rhyme())

