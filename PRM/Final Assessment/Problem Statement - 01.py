numbers = list(map(int, input().split()))
numbers.sort()
split_on = len(numbers)//2
high = numbers[split_on:]
low = numbers[:split_on]
ans = []
for i in range(len(high)):
    ans.append(high[-i+1])
    if len(low) > i:
        ans.append(low[i])
print(ans)
