from operator import mul

def twenty_twenty_five():
    """Assignment: Come up with the most creative expression that evaulates to 2025 using only numbers and the +, *, and - operators. 
    Approach: This function returns 2025 as a product of its prime factors.
    >>> twenty_twenty_five()
    2025
    """
    return mul(mul(5,5), mul(mul(3, 3), mul(3, 3)))