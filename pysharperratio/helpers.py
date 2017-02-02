
import numba
import numpy as np
import pandas as pd

numba.jit()
def compute_r0(x):
    """ Computeds r0
    
    Parameters
    ----------
    x:  numpy array of shape = [n_samples]
        A (non-empty) numeric vector of increments (e.g. returns).
    
    Example
    -------
    x = numpy.random.rand(1000)
    r0 = compute_r0(x)
    
    Returns
    -------
    r0: The number of upper records minus lower records over the 
        cumulated sum of x.
    
    """   
    # Compute the rolling maximum of the log returns
    rolling_max = pd.expanding_max(np.cumsum(x),min_periods=1)
    
    # Compute the rolling minimum of the log returns
    rolling_min = pd.expanding_min(np.cumsum(x),min_periods=1)
    
    # Get the number of unique values for each. This should signal the unique jumps in each case. 
    uppers = np.unique(rolling_max).shape[0]
    downers = np.unique(rolling_min).shape[0]
    
    # Compute the difference to get R0
    r_0 = uppers - downers
    
    return r_0