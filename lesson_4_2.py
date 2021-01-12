lst1 = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 124]
lst2 = [lst1[i] for i in range(1, len(lst1)) if lst1[i] > lst1[i-1]]

print(lst2)