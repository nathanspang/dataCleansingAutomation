class DataSheet:
    def __init__(self, dataframe):
        self.dataframe = dataframe

    def get_cols(self):
        for col in self.dataframe.columns:
            print(col)


class Column:
    def __init__(self, name):
        self.name = name
