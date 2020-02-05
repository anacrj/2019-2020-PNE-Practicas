# -- Session 2. Exercise 3


def fibosum(n):
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


fibonacci = fibosum(30)

print("Sum of the first 5 terms of the Fibonacci series: ", fibonacci[5])
print("Sum of the first 10 terms of the Fibonacci series: ", fibonacci[10])
