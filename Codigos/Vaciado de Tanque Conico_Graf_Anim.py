# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 14:56:15 2020

@author: ewe
"""

import matplotlib.pyplot as plt
import numpy as np

#Variables del Cono y el Agua
Rt = 6
Ro = 0.7
ho = 14
g  = 9.8

#Variables del Cono


#Delta del Tiempo
dt = 0.25

#Varaibles del Agua
h = ho
Ra = Rt
t = 0

plt.plot([-Rt,Rt,0,0,-Rt],[ho,ho,0,0,ho])
linea,=plt.plot([-Rt,Rt],[ho,ho])

#Constantes:
Ch = np.sqrt(ho)
Cr = (Ro/Rt)**2
Cx = ((-3)*(np.sqrt(2*g)))/2

for i in range(150):
    h = (Cx*Cr*t + Ch)**2
    Ra = (h*Rt)/(ho)
    linea.set_ydata([h,h])
    linea.set_xdata([-Ra,Ra])
    plt.pause(0.1)
    t = t + dt