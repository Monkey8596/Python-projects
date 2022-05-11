
def factorial(n):
    """ Calcualr el factorial de n.

    n int > 0
    returns n!
    """
    print(n)
    
    if n==1:
        return 1

    return n * factorial (n - 1)

n = int(input('Escribe un numero entero: '))

print(factorial(n))