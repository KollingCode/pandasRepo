#### Creating Dictionary Using {} ##

user_info : dict[str, str | int | bool | float | dict] = {"name" : "Paul" , 
                                           "age" : 22,
                                          'is_married' : True,
                                          "salary" : 1234.98, 
                                          "education" : {
                                              "primary": "Lagos",
                                          }}
print(user_info)

#### Creating Dictionary Using dict Constructor ##
user_details :dict[str , str | int | float] = dict(name = "Paul", age = 34 , salary = 2344.78 )
# user_details.setdefault('name' , "Paul")
print(user_details)

