import sys
import warnings

# import time warnings don't interfere with warning's tests
import pytest

with warnings.catch_warnings(record=True):
    from nistats import (_nistats_deprecation_warning,
                         _nistats_redundant_warning,
                         )


def test_nistats_deprecation_warning():
    with pytest.warns(
        FutureWarning,
        match='\n\n | Starting with Nilearn 0.7.0, all Nistats functionality ',
        ):
        _nistats_deprecation_warning()


def test_nistats_redundant_warning():
    with pytest.warns(
        UserWarning,
        match='\n\n | Using Nistats with Nilearn versions >= 0.7.0 ',
        ):
        _nistats_redundant_warning()


def test_warnings_filter_scope():
    """
    Tests that warnings generated at Nistats import in Python 2, 3.4 envs
    do not change the warnings filter for subsequent warnings.
    """
    with warnings.catch_warnings(record=True) as raised_warnings:
        warnings.warn('Dummy warning 1')  # Will be raised.
        warnings.filterwarnings("ignore", message="Dummy warning")
        warnings.warn('Dummy warning 2')  # Will not be raised.
        import nistats  # Irrespective of warning in py2, py3.4 # noqa:F401
        warnings.warn('Dummy warning 3')  # ...this should not be raised.
    assert str(raised_warnings[0].message) == 'Dummy warning 1'
    assert str(raised_warnings[-1].message) != 'Dummy warning 3'
