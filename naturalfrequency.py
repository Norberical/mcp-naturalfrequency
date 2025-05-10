import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import det
from math import sin, cos, sinh, cosh, inf
import json

def general_beam_natural_frequency(k_0: tuple[float,float],k_1: tuple[float,float],
                                   c_0: tuple[float,float],c_1: tuple[float,float]) -> float:
        
    detA = lambda x: det(np.array([
        [k_0[0], -k_0[1]*x**3, k_0[0], k_0[1]*x**3],
        [-c_0[1]*x, c_0[0], c_0[1]*x, c_0[0]],
        [-k_1[1]*x**3*sinh(x)+k_1[0]*cosh(x),-k_1[1]*x**3*cosh(x)+k_1[0]*sinh(x), -k_1[1]*x**3*sin(x)+k_1[0]*cos(x), k_1[1]*x**3*cos(x)+k_1[0]*sin(x)],
        [-c_1[1]*x*cosh(x)+c_1[0]*sinh(x),-c_1[1]*x*sinh(x)+c_1[0]*cosh(x), c_1[1]*x*cos(x)-c_1[0]*sin(x), c_1[1]*x*sin(x)+c_1[0]*cos(x)]
    ]))

    dx = 0.01
    x0 = 0.01
    x1 = x0+dx
    f0 = detA(x0)
    f1 = detA(x1)
    while f0*f1 > 0:
        x0 = x1
        x1 += dx
        f0 = f1
        f1 = detA(x1)
    
    x_a = x0 - (x1-x0)/(f1-f0)*f0
    f_a = detA(x_a)
    while abs(f_a) > 1e-6:
        if f0*f_a < 0:
            x1 = x_a
            f1 = f_a
        elif f1*f_a < 0:
            x0 = x_a
            f0 = f_a
        x_a = x0 - (x1-x0)/(f1-f0)*f0
        f_a = detA(x_a)

    return x_a

if __name__ == "__main__":
    k_0 = (1, 1/inf)
    k_1 = (0, 1)
    c_0 = (1, 1/inf)
    c_1 = (0, 1)
    
    x_a = general_beam_natural_frequency(k_0,k_1,c_0,c_1)
    print(f"Eigenfrequency: {x_a**2}")