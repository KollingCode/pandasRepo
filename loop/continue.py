### Continue In loop means skip a loop

message = "Hello World"

for x in message:
    if x == 'W':
        continue
    print('hello John ' , end = ' ')
    
    
# print()
# print()   
# for vvv in message:
#     print(vvv , end = ' ' )

print()
numbers = range(1 , 25)  ### 1 to 24

for number in numbers:
    if number == 10 or number == 17:
        continue
    print(number , end = " ")


print()
numbers = range(1 , 25)  ### 1 to 24

for number in numbers:
    if number == 11:
        continue
    print(f'2 times {number} = {2 * number}')