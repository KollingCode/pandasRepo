user_info = {"name" : "Paul" , "age" : 22,'is_married' : True,
             "salary" : 1234.98, 
             "education" : {"primary": "Lagos" }}

###Getting a value
print(user_info.get('name'))
print(user_info.get('salary'))
### Getting all keys
all_keys =user_info.keys()
print(list(all_keys))
### Getting all values
all_values = user_info.values()
print(tuple(all_values))
### Getting all items
all_items = user_info.items()
print(list(all_items))

pop_val = user_info.pop('name')
print(pop_val.upper())

pop_item = user_info.popitem()
print(pop_item)

user_info.update(user_id = "00001222" , phone = "09998988")
print(user_info)