### A Non-void returns  any data type i.e str, int, float, list , tuple
### it is  like gabbage-out
## show number, get value , display something
def sum_num() -> int:
     result = 34 + 23
     return result
     
data = sum_num()
print(data * 12 + 45 / 89)

def show_data() -> str:
    return 'Data removed sucessfully'
value = show_data()
print(value.upper()[0 : 4].capitalize().swapcase())
    

