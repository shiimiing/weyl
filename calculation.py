from numpy import *
from constant import *
import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt
def calculate(x):
    eq = integrate.quad(lambda t: Phi_of_x(x-t)*sigma(t), 0, 2*pi)[0]
    eq = eq/pi
    return eq
def simpson(x):
    a = 0
    b = float(2*pi)
    N = 50
    dt = (b-a)/N
    T = np.linspace(a,b,N+1)
    y = []
    for i in range(0, len(T)):
        t = T[i]
        y.append(Phi_of_x(x-t)*sigma(t))
    S = dt/3 * np.sum(y[0:-1:2] + 4*y[1::2] + y[2::2])
    return S/pi

def ver_two(x):
    sum = 0
    for k in range(1, 100):
        eq = integrate.quad(lambda t: Phi_of_x(x-t)*((cos(k*t-pi/4)/(k**0.5))), 0, 2*pi)[0]
        sum += eq
    return sum/pi
Y=[]
Z=[]
f=[]
X = linspace(0, 8*pi, 40)
for x in X:
    Z.append(ver_two(x))
    print("Appended {}".format(x))
    f.append(f_of_x(x))
plt.subplots()
plt.plot(X, Z, label="Integral")
plt.plot(X,f, label="Correct")
plt.legend()
plt.show()
