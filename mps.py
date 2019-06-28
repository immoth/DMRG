# -*- coding: utf-8 -*-
"""
Created on Wed May 22 11:51:40 2019

@author: jsten
"""

import numpy as np
import matplotlib.pyplot as plt
import time
from cmath import *
import scipy.linalg as lng
import copy


"creats a random matrix of size DDxDD"
def M(DD):
    return np.random.uniform(0,1,size=(DD,DD))

"creats a random vector of size DD"
def V(DD):
    return np.random.uniform(0,1,size=DD)

"creats a random matrix product state with L sites and physical dimension dd and bond dimension DD"
def MPS(L,DD,dd):
    mttp=[]
    for d in range(0,dd):
        mtp=[V(DD)]
        for l in range(1,L-1):
            mtp.append(M(DD))
        mtp.append(V(DD))
        mttp.append(mtp)
    return mttp
        
"finds the coeficient given an MPS and a configuration"
def Coef(mps,cfig):
    mtp=copy.deepcopy(mps)
    ctp=mtp[cfig[0]][0]
    for i in range(1,L):
        ctp=np.dot(ctp,mtp[cfig[i]][i])
    return ctp

"Find the dot product of two states writen as mps"
"Assumes real numbers" 
"All matrix products return square matrices so no DDp"   
def Norm(mps1,mps2):
    mtp1=copy.deepcopy(mps1)
    mtp2=copy.deepcopy(mps2)
    dd=len(mtp1)
    L=len(mtp1[0])
    DD=len(mtp1[0][L-1])
    nttp=np.zeros([DD,DD]) 
    for d in range(0,dd): 
        for D in range(0,DD):
            for Dp in range(0,DD):
                nttp[D][Dp]+=mtp1[d][L-1][D]*mtp2[d][L-1][Dp]
    for l in range(2,L):
        DD=len(mtp1[0][L-l])
        nttpp=np.zeros([DD,DD])
        for d in range(0,dd):
            nttpp+=np.dot(mtp1[d][L-l],np.dot(nttp,np.transpose(mtp2[d][L-l])))
        nttp=nttpp
    nttpp=0
    for d in range(0,dd):
        nttpp+=np.dot(mtp1[d][0],np.dot(nttp,mtp2[d][0]))
    nttp=nttpp
    return nttp

    
    
"returns a normalized MPS from any other MPS"
def nMPS(Mps):
    mtp=copy.deepcopy(Mps)
    ntp=Norm(mtp,mtp)
    dd=len(mtp)
    L=len(mtp[0])
    for d in range(0,dd):
        for l in range(0,L):
            mtp[d][l]=mtp[d][l]/np.power(ntp,1/(2*L))      
    return mtp






