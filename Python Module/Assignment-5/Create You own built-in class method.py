class Calculator:
    def __init__(self, first_value, second_value):
        self.first_value = first_value
        self.second_value = second_value

    def pow(self):
        ans = 1
        for exponent in range(self.second_value):
            ans *= self.first_value
        return ans

    def mlt(self):
        ans = self.first_value * self.second_value
        return ans


x, y = map(int, input("enter values for x, n separated by space: ").split())
a = Calculator(x, y)
print(a.pow())
