#my_script.py

from pandas import DataFrame
from my_mod import enlarge # this works
# from my_lambdata.my_mod import enlarge
from my_mod import list_to_col

df = DataFrame({"a":[1,2,3], "b":[4,5,6],})
print(df)

print()

x = 11
print(enlarge(x))

print()

l = [7, 8, 9]
print(list_to_col(df, l, 'c'))