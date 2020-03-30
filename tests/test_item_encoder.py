import pytest

from sku import ItemEncoder

@pytest.fixture
def ie():
    X = ['a', 'b', 'c']
    ie = ItemEncoder().fit(X)
    return ie

def test_transform_list(ie):
    assert ie.transform(['a', 'b', 'c']) == [0, 1, 2]

def test_transform_missing(ie):
    assert ie.transform(['a', 'z']) == [0, None]

def test_transform_single(ie):
    assert ie.transform('a') == 0

def test_inverse_list(ie):
    assert ie.inverse_transform([1, 2]) == ['b', 'c']

def test_inverse_single(ie):
    assert ie.inverse_transform(1) == 'b'
