# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 13:02:24 2019

@author: jsten
"""
import numpy as np
import matplotlib.pyplot as plt
import time
from cmath import *
import scipy.linalg as lng
import copy

"Need to make RCon and LCon work for a general dd" 


"not up to date"
def RightCheck(Mps):
    mtp=copy.deepcopy(Mps)
    dd=len(mtp)
    L=len(mtp[0])
    DD=len(mtp[0][0])
    Mtemp=np.zeros([DD,DD])
    for d in range(0,dd):
        for D in range(0,DD):
            for Dp in range(0,DD):
                Mtemp[D][Dp]=Mtemp[D][Dp]+np.transpose(mtp[d][0])[D]*mtp[d][0][Dp]
    print(Mtemp)
    for l in range(1,L-1):
        Mtemp=np.zeros(y[0][l].shape)
        for d in range(0,dd):
            Mtemp=Mtemp+np.dot(np.transpose(mtp[d][l]),mtp[d][l])
        print(Mtemp)
    Mtemp=0.0
    for d in range(0,dd):
        Mtemp=Mtemp+np.dot(np.transpose(mtp[d][L-1]),mtp[d][L-1])
    print(Mtemp)
    
"not up to date"
def LeftCheck(Mps):
    mtp=copy.deepcopy(Mps)
    dd=len(mtp)
    L=len(mtp[0])
    DD=len(mtp[0][0])
    Mtemp=0
    for d in range(0,dd):
        Mtemp=Mtemp+np.dot(mtp[d][0],np.transpose(mtp[d][0]))
    print(Mtemp)  
    for l in range(1,L-1):
        Mtemp=np.zeros(y[0][l].shape)
        for d in range(0,dd):
            Mtemp=Mtemp+np.dot(mtp[d][l],np.transpose(mtp[d][l]))
        print(Mtemp)  
    Mtemp=np.zeros([DD,DD])
    for d in range(0,dd):
        for D in range(0,DD):
            for Dp in range(0,DD):
                Mtemp[D][Dp]=Mtemp[D][Dp]+np.transpose(mtp[d][L-1])[D]*mtp[d][L-1][Dp]
    print(Mtemp)          
    
def RCon(Mps,l):
    mtp=copy.deepcopy(Mps)
    dd=len(mtp)
    L=len(mtp[0])
    DD=len(mtp[0][l])
    toStack=[mtp[0][l]]
    for d in range(1,dd):
        toStack.append(mtp[d][l])
    stack= np.vstack(toStack)
    SVD=lng.svd(stack,full_matrices=False)
    s=SVD[0]
    DG=np.diag(SVD[1])
    v=SVD[2]
    if l==0:
        for d in range(0,dd):
            mtp[d][0]=s[d]
            mtp[d][1]=np.dot(DG,np.dot(v,mtp[d][1]))
    elif l==L-2:
        DDp=len(mtp[0][l][0])
        for d in range(0,dd):
            mtp[d][l]=s[d*DD:(d+1)*DD,0:DDp]
            mtp[d][l+1]=np.dot(DG,np.dot(v,mtp[d][l+1]))
    else:
        DDp=len(mtp[0][l][0])
        for d in range(0,dd):
            mtp[d][l]=s[d*DD:(d+1)*DD,0:DDp]
            mtp[d][l+1]=np.dot(DG,np.dot(v,mtp[d][l+1]))
    return mtp

"Transposes a MPS"
def TAll(Mps):
    mtp=copy.deepcopy(Mps)
    mttp=copy.deepcopy(Mps)
    dd=len(mtp)
    L=len(mtp[0])
    DD=len(mtp[0][0])
    for l in range(0,L):
        for d in range(0,dd):
            mttp[d][L-l-1]=np.transpose(mtp[d][l])
    return mttp
    

def LCon(Mps,l):
        mtp=copy.deepcopy(Mps)
        L=len(mtp[0])
        mtp=TAll(mtp)
        mtp=RCon(mtp,L-1-l)
        mtp=TAll(mtp)
        return mtp
"""                
z1=LCon(y,4)
z2=LCon(z1,3)
z3=LCon(z2,2)
z4=LCon(z3,1)
"print(LeftCheck(z4))"



y1=RCon(y,0)
y2=RCon(y1,1)
y3=RCon(y2,2)
y4=RCon(y3,3)
"print(RightCheck(y4))"

m1=RCon(y,0)
m2=RCon(m1,1)
m3=LCon(m2,4)
m4=LCon(m3,3)
print(RightCheck(m4))
print(LeftCheck(m4))

print([E(y,y),E(y4,y4),E(z4,z4),E(m4,m4)])
"""

