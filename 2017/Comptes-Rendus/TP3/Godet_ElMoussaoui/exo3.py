import matplotlib.pyplot as plt
from numpy import *
from math import *
from pylab import *

def euler(f,t,u,u0,T,n):
  tt,uu = [],[]
  tt.append(tk)
  uu.append(u0)
  h = float (T)/n
  for i in range(u0,n):
	t=t+h
	u=u + h*f(t,u)
	tt.append(t)
	uu.append(u)

  return tt,uu
