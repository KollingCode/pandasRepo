### Break In loop means stopping a loop

message = "Hello World"

for x in message:
    if x == 'W':
        break
    print('hello John ' , end = ' ')
    
    
# print()
# print()   
# for vvv in message:
#     print(vvv , end = ' ' )

print()
numbers = range(1 , 25)  ### 1 to 24

for number in numbers:
    if number == 10:
        break
    print(number , end = " ")


print()
numbers = range(1 , 25)  ### 1 to 24

for number in numbers:
    if number == 11:
        break
    print(f'2 times {number} = {2 * number}')