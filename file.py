def calculateIntegral(f, a, b, n):
    """
    Calculate the integral of f(x) from a to b using n subintervals.
    """
    h = (b - a) / n
    sum = 0.0
    for i in range(n):
        sum += f(a + i * h)
    return h * sum
    