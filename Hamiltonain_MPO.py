# -*- coding: utf-8 -*-
"""
Created on Fri May 24 11:42:50 2019

@author: jsten
"""

import numpy as np
import matplotlib.pyplot as plt
import time
from cmath import *
import scipy.linalg as lng
import copy

"returns the matrix element <MPSa|h_{k,k+1}|MPSb> (i.e. assumes nearest neighbor hopping)"
"k ranges from 0-L-2 (L-1 gives zero)"
"All matrix products return a square matrix so no DDp"
def H(mps1,h,mps2,k):
    mpsA=copy.deepcopy(mps1)
    mpsB=copy.deepcopy(mps2)
    stp=[0.0]
    dd=len(mpsA)
    L=len(mpsA[0])
    for l in range(0,L-1):
        DD=len(mpsA[0][l+1])
        sttp=np.zeros([DD,DD])
        stp.append(sttp)
    if k<L-2:
        DD=len(mpsA[0][L-1])
        nttp=np.zeros([DD,DD]) 
        for D in range(0, DD): 
            for Dp in range(0,DD):
                for d in range(0, dd):
                    nttp[D][Dp]=nttp[D][Dp]+mpsA[d][L-1][D]*mpsB[d][L-1][Dp]
        stp[L-1]=nttp
             
        for l in range(2,L-k):
            DD=len(mpsA[0][L-l])
            nttp=np.zeros([DD,DD])
            for d in range(0,dd):
                nttp= nttp+np.dot(mpsA[d][L-l],np.dot(stp[L-l+1],np.transpose(mpsB[d][L-l])))
                stp[L-l]=nttp
            
            DD=len(mpsA[0][k])
            nttp=np.zeros([DD,DD]) 
            for d1 in range(0,dd):
                for d2 in range(0,dd):
                    for d3 in range(0,dd):
                        for d4 in range(0,dd):
                            nttp=nttp+h(d1,d2,d3,d4)*np.dot(mpsA[d1][k],np.dot(mpsA[d2][k+1],np.dot(stp[k+2],np.dot(np.transpose(mpsB[d3][k+1]),np.transpose(mpsB[d4][k]))))) 
            stp[k]=nttp

    elif k==L-2:
        DD=len(mpsA[0][k])
        nttp=np.zeros([DD,DD]) 
        for d1 in range(0,dd):
            for d2 in range(0,dd):
                for d3 in range(0,dd):
                    for d4 in range(0,dd):
                        nttp=nttp+h(d1,d2,d3,d4)*np.outer(np.dot(mpsA[d1][k],mpsA[d2][k+1]),np.dot(np.transpose(mpsB[d3][k+1]),np.transpose(mpsB[d4][k])))
        stp[k]=nttp

    for l in range(L-k+1,L+1):
        DD=len(mpsA[0][L-l])
        nttp=np.zeros([DD,DD])
        for d in range(0,dd):
            nttp=nttp+np.dot(mpsA[d][L-l],np.dot(stp[L-l+1],np.transpose(mpsB[d][L-l])))
        stp[L-l]=nttp             
    return stp[0][0][0]
"End function"    

"Hamiltonian H= Z_i Z_j+X_i"    
def hzz(d1,d2,d3,d4):
    if d1==d2 and d2==d3 and d3==d4: 
        htp=1 
    else: 
        htp=0
    if d1==d4 and d2==d3 and d1!=d2: 
        htp+=-1 
    return htp

def hx(d1,d2,d3,d4):
    htp=0
    if d1!=d4 and d2==d3:
        htp+=0.5
    if d1==d4 and d2!=d3:
        htp+=0.5
    return htp

"Gives the total energy expectation value"
def E(mps1, mps2):
    mpsA=copy.deepcopy(mps1)
    mpsB=copy.deepcopy(mps2)
    etp=0;
    L=len(mpsA[0])
    for k in range(0,L-1):
        etp+=H(mpsA,hzz,mpsB,k)+H(mpsA,hx,mpsB,k)
    return etp
    