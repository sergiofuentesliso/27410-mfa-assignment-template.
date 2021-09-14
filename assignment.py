
###### Ignore this
import pytest
import hashlib
_ = 123456789  # just a wrong number, please ignore
###### Stop ignoring

import numpy as np

# Metabolic Flux Analysis

# 1. Write down the stoichiometry matrix S for the model as a numpy array.
# The order of the rows should correspond to A, B and C.
# The order of the columns should correspond to v1-v6
# The reaction formulas are:
# v1: 1 A -> 1 B
# v2: 1 A -> 1 C
# v3: 1 C ->
# v4: 1 C ->
# v5: 1 B ->
# v6: 1 A -> 

# replace [[]] with the stoichiometric matrix.
S = np.array([[]])


# 2. Calculate how many fluxes need to be measured (degrees of freedom).

# Assign your solution to the following variable (replace _ with your solution;
# cannot be just a number; should be a computation based on S)

degrees_of_freedom = _


# 3. Based on measured fluxes v4 = 2.5, v5 = 2, and v6 = 10, calculate v1-v3.

# Put you're intermediate steps here ...

# Assign the final solution here (replace _ with your final step)
# v_c needs to be a numpy.array containing the three calculated fluxes v1-v3
# Ideally you should get to v_c through a computation involving S and the
# measured fluxes v4-v6 as covered in the lecture.

v_c = _


# Tests come in the end
###### Don't touch
def test_stoichiometry_matrix():
    assert hashlib.md5(S.astype(int)).digest() == b'\x97V\x01\xe6\x14\x96\x05p\xda~?.\x9b\xc0.\x87'

def test_degrees_of_freedom():
    assert degrees_of_freedom == 3

def test_mfa_calculation():
    assert v_c.sum() == 15.5
###### this
