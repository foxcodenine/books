# IPYTHON $ JUPYTER NOTEBOOK


# from ipython shell you can do #run to run it:
# %run hello_world.py 

# ______________________________________________________________________

# ipython use pretty-print.

from numpy.random import randn

data = {i: randn() for i in range(7)}

# ______________________________________________________________________

# to open jupyter notebook enter j.. n.. while in conda base env.

    # $ jupyter notebook

# ______________________________________________________________________

# Tab Completion

_secret_key = 'xjfjhsdbfjvhbsdjbfv'

# _<Tab>                                       <- auto comlete variables

# _secret_ket.<Tab>                            <- auto comlete function

#  path = '/home/foxcodenine/git/'<Tab>        <- auto comlete path

# %run ch<Tab>                                 <- combined with %run


# ______________________________________________________________________

# Introspection (using ?)

b = [1, 2, 3]

# b?                

# print?

# ------------------------------

def add_numbers(a, b):
    '''
    Add two numbers together.

    Returns
    _______
    the sum : tye of arguments
    '''
    return a + b

# add_numbers?      <- shows docstring
# add_numbers??     <- shows docstring & source code

# ------------------------------

# also combined with * it will show all names matching the wildcard:

#  >> import numpy as np 
#  >> np.*load*?
# np.__loader__
# np.load
# np.loads
# np.loadtxt

# ______________________________________________________________________

# The %run Command

# %run script_test.py
# %run -i script_test.py  <-scripy file can assess variables aleady defined in ipython


print(a)