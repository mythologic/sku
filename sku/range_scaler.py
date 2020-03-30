class RangeScaler:
    '''Scale features according to a specified out range'''
    def __init__(self, out_range=(0, 100), floor=None, round=True):
        self.out_range = out_range
        self.floor = floor
        self.round = round

    def __repr__(self):
        return f'RangeScaler(out_range={self.out_range}, floor={self.floor}, round={self.round})'

    def fit(self, X):
        '''Fit range scaler'''
        if not self.floor and self.floor != 0:
            min_ = min(X)
        else:
            min_ = self.floor
        max_ = max(X)
        self.in_range_ = (min_, max_)
        return self

    def transform(self, X):
        '''Transform values'''
        if not isinstance(X, list):
            X = [X]
        X = [scale(xi, self.out_range, self.in_range_) for xi in X]
        if self.round:
            X = [int(round(xi)) for xi in X]
        if len(X) == 1:
            return X[0]
        return X

    def fit_transform(self, X):
        '''Fit range scaler and transform values'''
        self.fit(X)
        return self.transform(X)

def scale(x, o=(0, 100), i=(0, 1)):
    return (x - i[0]) / (i[1] - i[0]) * (o[1] - o[0]) + o[0]
