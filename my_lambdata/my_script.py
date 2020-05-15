#my_script.py

from pandas import DataFrame
# from my_mod import enlarge # this works
from my_lambdata.my_mod import enlarge
from list_to_col import List_to_col
# from my_mod import train_val_test

df = DataFrame({"a":[1,2,3], "b":[4,5,6],})
print(df)

print()

x = 11
print(enlarge(x))

print()

l = [7, 8, 9]
# print(List_to_col.changer(df, l, 'c'))

