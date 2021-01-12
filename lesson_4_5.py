from functools import reduce

print(reduce(lambda x, y: x * y, [z for z in range(100, 1001) if z % 2 == 0]))