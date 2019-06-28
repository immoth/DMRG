# -*- coding: utf-8 -*-
"""
Created on Thu May 30 11:36:37 2019

@author: jsten
"""

import numpy as np
import matplotlib.pyplot as plt
import time
from cmath import *
import scipy.linalg as lng
import copy
import Hamiltonain_MPO
import mps

def Dmps(Mps,l,d,D,Dp):
    mtp=copy.deepcopy(Mps);
    dd=len(mtp)
    L=len(mtp[0])
    DD=len(mtp[0][l])
    DDp=len(mtp[0][l][0])
    for ds in range(0,dd):
        mtp[ds][l]=np.zeros([DD,DDp])
    mtp[d][l][D][Dp]=1.0
    return mtp

"can be made more efficient by calculating Dmps only once for each parameter"
"only works for 0<l<L-1"
def DE(Mps,l):
    mtp=copy.deepcopy(Mps)
    dd=len(mtp)
    L=len(mtp[0])
    DD=len(mtp[0][l])
    DDp=len(mtp[0][l][0]) 
    eT=[]
    nT=[]
    for d1 in range(0,dd):
        for D1 in range(0,DD):
            for Dp1 in range(0,DDp):
                eTT=[]
                nTT=[]
                for d2 in range(0,dd):
                    for D2 in range(0,DD):
                        for Dp2 in range(0,DDp):
                            dmps1=Dmps(mtp,l,d1,D1,Dp1)
                            dmps2=Dmps(mtp,l,d2,D2,Dp2)
                            dE=Hamiltonain_MPO.E(dmps1,dmps2)
                            dN=mps.Norm(dmps1,dmps2)
                            eTT.append(dE)
                            nTT.append(dN)
                eT.append(eTT)
                nT.append(nTT)
    return([np.array(eT),np.array(nT)])




