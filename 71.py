def sum_digits(number):
    s = 0
    for digit in str(number):
        raqam = int(digit)
        s += raqam
    return s
n = input() # "123456"
start = n[0:3]
end = n[3:6]