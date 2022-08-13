input_str = input("Enter the Word I will send it to Mirror Dimension: ")
output_str = ""
i = len(input_str)-1
while i >= 0:
    output_str += input_str[i]
    i -= 1
print("Word in Mirror Dimension: " + str(output_str))
