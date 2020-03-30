import pytest

from sku import NumberBinarizer

@pytest.fixture
def nb():
    nb = NumberBinarizer(bins=4)
    X = list(range(10))
    nb.fit(X)
    return nb

def test_number_binarizer(nb):
    assert nb.transform(list(range(10))) == [0, 0, 0, 1, 1, 2, 2, 3, 3, 3]
