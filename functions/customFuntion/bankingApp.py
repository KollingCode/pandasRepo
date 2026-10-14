### Create  functions to :
### Function to create user account

# 1, Save Money
##### Items to save money ####
# i,  account number 
# ii, amount to save
# iii, initial balance
### Database data #### 
balance : float = 0.0  ### Global variable
acct_num : str = "123456" 
customer_name : str = "James Doe"
CUST_PIN = "1234"
cust_details : dict[str , str | float | int] = {}
cust_list : list[dict] = []
from random import random 
from uuid import uuid1 as id
acct_num = str(id(4))
cust_details["acct_num"] = acct_num
print(cust_details)
def acct_details():
    
    count = int(input("Enter Numbers Customers To Enter And Press 'Control + C' To Quit  "))
    while len(cust_list) <= count :
        acct_name = input("Please Enter Account Name >>> ")
        if isinstance(acct_name , str) and acct_name.isalpha():
           cust_details["acct_name"] = acct_name
           cust_details["acct_balance"] = 0.0
           cust_list.append(cust_details)
        #    print(cust_list)
        else:
            print( "Check Your Details !!!")
# acct_details() 

print(cust_list)
def save_money(amount  : float , account_num : str , cust_name : str) -> None:
    if isinstance(amount , float) and isinstance(account_num , str) and isinstance(cust_name, str):
        if amount >= 0.0 and account_num == acct_num and cust_name == customer_name:
            global balance
            balance = balance + amount
            print(f'{amount} has been saved to {acct_num} Account Number successfully')
        else:
            print("Ooops!!! Check your details!!")
    else:
        print("Data not formatted correctly")
      
# save_money(12344.00 , "123456" , "James Doe")
# save_money(345344.00 , "123456" , "Jame Doe")
# save_money(456744.00 , "123456" , "James Doe")
# save_money(12344.00 , "123456" , "James Doe")
# save_money(245344.00 , "123456" , "James Doe")
# save_money(5656744.00 , "123456" , "James Doe")
# save_money(46344.00 , "123456" , "James Doe")
# save_money(75344.00 , "123456" , "James Doe")
# save_money(6776676744.00 , "13456" , "James Doe")


 # 3, Check Balance           
    
# def check_balance(PIN : str , account_num : str , cust_name : str) -> str:
#     if isinstance(PIN , str) and isinstance(account_num , str) and isinstance(cust_name, str):
#         if PIN == CUST_PIN and account_num == acct_num and cust_name == customer_name:
#             global balance
#             return f'{cust_name}, your account balance is {balance}'  
#         else:
#             return  "Ooops!!! Check your details!!"
#     else:
#         return "Data not formatted correctly"
# bal_details = check_balance("1234" , "123456" , "James Doe")
# print(bal_details)

# def withdraw_money (amount: float , PIN : str , account_num : str , cust_name : str) -> float | str:
#     if isinstance(PIN , str) and  isinstance(amount , float | int) and isinstance(account_num , str) and isinstance(cust_name, str):
#         if PIN == CUST_PIN and account_num == acct_num and cust_name == customer_name:
#             global balance
#             if amount < balance:
#                 balance = balance - amount
#                 return  amount
#             else:
#                 return "Insuffiente fund"
                 
#         else:
#             return  "Ooops!!! Check your details!!"
#     else:
#         return "Data not formatted correctly"
# my_money = withdraw_money(123000 , "1234" , "123456" , "James Doe")
# print(my_money)
# my_money = withdraw_money(5623000 , "1234" , "123456" , "James Doe")
# print(my_money)
# my_money = withdraw_money(23000 , "1234" , "123456" , "James Doe")
# print(my_money)

# bal_details = check_balance("1234" , "123456" , "James Doe")
# print(bal_details)
