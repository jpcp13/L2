import numpy as np
import matplotlib.pyplot as plt
from math import *
from moduletp3 import *

u0=1.0
T=10.0
n=80

tt, uu = euler(f, u0, T, n)

