<h3 align="center">
  <img src="https://raw.githubusercontent.com/mythologic/sku/master/logo/sku.png" width="300px" alt="sku">
</h3>
<p align="center">
  <a href="https://github.com/mythologic/sku/"><img alt="GitHub" src="https://img.shields.io/github/license/mythologic/sku/"></a>
  <a href="https://travis-ci.org/mythologic/sku/"><img alt="Travis" src="https://img.shields.io/travis/mythologic/sku/.svg"></a>
  <a href="https://pypi.python.org/pypi/sku/"><img alt="PyPI" src="https://img.shields.io/pypi/v/sku/.svg"></a>
  <a href="https://pepy.tech/project/sku"><img alt="Downloads" src="https://pepy.tech/badge/sku"></a>
</p>

#### Install

```sh
pip install -U sku
```

#### About

`sku` is a scikit-learn utilities package.

#### Usage

ItemEncoder:

```python
from sku import ItemEncoder

X = ['a', 'b', 'c']
ie = ItemEncoder()
ie.fit_transform(X)
# [0, 1, 2]
```

ItemVectorizer:

```python
from sku import ItemVectorizer

X = ['a,b,c', 'b,c', 'a,c,d,e,f', 'b']
iv = ItemVectorizer()
iv.fit(X)
iv.transform(['c,f'])
# [0, 0, 1, 0, 0, 1]
```

NumberBinarizer:

```python
from sku import NumberBinarizer

X = list(range(10))
nb = NumberBinarizer(bins=4)
nb.fit_transform(X)
# [0, 0, 0, 1, 1, 2, 2, 3, 3, 3]
```

RangeScaler:

```
from sku import RangeScaler

X = [30, 50, 100, 90, 80, 40]
rs = RangeScaler(out_range=(0, 10), floor=0, round=True)
rs.fit_transform(X)
# [3, 5, 10, 9, 8, 4]
```
