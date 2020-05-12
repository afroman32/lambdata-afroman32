

from pandas import DataFrame
# state abbreviations

def add_state_names(new_df):
    # TODO add a column of corresponding state names
    # dict with abbreviations and state names
    # create a new column that is a copy of the first but mapped with the names 
    # concat with axis=1

    # create a copy so it doesn't mess with the original
    my_df = new_df.copy()    

    # dictionary of names and abbreviations
    names_map = {'CA': 'California', 'CO': 'Colorado', 'CT': 'Conneticut'}

    # new column with names
    my_df['names'] = my_df['abbrev'].map(names_map)

    return my_df


if __name__ == '__main__':

    df = DataFrame({'abbrev': ['CA', 'CO', 'CT', 'DC', 'TX']})
    print(df.head())

    df2 = add_state_names(df)
    print(df2.head())

    df3 = DataFrame({'a': [1, 2, 3, 4]})
    print(df3.head())

