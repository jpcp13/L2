from pylab import * 
from math import * 
from methodes import * 

T = 0.99
n = 8000
h = float(T)/n 

Tk, Uk = [], []
u0 = 1.0
t0 = 0.0

uk = u0
tk = t0

Tk.append(t0)
Uk.append(u0)

for k in range(n):
	tk = tk + h 
	uk = uk + h*f2(tk, uk) 
	Tk.append(tk)
	Uk.append(uk)
	 

clf()
plot(Tk, Uk, 'r')
grid()
plt.savefig('figure2A')

show()




	
	
	
