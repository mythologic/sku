import pytest

from sku import ItemVectorizer

@pytest.fixture
def iv():
    X = ['a,b,c', 'b,c', 'a,c,d,e,f', 'b']
    iv = ItemVectorizer()
    iv.fit(X)
    return iv

def test_transform_list(iv):
    assert iv.transform(['a,b,c', 'b,c', 'a,c,d,e,f', 'b']) == [
        [1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 0, 0],
        [1, 0, 1, 1, 1, 1],
        [0, 1, 0, 0, 0, 0]
    ]

def test_transform_single(iv):
    assert iv.transform('a') == [1, 0, 0, 0, 0, 0]

def test_transform_missing(iv):
    assert iv.transform('a,z') == [1, 0, 0, 0, 0, 0]

def test_list_double(iv):
    assert iv.transform(['b,d', 'a,a']) == [[0, 1, 0, 1, 0, 0], [1, 0, 0, 0, 0, 0]]

def test_inverse_single(iv):
    assert iv.inverse_transform([1, 1, 0, 1, 0]) == 'a,b,d'

def test_inverse_list(iv):
    assert iv.inverse_transform([[0, 0, 0, 0, 0, 1], [1, 1, 0, 0, 0, 0]]) == ['f', 'a,b']
