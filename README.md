<h3 align="center">
  <img src="https://raw.githubusercontent.com/maxhumber/itemvec/master/logo/itemvec.png" width="300px" alt="itemvec">
</h3>
<p align="center">
  <a href="https://github.com/maxhumber/itemvec"><img alt="GitHub" src="https://img.shields.io/github/license/maxhumber/itemvec"></a>
  <a href="https://travis-ci.org/maxhumber/itemvec"><img alt="Travis" src="https://img.shields.io/travis/maxhumber/itemvec.svg"></a>
  <a href="https://pypi.python.org/pypi/itemvec"><img alt="PyPI" src="https://img.shields.io/pypi/v/itemvec.svg"></a>
  <a href="https://pepy.tech/project/itemvec"><img alt="Downloads" src="https://pepy.tech/badge/itemvec"></a>
</p>

#### Install

```
pip install -U itemvec
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

