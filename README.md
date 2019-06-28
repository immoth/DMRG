# DMRG
A density functional renormalization group (DMRG) solver using matrix product states (MPS)

## Running The Program
0) Insure that all files are downloaded into the same folder
1) Open the DMRG.py file (this is the main programe file.  No other files need to be open to run the program.)
3) The program is no ready to run.  The following steps discuss chossing the parameters of the code.

      a) In DMRG.py line 21 reads "x=mps.MPS(5,2,2)".  This generates the initial matrix product state.  The function MPS takes three 
         parameters.  First is the number of sites (currently set to 5).  Second is the physical dimension of each site (set to 2). 
         The last is the inital bond dimension of each site (set to 2).  Each of these can be adjusted as needed.
         
      b) The Hamiltonian is defined in Hamiltonain_MPO.py (Note the miss spelling in the file name).  Line 97 of Hamiltonain_MPO reads
         "etp+=H(mpsA,hzz,mpsB,k)+H(mpsA,hx,mpsB,k)" where hx is defined on line 82 and hzz is defined on line 73.  The user can define 
         their own Hamiltonian h_user and edit line 97 so that it reades "etp+=H(mpsA,h_user,mpsB,k)."  The function h_user(d1,d2,d3,d4) 
         must be function of the physical deminsions of two neighboring sites as follows: for a matrix Hamiltonian d1 is the row of site 1,
         d2 is the row of site 2, d3 is the collumn of site 1, and d4 is the collumn of site 2.  
    
4) The program outputs: 
      a) The normalization of the MPS (if it is not 1.0 then there is a bug)
      b) The ground state energy after each iteration
      c) A plot of the ground state energy vs iteration step (if the energy has not converged then DMRG has failed).
         
## Comming Soon
1) I will be making Hamiltonian input more user friendly.  In the future, the user will be able to give the Hamiltonian in terms of creation 
   and destruction operators.
2) I am working on a GUI for parameter input
3) I believe the speed of the program can be improved by optimizing certain functions.  I am working towards full optimization.

## Description of Each File
DMRG.py: This is the main program file

Cononical_Form.py: This is called by DMRG.py during each iteration to prepare the MPS in the appropriate canonical form

Optimize.py: This is where the real number crunching takes place.  This is called by DMRG.py to optimize the MPS during each iteration

Derivative.py: This takes the derivative of the MPS.  This is called by Optimize.py to find the extreme of the local Shrodinger equation.

mps.py: This creates an arbitrary MPS and normalizes it.  This is called in DMRG.py to initalize the MPS.

Hamiltonain.py: This describes the Hamiltonian and calulates the energy expectation value.  This is called by Derivative.py to calculate the                  
                derivative of expectation values.
