from operator import mul, sub

def multiplyButFrustrating (variableOne, variableTwo):
    """Multiplies variableOne by variableTwo
    >>> multiplyButFrustrating(2,6)
    11
    >>> multiplyButFrustrating(0,3)
    -1
    >>> multiplyButFrustrating(5,-1)
    -6
    """
    return sub(mul(variableOne, variableTwo), 1)