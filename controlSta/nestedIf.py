age = int(input("Please enter your age >>> "))
nat = input("Please enter your nationality >>> ").lower().strip()

if age >= 18:
    ### Nested if-else block
    if nat == "nigerian":
        print("You can vote")
    else:
        print("You are not a Nigerian")
 
else:
    print("You are too young to vote")