pySharpeRratio
==============

Description
-----------

This package implements a moment-free estimator of the Sharpe
(signal-to-noise) ratio. The algorithm does not require the computation
of any moments by estimating the Sharpe ratio based on the cumulative
sum of (i.i.d.) increments or returns. This algorithm is much more
precise (efficient) when increments are heavy-tailed.

The estimator computes the difference between the drawdown and drawup
durations. First, the cumulative sum of x (e.g. prices) is computed,
then the total drawdown and drawup durations are computed. Precision is
improved by averaging the estimator on several random permutations of x.

Author & Maintainer: Amir Sani
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Reference
---------

Challet, Damien. "Sharper asset ranking from total drawdown durations."
arXiv preprint arXiv:1505.01333 (2015).

Bibtex
~~~~~~

@article{challet2015sharper, title={Sharper asset ranking from total
drawdown durations}, author={Challet, Damien}, journal={arXiv preprint
arXiv:1505.01333}, year={2015} }

Copyright (c) 2017, Amir Sani
-----------------------------
