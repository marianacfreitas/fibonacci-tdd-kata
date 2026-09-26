def fibonacci(n):
    n1 = 0
    n2 = 1
    for i in range(n):
        temp = n1
        n1 = n2
        n2 = temp+n2
    return n1