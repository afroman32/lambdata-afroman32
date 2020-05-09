
class List_to_col:
    def __init__(self, df, l, name):
        self.df = df
        self.l = l
        self.name = name

    def changer(self):
        from pandas import Series
        df2 = self.df.copy()
        new = Series(self.l)
        df2[self.name] = new
        return df2


if __name__ == "__main__":

    from pandas import DataFrame

    convert = List_to_col(df=DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]}),
                          l=[7, 8, 9],
                          name='c')

    print (convert.df)
    print(convert.changer())
