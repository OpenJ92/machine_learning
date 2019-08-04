from sklearn.preprocessing import LabelBinarizer

from sklearn.base import TransformerMixin 

class _Identity(TransformerMixin):
    def __init__(self, *args, **kwargs):
        self.encoder = None 

    def fit(self, x, y=None):
        return self

    def transform(self, x, y=None):
        return x


class _LabelBinarizer(TransformerMixin):
    def __init__(self, *args, **kwargs):
        self.encoder = LabelBinarizer(*args, **kwargs)

    def fit(self, x, y=None):
        self.encoder.fit(x)
        return self

    def transform(self, x, y=None):
        return self.encoder.transform(x)

