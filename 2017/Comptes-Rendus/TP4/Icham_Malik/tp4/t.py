
def _ifactor(n):
    t , j = [], 2
    while n > 1:
        if (n % j) == 0:
            t.append(j)
            n //= j
        else:
            j += 1
    return t
 
print(_ifactor(120))
