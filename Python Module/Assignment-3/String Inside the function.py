def reverse_string(s):
    out = ''
    for i in range(1, len(s)+1):
        out += s[-i]
    return out
    
orig_str = input("Enter a string: ")
reve_str = reverse_string(orig_str)
print("reverse string is:" , reve_str)