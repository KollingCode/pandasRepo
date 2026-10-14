user_info : dict[str, str | int | bool | float | dict] = {"name" : "Paul" , 
                                           "age" : 22,
                                          'is_married' : True,
                                          "salary" : 1234.98, 
                                          "education" : {
                                              "primary": "Lagos",
                                          }}
### Mutating Dictionary value
user_info["name"] = 'Peter'
user_info["age"] = 45
user_info["salary"] = 3456.90

## Addig new item to the dictionary
user_info["gender"] = 'Male'
user_info["state"] = 'Kano'

print(user_info)

### Accessing Dictionary value
print(user_info["name"])
print(user_info["salary"])
print(user_info["age"])

