# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 10:52:45 2019

@author: jsten
"""

import numpy as np

"spin matrices"
s0=np.array([[1,0],[0,1]])
sx=np.array([[0,1],[1,0]])
sy=np.array([[0,1j],[-1j,0]])
sz=np.array([[1,0],[0,-1]])
z=s0-s0
sp=1/2*(sx+1j*sy)
sm=1/2*(sx-1j*sy)

def k4(a,b,c,d):
    return np.kron(a,np.kron(b,np.kron(c,d)))

def dot8(a,b,c,d,e,f,g,h):
    return np.dot(a,np.dot(b,np.dot(c,np.dot(d,np.dot(e,np.dot(f,h))))))
                  
"four creation=a and destruction=b operators"
a1=k4(sp,s0,s0,s0)
b1=k4(sm,s0,s0,s0)
a2=k4(sz,sp,s0,s0)
b2=k4(sz,sm,s0,s0)
a3=k4(sz,sz,sp,s0)
b3=k4(sz,sz,sm,s0)
a4=k4(sz,sz,sz,sp)
b4=k4(sz,sz,sz,sm)
i0=k4(s0,s0,s0,s0)

"nearest neighbor hopping"
Hl=dot8(a1,b3,i0,i0,i0,i0,i0,i0)+dot8(a3,b1,i0,i0,i0,i0,i0,i0)+dot8(a2,b4,i0,i0,i0,i0,i0,i0)+dot8(a4,b2,i0,i0,i0,i0,i0,i0)

"Translates the matrix Hl in the function h of bond dimensions used in DMRG"
"each D runs over occupation and spin"
def h(D1,D1p,D2,D2p):
    htp=Hl[4*D2+D1][4*D2p+D1p]
    return htp
    