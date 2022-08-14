values_list = list(map(int, input("Enter a values separated by space: ").split()))
even_count = 0
odd_count = 0
for i in values_list:
    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Number of even days: " + str(even_count))
print("Number of odd days: " + str(odd_count))
