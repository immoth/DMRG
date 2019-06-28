# -*- coding: utf-8 -*-
"""
Created on Fri May 31 13:24:09 2019

@author: jsten
"""

import numpy as np
import matplotlib.pyplot as plt
import time
from cmath import *
import scipy.linalg as lng
import copy

import mps 
import Derivative
import Cononical_Form
import Hamiltonain_MPO
import Optimize

x=mps.MPS(5,3,2)
y=mps.nMPS(x)
print(mps.Norm(y,y))
dd=len(y)
L=len(y[0])
DD=len(y[0][0])

"""
eplt=[]
for t in range(0,9):
    for l in range(1,L-1):
        y=Opt(y,l)
        etmp=E(y,y)
        eplt.append(etmp)
        print([t,etmp])




plt.plot(eplt)
"""

eplt=[]
yT=[]
"end vectors blow up for MPS(5,3,2)"
"I think im doing LCon from the wrong direction"
for t in range(0,5):
    y=Cononical_Form.RCon(y,0)
    yT.append(y)
    for l in range(1,L-1):
        y=Cononical_Form.LCon(y,L-l)
    for l in range(1,L-1):
        y=Optimize.Opt(y,l)
        yT.append(y)
        etmp=Hamiltonain_MPO.E(y,y)
        eplt.append(etmp)
        print([t,etmp])
        y=Cononical_Form.RCon(y,l)
        yT.append(y)




plt.plot(eplt)