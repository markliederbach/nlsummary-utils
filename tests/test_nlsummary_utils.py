"""Test package level functionality of nlsummary_utils"""

import nlsummary_utils

def test_has_version():
    """Test that a __version__ attribute is defined."""
    assert hasattr(nlsummary_utils, "__version__")
