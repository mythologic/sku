class ItemVectorizer:
    '''Vectorize items in a one-vs-all fashion'''
    def __init__(self, delimiter=",", max_items=None):
        self.delimiter = delimiter
        if max_items:
            self.max_items = max_items
        else:
            self.max_items = float('inf')

    def __repr__(self):
        return f'ItemVectorizer(delimiter="{self.delimiter}", max_items={self.max_items})'

    def fit(self, X):
        '''Fit item vectorizer'''
        self.items_ = []
        for row in X:
            for item in row.split(self.delimiter):
                item = item.strip()
                if (item not in self.items_) and (len(self.items_) < self.max_items):
                    self.items_.append(item)
        return self

    def transform(self, X):
        '''Return vectorized items'''
        if isinstance(X, str):
            X = [X]
        Xt = [[0] * len(self.items_) for _ in range(len(X))]
        for uid, item_list in enumerate(X):
            for item in item_list.split(self.delimiter):
                item = item.strip()
                try:
                    iid = self.items_.index(item)
                    Xt[uid][iid] = 1
                except ValueError:
                    pass
        if len(Xt) == 1:
            return Xt[0]
        return Xt

    def fit_transform(self, X):
        '''Fit vectorizer and return vectorized items'''
        self.fit(X)
        Xt = self.transform(X)
        return Xt

    def inverse_transform(self, X):
        '''Transform encodings back to original values'''
        if not isinstance(X[0], list):
            X = [X]
        Xt = []
        for row in X:
            items = []
            for i, flag in enumerate(row):
                if flag == 1:
                    items.append(self.items_[i])
            istr = f'{self.delimiter}'.join(items)
            Xt.append(istr)
        if len(Xt) == 1:
            return Xt[0]
        return Xt
