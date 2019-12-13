====================
Keywords Distribution Analysis
====================

Overview
===========

- This repository is an analysis of the `Google Ads <https://ads.google.com/>`_ `Keywords <https://support.google.com/google-ads/answer/6323?hl=en>`_
distributions for the Account X and Account Y. Performance of every Keyword (Clicks, Impressions, ROAS, etc.) is a random
process.

- `Keywords <https://support.google.com/google-ads/answer/6323?hl=en>`_ can have very different purposes: e.g. there are ones
with Brand name ("Puma sneakers") to pick audience, which already seeks for specific products or Generic ones ("sneakers")
to catch customers, who are just wandering around. In theory groups from the example above are very different ones and should
be treated separately. So it is important to understand, which groups of `Keywords <https://support.google.com/google-ads/answer/6323?hl=en>`_ have
the same performance distribution and which do not.
| P.S. Speaking math, we are just comparing distibutions over here.

- Also, it's a good idea to look at dynamics of `Keywords <https://support.google.com/google-ads/answer/6323?hl=en>`_ distributions
to see, if changes being made in the account lead to healthier performance with time. And it gives us better insight, than
just looking at graph of some mean statistic vs time.


Installation
===========

Make sure you have Python3.7, git, virtualenv installed.

- For Linux:

.. code-block:: bash

    git clone git@github.com:bluella/keywords-distribution-analysis.git
    cd keywords-distribution-analysis
    virtualenv -p /usr/bin/python3.7 ds_env
    source ds_env/bin/activate
    pip install -r requirements.txt

- For Mac:

.. code-block:: bash

    git clone git@github.com:bluella/keywords-distribution-analysis.git
    cd keywords-distribution-analysis
    virtualenv -p /usr/local/bin/python3.7 ds_env
    source ds_env/bin/activate
    pip install -r requirements.txt


Workflow
========

Few things were done:

- Datesets were created with `Google Ads Reports <https://support.google.com/google-ads/answer/6201327?hl=en>`_

- Visual comparison of monthly distributions

- Visual comparison of distributions of a few keywords groups

- Hypothesis testing of distributions being different from each other.

Done with four tests for three timeframes (August, September, October):

    - `Brown–Forsythe test <https://en.wikipedia.org/wiki/Levene%27s_test>`_ , `Scipy docs <https://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.stats.levene.html>`_

    - `Wilcoxon Rank-Sum Test <https://en.wikipedia.org/wiki/Wilcoxon_signed-rank_test>`_ , `Scipy docs <https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.wilcoxon.html>`_

    - `Kolmogorov - Smirnov test <https://en.wikipedia.org/wiki/Kolmogorov%E2%80%93Smirnov_test>`_ , `Scipy docs <https://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.stats.ks_2samp.html>`_

    - `Kruskal - Wallis test <https://en.wikipedia.org/wiki/Kruskal%E2%80%93Wallis_one-way_analysis_of_variance>`_ , `Scipy docs <https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.kruskal.html>`_

Those were picked because:

    - distributions are clearly not Gaussian, so we need nonparametric tests
    - sample sizes are different
    - tests look at different properties of distributions

Results
===========

- Via doing various testing on the multiple timeframes, we are ensuring robustness of our results.
- Distributions from Account X send us mixed signals, so we fail to reject null Hypothesis, that random variables come from the same distribution.
- Distributions from Account Y are clearly different ones. Null is reject by every test. Graphs suggest the same.

Releases
========

See `CHANGELOG <https://github.com/bluella/keywords-distribution-analysis/blob/master/CHANGELOG.rst>`_.

License
=======

This project is licensed under the MIT License -
see the `LICENSE <https://github.com/bluella/keywords-distribution-analysis/blob/master/LICENSE.txt>`_ for details.
