def count_k(n, k):
    """ 
    >>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1 
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3) 
    274
    >>> count_k(300, 1) # Only one step at a time 
    1
    """
    def ranger(stairs, stepSize):
        if (stairs<0 or stepSize > k):
            return 0
        elif (stairs==0):
            return 1
        else:
            return ranger (stairs-stepSize, 1) + ranger(stairs, stepSize+1)
        
    return ranger(n,1)