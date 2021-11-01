
def fibonacci(n):
# tested on 10,0 and 1
    '''
    A recursive function that returns the fibonacci value for a given number.
    '''
    pass
# returning the base case
    if n == 0:
        return n
    if n == 1:
        return 1
# calculation the fibonacci(n) by this equation: F(n) = F(n-1) + F(n-2)
    return fibonacci(n-1)+fibonacci(n-2)


def lucas(n):
    # tested on 10,0 and 1
    '''
    A recursive function that returns the lucas value for a given number.
    '''
    pass
    if n ==0:
        return 2

    if n ==1:
        return 1
    
    if n > 1:
        return lucas(n-1) + lucas(n-2)


def sum_series(n, n1=0,n2=1):
    '''
    A recursive function that returns either the fibonacci or the lucas value for a given number according to the first and second numbers.
    '''
    pass
    if n1 == 0 and n2 == 1:
        return fibonacci(n)
    if not n1 == 0 or n2 == 1:
        return lucas(n)

    return sum_series(n, n1, n2)
