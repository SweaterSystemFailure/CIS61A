def is_prime(n):   
    """Returns True if n is a prime number and False otherwise.
    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    def checker (n, d): 
        if d==1:
            return True;
        elif (n%d==0):
            return False
        else:
            return checker(n,d-1)

    if n<=1:
        return False
    else:
         return checker(n,n-1) 