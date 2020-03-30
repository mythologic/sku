class NumberBinarizer:
    '''Binarize numbers'''
    def __init__(self, bins=5):
        self.bins = bins

    def __repr__(self):
        return f'NumberBinarizer(bins={self.bins})'

    def fit(self, X):
        '''Fit number binarizer'''
        self.min_ = min(X)
        self.max_ = max(X)
        return self

    def transform(self, X):
        '''Transform values'''
        if not isinstance(X, list):
            X = [X]
        X = [bin(xi, self.bins, (self.min_, self.max_)) for xi in X]
        X = [xi - 1 if xi == self.bins else xi for xi in X]
        if len(X) == 1:
            return X[0]
        return X

    def fit_transform(self, X):
        '''Fit number binarizer and transform values'''
        self.fit(X)
        return self.transform(X)

def bin(x, b, o=(0, 100)):
    return int(b * ((x - o[0]) / (o[1] - o[0])))
