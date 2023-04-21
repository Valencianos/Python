def summa(a: int, b: int):
    if b == 0:
        return a
    else:
        a += 1
        return summa(a, b - 1)

print(summa(16,12))
