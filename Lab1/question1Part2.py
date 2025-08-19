def exponentiate(base, exponent):
    """Exponentiates base argument by exponent argument, assuming the exponent is a positive integer which is greater than 1.
    >>> exponentiate(4, 2)
    16
    """
    result = base
    for _ in range (exponent-1):
        result *= base

    return result

def multiply (variableOne, variableTwo):
    """Multiplies variableOne by variableTwo
    >>> multiply(2,6)
    12
    """
    return variableOne * variableTwo

def twenty_twenty_five():
    """Assignment: Come up with the most creative expression that evaulates to 2025 using only numbers and the +, *, and - operators. 
    Approach: This function returns 2025 as a product of its prime factors.
    >>> twenty_twenty_five()
    2025
    """
    return multiply(exponentiate(3,4), exponentiate(5, 2))