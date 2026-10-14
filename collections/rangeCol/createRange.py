#### Range is class for generating sequential integers

### range(<stop> exclusive):: it generates integer from 0 to 9
range(10)
### range(<start>(inclusive) , stop (exclusive))it generates integer from 2 to 9
range(2 , 10)
### range(<start>(inclusive) , stop (exclusive) , <step> (skip))
# it generates integer from 1 , 4 , 7 
range(1 , 10 , 3)

range_obj = range(1 , 11, 3)
print(range_obj)
for num in range_obj:
    print(num , end = " ")