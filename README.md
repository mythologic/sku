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

#### Usage

Itemvec is easy to use:

```
from itemvec import ItemVectorizer
import numpy as np

products = np.array([
    'reeses, kitkat, skittles',
    'kitkat, smarties, reeses',
    'smarties, rockets, jubejubes'
])

iv = ItemVectorizer(delimiter=',')
iv.fit(products)
result = iv.transform(products)
result.todense()

# matrix([[1, 1, 1, 0, 0, 0],
#         [1, 1, 0, 1, 0, 0],
#         [0, 0, 0, 1, 1, 1]], dtype=int64)
```

