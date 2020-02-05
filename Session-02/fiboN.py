# -- Session 2. Exercise 2


def fibon(n):
    x1 = 0
    x2 = 1
    list_fibon = []
    if n >= 1:
        list_fibon.append(x1)
    if n >= 2:
        list_fibon.append(x2)
    if n >= 3:
        for n in range(3, n + 1):
            xn = x1 + x2
            list_fibon.append(xn)
            x1 = x2
            x2 = xn
    return list_fibon


fibonacci = fibon(20)

print("5th Fibonacci term: ", fibonacci[5])
print("10th Fibonacci term: ", fibonacci[10])
print("15th Fibonacci term: ", fibonacci[15])
