# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 10:18:25 2020

@author: ewe
"""

import matplotlib.pyplot as plt
import numpy as np

Rt = 6
Ro = 0.7
ho = 14
g  = 9.8

dt = 1.0

h = ho
t = 0

Vh = []
Vt = []

#Constantes:
Ch = np.sqrt(ho)
Cr = (Ro/Rt)**2
Cx = ((-3)*(np.sqrt(2*g)))/2

for i in range(50):
    h = (Cx*Cr*t + Ch)**2
    t = t + dt
    Vh.append(h)
    Vt.append(t)
    
plt.plot(Vt, Vh)
plt.xlabel("T")
plt.ylabel("h")
plt.title("Vaciado de un Tanque")


