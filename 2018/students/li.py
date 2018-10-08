from math import log
from math import sqrt
from math import factorial
def li(x):
    g = 0.577215664901532
    R=sqrt(x)
    S=0
    I=0
    for n in range (1,16):
        A=((-1)**(n-1))*((log(x))**n)
        B=(factorial(n))*(2**(n-1))
        S=S+(A/B)
        m=(n-1)/2
        for k in range (int(m)):
            I=(1/(2*k+1))+I
    E = g + log(log(x)) + R*S*I
    return(E)
