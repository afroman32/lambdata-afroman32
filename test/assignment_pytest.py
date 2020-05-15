from pandas import DataFrame

from my_lambdata.assignment import add_state_names

# Objective: test the add_state_names function from the my_lambdata/assignment.py file

def test_add_state_names():
    
    df = DataFrame({'abbrev': ['CA', 'CO', 'CT', 'DC', 'TX']})
    assert list(df.columns) == ['abbrev']
    
    result = add_state_names(df)
    assert list(result.columns) == ['abbrev', 'names']
    assert result.iloc[0]['abbrev'] == 'CA'
    assert result.iloc[0]['names'] == 'California'
