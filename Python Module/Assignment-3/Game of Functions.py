def add_nums(num):
    out = 0
    for i in num:
        out += i
    return out


nums = [int(i) for i in input("Enter list values separated by space: ").split()]
ans = add_nums(nums)
print("the sum is", ans)
