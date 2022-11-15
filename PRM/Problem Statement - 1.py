n = int(input("Enter no of Elements: "))
words = input("Enter Elements separated by Space: ").split()
words.sort(key=lambda x: x[-2])
print(words)
