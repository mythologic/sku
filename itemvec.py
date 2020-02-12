import numpy as np
from scipy.sparse import csr_matrix

class ItemVectorizer:
    def __init__(self, delimiter=",", max_items=None):
        self.delimiter = delimiter
        if max_items:
            self.max_items = max_items
        else:
            self.max_items = np.inf

    def __repr__(self):
        return (
            f'ItemVectorizer(delimiter="{self.delimiter}", max_items={self.max_items})'
        )

    def fit(self, X):
        self.items_ = []
        for row in X:
            for item in row.split(self.delimiter):
                item = item.strip()
                if (item not in self.items_) and (len(self.items_) < self.max_items):
                    self.items_.append(item)
        return self

    def transform(self, X):
        users = []
        items = []
        for user, item_list in enumerate(X):
            for item in item_list.split(self.delimiter):
                item = item.strip()
                try:
                    users.append(user)
                    items.append(self.items_.index(item))
                except ValueError:
                    pass
        data = [1] * len(users)
        matrix = csr_matrix((data, (users, items)), shape=(len(X), len(self.items_)))
        return matrix

    def fit_transform(self, X):
        self.fit(X)
        Xt = self.transform(X)
        return Xt
