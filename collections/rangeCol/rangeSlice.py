### Slicing :: creating a sequential collection from exiting
## collection
range_obj = range(1 , 55, 2)
### Accessing range value
print(range_obj[0])   ### 1
print(range_obj[4])   ### 9
print(range_obj[9])   ### 19

print(range_obj[-1])   ### 1
print(range_obj[-4])   ### 9
print(range_obj[-9])   ### 19

# for num in range_obj:
#     print(num , end = " ")
print()
### Positive Index Slicing
range_data = range(1 , 55)
new_data = range_data[5 : 13 ]
new_data2 = range_data[2 : 10 : 2 ]
print(new_data2)

print(new_data)

### Negative Index Slicing
range_data = range(1 , 55)
new_data3 = range_data[-5 : -13 ]
new_data4 = range_data[-2 : -10 : 2 ]
print(new_data3)
print(new_data4)

