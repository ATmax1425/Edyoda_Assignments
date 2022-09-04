nums = [int(i) for i in input("Enter list values separated by space: ").split()]
print("Square the elements of the list:", list(map(lambda x: x ** 2, nums)))
