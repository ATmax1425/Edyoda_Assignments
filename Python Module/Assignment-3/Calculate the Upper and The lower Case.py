def calculate(s):
    upper_case = 0
    lower_case = 0
    for i in s:
        if i.isupper():
            upper_case += 1
        elif i.islower():
            lower_case += 1
    
    return upper_case,  lower_case

in_str = input("Enter a string: ")

upper_case_count, lower_case_count = calculate(in_str)

print("There are", upper_case_count, "upper case letters")
print("There are", lower_case_count, "lower case letters")