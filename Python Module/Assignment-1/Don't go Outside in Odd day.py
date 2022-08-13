print("Enter a value and Press Enter and Put next value at end just Press Enter without a value")
count = 0
even_count = 0
odd_count = 0
while True:
    value_str = input("Enter value No." + str(count) + ": ")
    if value_str:
        value = int(value_str)
        if value % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    else:
        break
    count += 1

print("Number of even numbers: " + str(even_count))
print("Number of odd numbers: " + str(odd_count))
