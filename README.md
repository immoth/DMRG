# DMRG
A density functional renormalization group solver using matrix product states

## Running The Program
0) Insure that all files are downloaded into the same folder
1) Open the DMRG.py file (this is the main programe file.  No other files need to be open to run the program.)
3) The program is no ready to run.  The following steps discuss chossing the parameters of the code.
      a) In DMRG.py line 21 reads x=mps.MPS(5,2,2).  This generates the initial matrix product state.  The function MPS takes three 
         parameters.  First is the number of sites (currently set to 5).  Second is the physical dimension of each site (set to 2). 
         The last is the inital bond dimension of each site (set to 2).  Each of these can be adjusted as needed.
      b) The Hamiltonian is defined in...   
