# DMRG
A density functional renormalization group solver using matrix product states

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
