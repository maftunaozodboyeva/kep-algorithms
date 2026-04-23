def calc(a, b, s):
    if s == "+":
        return a + b
    if s == "-":
        return a - b
    if s == "*":
        return a * b
    if s == "/":
        return a / b


print(calc(2, 5, "+"))
