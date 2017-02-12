import numpy as np
import pandas as pd
import pickle
import os

from scipy import stats

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

def estimateSNR(x,permutations=1000):
    """A moment-free Sharpe (signal-to-noise) ratio estimator.

    This function accepts a vector of price returns (or any possibly heavy-tailed
    data) and returns a list containing the moment-free estimator, the vanilla
    estimator.

    Parameters
    ----------
    x : numpy array of shape = [n_samples]
        A (non-empty) numeric vector of values.

    permutations:
        The basic assumption of the estimator is that the sample data
        are independent and indentically distributed. To improve the efficiency
        (precision) of the test, it is a good idea to average it over several random
        index permutations.

    Example
    -------
    >>> x = numpy.random.rand(100)
    >>> snr,r0bar,n = estimateSNR(x,numPerm=1000)


    Returns
    -------
    snr:  The signal-to-noise ratio. To have something comparable with
          a t-statistics, multiply by sqrt(length(x)).

    r0bar:  The average number of upper records minus lower records over
            the permutations of the cumulated sum of x.

    n:  The length of the vector x. It may be smaller than the input
        length if x contains NaNs.

    """
    N = x.shape[0]

    # Compute nu
    nu, _, _ = stats.t.fit(x)

    # Compute r0bar over permutations
    r0bar = np.mean([compute_r0(x[np.random.permutation(x.shape[0])])
                     for perm in range(permutations)])

    # Load spline
    with open(os.path.join(os.path.dirname(__file__),
                           '..', 'interpolator.pkl'), 'rb') as f:
        f_a = pickle.load(f)

    # Compute signal to noise ratio
    snr = np.sign(r0bar/N)*f_a(np.abs(r0bar/N))*(1.0-8.0/3.0 * nu**(-1.5))

    # Return snr
    return snr
