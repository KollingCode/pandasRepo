# ### Creating list using square brackets ::::++ []
# names : list = ["John" , "Ann" ,  "Matt" , "James"]
# print(names)
# info : list = ["John" , 34 , 56432.87 , True , range(4), [45,89]]
# print(info)

# ## indexing
# print(names[1])
# print(names[2])
# print(names[0])
# print(names[-1])

# ## Mutability
# names[1] = 'Annah'
# names[2] = "Mathew"
# names[-1] = "Paul"
# print(names)

# ## Sorting List
# sorted_names = sorted(names , reverse=True )
# print(sorted_names )

### list Constructor  ::: List()
animals = list()
animals.append('Dog')
animals.append('Cat')
animals.append('Hen')
animals.append('Goat')
print(animals)
nums = range(1 ,11)
numbers = list(nums)
print(numbers)
message = "Hello"
msg = list(message)
print(msg)