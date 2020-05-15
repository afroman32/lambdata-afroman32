
import unittest
from pandas import DataFrame

from my_lambdata.assignment_oop import DataProcessor

class TestDataProcessor(unittest.TestCase):

    def test_add_state_names(self):
        
        df = DataFrame({'abbrev': ['CA', 'CO', 'CT', 'DC', 'TX']})
        processor = DataProcessor(df)
        self.assertEqual(list(processor.df.columns), ['abbrev'])
        
        processor.add_state_names()

        self.assertEqual(list(processor.df.columns), ['abbrev', 'names'])
        self.assertEqual(processor.df.iloc[0]['abbrev'], 'CA')
        self.assertEqual(processor.df.iloc[0]['names'], 'California')


if __name__ == '__main__':
    unittest.main()