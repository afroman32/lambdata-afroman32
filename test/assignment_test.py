import unittest

from pandas import DataFrame
from my_lambdata.assignment import add_state_names

# Objective: test the add_state_names function from the my_lambdata/assignment.py file
class TestAssignment(unittest.TestCase):

    def test_add_state_names(self):
        
        df = DataFrame({'abbrev': ['CA', 'CO', 'CT', 'DC', 'TX']})
        self.assertEqual(list(df.columns), ['abbrev'])
        
        result = add_state_names(df)
        self.assertEqual(list(result.columns), ['abbrev', 'names'])
        self.assertEqual(result.iloc[0]['abbrev'], 'CA')
        self.assertEqual(result.iloc[0]['names'], 'California')


if __name__ == '__main__':
    unittest.main()