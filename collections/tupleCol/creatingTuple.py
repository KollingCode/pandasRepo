#### How to create a tuple
# 1, ()
# 1, Comma Separated Values 
names : tuple = "John" , "Ann" ,  "Matt" , "James"


## indexing
print(names[1])
print(names[2])
print(names[0])
print(names[-1])
info : tuple = ("John" , 34 , 56432.87 , True , range(4), [45,89])

## Immutability is not possible
# names[1] = 'Annah'
# names[2] = "Mathew"
# names[-1] = "Paul"
# print(names)

## Sorting List
sorted_names = sorted(names , reverse=True )
print(tuple(sorted_names ))

## Tuple Constructor
users_vals = tuple(range(11))
print(users_vals)
user_name = "Ronaldo"
str_tuple = tuple(user_name)
print(str_tuple)

info1 : list = ["John" , 34 , 56432.87 , True , range(4), [45,89]]
print(tuple(info1))