len_inp_list = int(input("Enter the count of the tuples in the list: "))
print("Enter tuple values separated by space")
inp_list = [tuple([int(j) for j in input(str(i+1)+": ").split()]) for i in range(len_inp_list)]
orig = [i[1] for i in inp_list]
sorted_orig = sorted(orig)
output = []
for i in sorted_orig:
    index = orig.index(i)
    output.append(inp_list.pop(index))
    orig.pop(index)

print(output)