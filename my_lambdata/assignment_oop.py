
from pandas import DataFrame
# state abbreviations

class DataProcessor:
    def __init__(self, something_else):
        """
        Params: my_df (pandas.DataFrame) has a column called abbrev with state abbreviations
        """
        self.df = something_else


    def add_state_names(self):

        # dictionary of names and abbreviations
        names_map = {'CA': 'California', 'CO': 'Colorado', 'CT': 'Conneticut'}
        # new column with names
        self.df['names'] = self.df['abbrev'].map(names_map)
        return self.df


if __name__ == '__main__':

    df = DataFrame({'abbrev': ['CA', 'CO', 'CT', 'DC', 'TX']})

    processor = DataProcessor(df)
    print(processor.df.head())

    processor.add_state_names(df)
    print(processor.df.head())
