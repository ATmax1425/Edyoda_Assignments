nums = [int(i) for i in input("Enter list values separated by space: ").split()]
out = list(map(lambda x: x * 3, nums))
print("Triple of list numbers:", out)
