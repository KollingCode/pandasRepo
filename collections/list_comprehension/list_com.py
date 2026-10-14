numbers = [12, 56, 7, 9, 32, 79]
# odd = []
# even = []
# for num in numbers:
#     if num % 2 == 1:
#         odd.append(num)
#     else: 
#         even.append(num)
# print(odd )
# print(even )

even_dat = [num for num in numbers if num % 2 == 0  ]
print(even_dat)

odd_dat = [num for num in numbers if num % 2 == 1  ]
print(odd_dat)

