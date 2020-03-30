import pytest

from sku import RangeScaler

@pytest.fixture
def rs():
    X = [30, 50, 100, 90, 80, 40]
    rs = RangeScaler(out_range=(0, 10), floor=0, round=True)
    rs.fit(X)
    return rs

def test_transform_list(rs):
    assert rs.transform([30, 50, 100, 90, 80, 40]) == [3, 5, 10, 9, 8, 4]

def test_transform_one(rs):
    assert rs.transform(30) == 3

def test_one_out_of_range(rs):
    assert rs.transform(200) == 20
