# -*- coding: utf-8 -*-
"""
Created on Fri May 31 12:13:27 2019

@author: jsten
"""

import numpy as np
import matplotlib.pyplot as plt
import time
from cmath import *
import scipy.linalg as lng
import copy
import Derivative
import mps

"only works for 0<l<L-1"
def Opt(Mps,l):
    mtp=copy.deepcopy(Mps)
    dd=len(mtp)
    L=len(mtp[0])
    DD=len(mtp[0][l])
    DDp=len(mtp[0][l][0])
    dee=Derivative.DE(mtp,l)
    hh=dee[0]
    ss=dee[1]
    ht=(hh+np.transpose(hh))/2  
    st=(ss+np.transpose(ss))/2
    egn=lng.eig(ht,st)
    et=egn[0]
    ev=np.transpose(egn[1])

    mini=np.argmin(et)
    for d in range(0,dd): 
        for D in range(0,DD): 
            for Dp in range(0,DDp):
                mtp[d][l][D][Dp]=ev[mini][DD*DDp*d+DDp*D+Dp]
    return mps.nMPS(mtp)

