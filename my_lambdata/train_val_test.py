
class Train_val_test:
    def __init__(self, df):
        self.df = df

    def split(self):
        # 60, 20, 20 split
        train_lim = int(len(self.df)*.6)
        val_lim = int(len(self.df)*.2)+train_lim
        train = self.df.iloc[0:train_lim]
        val = self.df.iloc[train_lim: val_lim]
        test = self.df.iloc[val_lim: len(self.df)]

        return (train, val, test)


if __name__ == "__main__":
    from pandas import DataFrame
    splitter = Train_val_test(df = DataFrame({"a":[0,1,2,3,4,5,6,7,8,9], 
                                            "b":[9,8,7,6,5,4,3,2,1,0],
                                            "c":[0,1,9,2,8,3,7,4,6,5]
                    }))

    print(splitter.split())