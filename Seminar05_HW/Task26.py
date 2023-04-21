def degree(num_a: int, num_b: int) -> int:
    if num_b == 0:
        return 1
    return num_a * degree(num_a,num_b - 1)

print(degree(3,5))


