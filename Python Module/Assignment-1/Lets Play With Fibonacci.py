end = int(input("Enter the maximum value for fibonacci series: "))
pri = 0
now = 1
temp = 0
while now < end:
    temp = pri
    pri = now
    now = temp + pri
    print(pri)
