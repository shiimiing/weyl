from numpy import *
import scipy.integrate as integrate
from mpmath import *

lmbda = 0.5
alpha = 0.5

#mpmath configuration
mp.dps = 15
mp.pretty = True

#DO NOT MODIFY IT
def Phi_of_x(x):
    eq = sin(lmbda*x)
    return eq

def Psi_of_kt(k, t):
    k = float(k); t = float(t)
    eq = cos(k*t-pi/4)/sqrt(k)
    return eq

def sigma(t):
    eq = nsum(lambda k: Psi_of_kt(k, t), [1, inf])
    return float(eq)

def f_of_x(x):
    eq = (0.5**(-0.5))*(sin(lmbda*x-pi/4))
    return eq

func = float(nsum(lambda k:cos(k-pi/4)/sqrt(k), [1, inf]))
hand = 0
for k in range(1, 10000):
    hand += cos(k-pi/4)/sqrt(k)
print("Error is: {}".format(hand-func))





