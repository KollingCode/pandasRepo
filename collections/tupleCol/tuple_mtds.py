### Tuple Methods ####

info : tuple = ("John" , 34 , 56432.87 , 'John',True ,34,"John" ,[45,89])

count_res = info.count('John')
print('Count Result ::',count_res)

index_res = info.index(34)
print("Index Result ", index_res)

index_res = info.index(34, 2 )
print("Index Result ", index_res)

index_res = info.index(34 , 1 , 4)
print("Index Result ", index_res)
