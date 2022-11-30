# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 09:24:22 2020

@author: ewe
"""

import matplotlib.pyplot as plt
import numpy as np

Rt = 6
Ro = 0.7
ho = 14
g  = 9.8

dt = 0.25

h = ho
t = 0

Vh = []
Vt = []

for i in range(200):
    h = -(((3)*(Ro/Rt)**2)*np.sqrt(2*g*h))*dt + h
    t = t + dt
    Vh.append(h)
    Vt.append(t)
    
plt.plot(Vt, Vh)
plt.xlabel("T")
plt.ylabel("h")
plt.title("Vaciado de un Tanque")

print(Vh)