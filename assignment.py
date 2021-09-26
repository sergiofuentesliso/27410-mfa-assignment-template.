import numpy as np


# Metabolic Flux Analysis

# 1. Write down the stoichiometry matrix S for the model as a numpy array.
# The order of the rows should correspond to A, B and C.
# The order of the columns should correspond to v1-v6
# The reaction formulas are:
# v1: 1 A -> 1 B
# v2: 1 A -> 1 C
# v3: 1 C -> EX_v3
# v4: 1 C -> EX_v4
# v5: 1 B -> Ex_v5
# v6: EX_v6 -> 1 A

# replace [[]] with the stoichiometric matrix.


S = np.array([[-1,-1,0,0,0,1], [1,0,0,0,-1,0],[0,1,-1,-1,0,0]])
S

v = Matrix(symbols("v1:7")) # Use the symbolic math library `sympy` to carry out Sv = 0  symbolically to check if the balances are correct.
Equality(Matrix(S) * v, 0, evaluate=False) # How do you know it's correct? 



# 2. Calculate how many fluxes need to be measured (degrees of freedom).

# Assign your solution to the following variable (replace _ with your solution;
# cannot be just a number; should be a computation based on S)
from numpy.linalg import matrix_rank
S.shape
S.shape[1]
matrix_rank(S)
degrees_of_freedom = S.shape[1] - matrix_rank(S) # columnas - filas
degrees_of_freedom

# 3. Based on measured fluxes v4 = 2.5, v5 = 2, and v6 = -10, calculate v1-v3.


# Put you're intermediate steps here ...

S_c = np.array(S[:,0:3])
S_m = np.array(S[:,3:])
v_m = np.array([2.5,2,-10])

# Assign the final solution here (replace _ with your final step) ;  v_c needs to be a numpy.array containing the three calculated fluxes v1-v3
# Ideally you should get to v_c through a computation involving S and the measured fluxes v4-v6 as covered in the lecture.

### ¡¡¡ SIGNO FLUJOS |abs| ????? !!! 

V_c = -np.linalg.inv(S_c).dot(S_m.dot(v_m))
V_c                                             # I copy output to line 62
v_c = np.array([  2. , -12. , -14.5])


# Tests come in the end
###### Don't touch
def test_stoichiometry_matrix():
    assert hashlib.md5(S.astype(int)).digest() == b'\x97V\x01\xe6\x14\x96\x05p\xda~?.\x9b\xc0.\x87'

def test_degrees_of_freedom():
    assert degrees_of_freedom == 3

def test_mfa_calculation():
    assert v_c.sum() == 15.5
