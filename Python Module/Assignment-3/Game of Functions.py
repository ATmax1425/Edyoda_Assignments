def add_nums(nums):
    out = 0
    for i in nums:
        out += i
    return out

nums = [int(i) for i in input("Enter list values separated by space: ").split()]
ans = add_nums(nums)
print("the sum is", ans)