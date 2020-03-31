"""
functional MRI module for NeuroImaging in python
--------------------------------------------------

Documentation is available in the docstrings and online at
http://nistats.github.io.

Contents
--------
Nistats is a Python module for fast and easy functional MRI statistical
analysis.

Submodules
---------
datasets                --- Utilities to download NeuroImaging datasets
hemodynamic_models      --- Hemodyanmic response function specification
design_matrix           --- Design matrix creation for fMRI analysis
experimental_paradigm   --- Experimental paradigm files checks and utils
model                   --- Statistical tests on likelihood models
regression              --- Standard regression models
first_level_model       --- API for first level fMRI model estimation
second_level_model      --- API for second level fMRI model estimation
contrasts               --- API for contrast computation and manipulations
thresholding            --- Utilities for cluster-level statistical results
reporting               --- Utilities for creating reports & plotting data
utils                   --- Miscellaneous utilities
"""

import warnings
from distutils.version import LooseVersion

import nilearn

from .version import _check_module_dependencies, __version__


def _nistats_deprecation_warning():
    warning_msg = (
        '\n\n'
        ' | Starting with Nilearn 0.7.0, all Nistats functionality '
        "has been incorporated into Nilearn's stats & reporting modules.\n"
        ' | Nistats package will no longer be updated or maintained.\n')
    warnings.filterwarnings('once', message=warning_msg)
    warnings.warn(message=warning_msg,
                  category=FutureWarning,
                  stacklevel=4)


def _nistats_redundant_warning():
    warning_msg = (
        '\n\n'
        ' | Using Nistats with Nilearn versions >= 0.7.0 '
        'is redundant and potentially conflicting.\n'
        ' | Nilearn versions 0.7.0 and up offer all the functionality of Nistats '
        'as well the latest features and fixes.\n'
        ' | We strongly recommend uninstalling Nistats and using '
        "Nilearn's stats & reporting modules.\n")
    warnings.filterwarnings('once', message=warning_msg)
    warnings.warn(message=warning_msg,
                  stacklevel=4)


def _nistats_retirement_warning():
    nilearn_version = LooseVersion(nilearn.__version__)
    if nilearn_version.version[1] > 6:
        _nistats_redundant_warning()
    else:
        _nistats_deprecation_warning()


_check_module_dependencies()
_nistats_retirement_warning()

__all__ = ['__version__', 'datasets', 'design_matrix']
