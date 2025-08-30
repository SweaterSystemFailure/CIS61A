def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    """
    if n<1:  
        return -1

    highest = 1
    x=2

    while n>x:
        if n%x==0:
            highest=x
        x+=1

    if highest == 1:
        return True
    else:
        return False