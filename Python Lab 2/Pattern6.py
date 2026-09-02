count = 7
for i in range(count):
    for j in range(count):
        distance = min(i, j, count - 1 - i, count - 1 - j)
        num = 4 - distance
        print(num, end=" ")
    print()