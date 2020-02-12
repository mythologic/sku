import numpy as np
import pytest

from itemvec import ItemVectorizer

@pytest.fixture
def X():
    data = np.array([
        'this is a sentence',
        'this is also a sentence',
        'this is not a sentence'
    ])
    return data

@pytest.fixture
def products():
    data = np.array([
        'reeses, kitkat, skittles',
        'kitkat, smarties, reeses',
        'smarties, rockets, jubejubes'
    ])
    return data

def test_comma_delimiter(products):
    iv = ItemVectorizer(delimiter=',')
    iv.fit(products)
    assert iv.items_ == ['reeses', 'kitkat', 'skittles', 'smarties', 'rockets', 'jubejubes']

def test_sentence_vectorization(X):
    iv = ItemVectorizer(delimiter=' ')
    iv.fit(X)
    result = iv.transform(X).todense() == np.array([
        [1, 1, 1, 1, 0, 0],
        [1, 1, 1, 1, 1, 0],
        [1, 1, 1, 1, 0, 1]])
    assert result.all()
