#### How to create a set ###

#1 , Using {element} 

names : set = {"John" ,3455.98, "Peter" ,True, "Ann" , "James", "John" ,
               "Peter", "Ann" , "James", "Ann" , "James", 
               "Paul" , 67 }
print(names)

names.add("Matt")
print(names)

#2, Using set constructors

users_vals = set(range(11))
print(users_vals)
user_name = "Ronaldo"
str_set = set(user_name)
print(str_set)

