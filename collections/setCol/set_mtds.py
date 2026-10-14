
names : set = {"John" , "Peter" , "Ann" , "James", "John" ,
               "Peter", "Ann" , "James", "Ann" , "James", 
               "Paul" }

names.add('Ronaldo')
print(names)
pop_element = names.pop()
print(pop_element.upper()[0])
# names.remove('James')
# names.discard('James')
names.update({'Sola' , "Tola"})
new_set = names.copy()
print(new_set)

print(names)
