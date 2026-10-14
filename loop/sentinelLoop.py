num = int(input("Enter the number of numbers >>> "))
nums = []

for _  in range(num):
    num1 = input("Enter a number >>> ")
    if num1 == 'no':
        break
    nums.append(int(num1))

    
print(nums)