# my_mod.py


def enlarge(n):
    return n*100

def list_to_col(df, l, name):
    import pandas as pd
    new = pd.Series(l)
    df[name] = new
    return df

def train_val_test(df):
    # 60, 20, 20 split
    train_lim = int(len(df)*.6)
    val_lim = int(len(df)*.2)+train_lim
    train = df.iloc[0:train_lim]
    val = df.iloc[train_lim: val_lim]
    test = df.iloc[val_lim: len(df)]

    return (train, val, test)

if __name__ == "__main__":
    # only run the code below if running from the command line
    x = 5
    print(enlarge(x))

    y = int(input("Please chooses a number (eg 5): "))
    print(enlarge(y))