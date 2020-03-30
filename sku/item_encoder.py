class ItemEncoder:
    '''Encode item labels with value between 0 and n-1'''

    def __repr__(self):
        return 'ItemEncoder()'

    def fit(self, X):
        '''Fit item encoder'''
        self.classes_ = []
        for xi in X:
            if xi not in self.classes_:
                self.classes_.append(xi)
        return self

    def transform(self, X):
        '''Return encoded items'''
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
        '''Fit item encoder and return encoded labels'''
        self.fit(X)
        return self.transform(X)

    def inverse_transform(self, X):
        '''Transform encodings back to original item labels'''
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
