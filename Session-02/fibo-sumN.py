# -- Session 2. Exercise 3


def fibosum(n):
    x1 = 0
    x2 = 1
    result = 0
    for i in range(n):
        x3 = x1 + x2
        x1 = x2
        x2 = x3
        result = result + x1
    return result


print("Sum of the first 5 terms of the Fibonacci series: ", fibosum(5))
print("Sum of the first 10 terms of the Fibonacci series: ", fibosum(10))
