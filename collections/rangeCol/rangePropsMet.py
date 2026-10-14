range_obj = range(1 , 55, 2)
print(range_obj)
for num in range_obj:
    print(num , end = " ")
print()   
### Range Methods ####
### Range count method shows the number of integer in a range object 
count_res = range_obj.count(16)  ### Count equals (1)
print(count_res)

### Range index method shows the index  of integer in a range object 
index_res = range_obj.index(5)  ### Index of 16 equals (5)
print(index_res)

### Range Properties ####
print(range_obj.start)  ### 1
print(range_obj.stop)   ## 55
print(range_obj.step)  ### 2