"""
Sample Test
"""
# pylint: disable=redefined-outer-name, unused-argument

import pytest
import sample.main


@pytest.fixture
def sample_fixture():
    """Setup test fixture"""
    return 1


def test_func(sample_fixture):
    """Test the sample function"""
    assert sample.main.sample_func(1) == 2


def test_negative(sample_fixture):
    """Negative test of sample function"""
    assert sample.main.sample_func(-2) == -1
