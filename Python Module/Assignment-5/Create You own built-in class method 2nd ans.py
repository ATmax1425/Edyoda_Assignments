class CalculatorValue:
    def __init__(self, value):
        self.value = value

    def __xor__(self, other):
        ans = eval("*".join([str(self.value) for _ in range(other.value)]))
        return ans


a = CalculatorValue(int(input("Enter Base Value: ")))
b = CalculatorValue(int(input("Enter Exponent Value: ")))
print(a ^ b)
