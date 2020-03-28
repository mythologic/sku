import pytest

from sku import RangeScaler, NumberBinarizer
from sku import ItemVectorizer, ItemEncoder

ie = ItemEncoder()
X = ['a', 'b', 'c']
ie.fit(X)
ie.transform(X)
ie.transform(['a', 'z'])
ie.transform('a')
ie.inverse_transform(1)
ie.inverse_transform([1, 2])







def test_range_scaler():
    rs = RangeScaler(out_range=(0, 10), floor=0, round=True)
    x = [30, 50, 100, 90, 80, 40]
    rs.fit(x)
    result = rs.transform(x)
    assert result == [3, 5, 10, 9, 8, 4]

def test_number_binarizer():
    nb = NumberBinarizer(bins=4)
    result = nb.fit_transform(range(10))
    assert result == [0, 0, 0, 1, 1, 2, 2, 3, 3, 3]


# from itemvec import ItemVectorizer
#
# @pytest.fixture
# def X():
#     data = np.array([
#         'this is a sentence',
#         'this is also a sentence',
#         'this is not a sentence'
#     ])
#     return data
#
# @pytest.fixture
# def products():
#     data = np.array([
#         'reeses, kitkat, skittles',
#         'kitkat, smarties, reeses',
#         'smarties, rockets, jubejubes'
#     ])
#     return data
#
# def test_comma_delimiter(products):
#     iv = ItemVectorizer(delimiter=',')
#     iv.fit(products)
#     assert iv.items_ == ['reeses', 'kitkat', 'skittles', 'smarties', 'rockets', 'jubejubes']
#
# def test_sentence_vectorization(X):
#     iv = ItemVectorizer(delimiter=' ')
#     iv.fit(X)
#     result = iv.transform(X).todense() == np.array([
#         [1, 1, 1, 1, 0, 0],
#         [1, 1, 1, 1, 1, 0],
#         [1, 1, 1, 1, 0, 1]])
#     assert result.all()
