def fibonacciN(n):
    """Return the nth Fibonacci number.
    Fibonacci Numbers is a series of numbers in which each number is 
    the sum of the two preceding numbers
    >>> fibonacciN(5) # 1, 1, 2, 3, 5
    5
    >>> fibonacciN(7) 
    13
    """
    
    first=1
    second=0
    result=0
    counter=0

    while counter < n:
        result = first + second
        first = second
        second = result
        counter +=1

    return result