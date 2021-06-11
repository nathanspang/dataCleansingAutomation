class DataSheet:
    def __init__(self, dataframe):
        self.dataframe = dataframe

    def get_cols(self):
        cols = {}
        for col in self.dataframe.columns:
            cols[col] = Column(col)
        return cols


class Column:
    def __init__(self, name):
        self.name = name

class CategoricalColumn(Column):
    def __init__(self, value, binary):
        self.value = value
        self.binary = binary

class NumericalColumn(Column):
    def __init__(self, value, imput_method):
        self.value = value
        self.imput_method = imput_method
