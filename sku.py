class ItemEncoder:
    def __repr__(self):
        return 'ItemEncoder()'

    def fit(self, X):
        self.classes_ = []
        for xi in X:
            if xi not in self.classes_:
                self.classes_.append(xi)
        return self

    def transform(self, X):
        if isinstance(X, str):
            X = [X]
        Xt = []
        for xi in X:
            if xi not in self.classes_:
                Xt.append(None)
            else:
                Xt.append(self.classes_.index(xi))
        if len(Xt) == 1:
            return Xt[0]
        return Xt

    def fit_transform(self, X):
        self.fit(X)
        return self.transform(X)

    def inverse_transform(self, X):
        if isinstance(X, int):
            X = [X]
        Xt = []
        for xi in X:
            try:
                Xt.append(self.classes_[xi])
            except IndexError:
                Xt.append(None)
        if len(Xt) == 1:
            return Xt[0]
        return Xt

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





def scale(x, o=(0, 100), i=(0, 1)):
    return (x - i[0]) / (i[1] - i[0]) * (o[1] - o[0]) + o[0]

class RangeScaler:
    def __init__(self, out_range=(0, 100), floor=None, round=True):
        self.out_range = out_range
        self.floor = floor
        self.round = round

    def __repr__(self):
        return f'RangeScaler(out_range={self.out_range}, floor={self.floor}, round={self.round})'

    def fit(self, y):
        if not self.floor and self.floor != 0:
            min_ = min(y)
        else:
            min_ = self.floor
        max_ = max(y)
        self.in_range_ = (min_, max_)
        return self

    def transform(self, y):
        if not isinstance(y, list):
            y = [y]
        y = [scale(yi, self.out_range, self.in_range_) for yi in y]
        if self.round:
            y = [int(round(yi)) for yi in y]
        if len(y) == 1:
            return y[0]
        return y

    def fit_transform(self, y):
        self.fit(y)
        return self.transform(y)

def bin(x, b, o=(0, 100)):
    return int(b * ((x - o[0]) / (o[1] - o[0])))

class NumberBinarizer:
    def __init__(self, bins=5):
        self.bins = bins

    def __repr__(self):
        return f'NumberBinarizer(bins={self.bins})'

    def fit(self, y):
        self.min_ = min(y)
        self.max_ = max(y)
        return self

    def transform(self, y):
        if not isinstance(y, list):
            y = [y]
        y = [bin(yi, self.bins, (self.min_, self.max_)) for yi in y]
        y = [yi - 1 if yi == self.bins else yi for yi in y]
        if len(y) == 1:
            return y[0]
        return y

    def fit_transform(self, y):
        self.fit(y)
        return self.transform(y)
