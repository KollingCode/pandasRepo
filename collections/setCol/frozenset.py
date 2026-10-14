"""
A frozeset is a collection of hashed immutable items

### How to create a frozeset
# 1, frozentset()

#### Properties of a frozenset ####
# 1 , Its items are immutable 
# 2 , its items are not indexed 
# 3 , its items are not ordered
# 4 , its items are  unique (it  allows no duplicated items)
# 5, its itemes are not sorted (not in ascending or descending order) 
# 6, it can contain any item of any data type 
""" 

names : frozenset = frozenset( ["John" ,3455.98, "Peter" ,True, "Ann" 
                     , "James", "John" ])
print(names)
