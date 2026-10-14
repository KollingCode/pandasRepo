### A function is a piece of code 
# that is reusable
### Function Syntax ####
# def <name of the function > (<** parameters>):
    ### code

## Function Declaration And Implementation
def message():
    "This function displays 'Hello Python and sums 12 and 34'"
    num = 12
    val = 34
    print(num + val )
    print("Hello Python!!")
  
### Calling a function  
message()
message()
message()
### Function referrencing or listening
message

### Types of function
## 1 , Void Function ::: Return 'None' to the caller , which means nothing
## 2 , Non-Void Function ::: Returns data to
# the caller any type e.g  (str, int, float , bool, list  tuple ,dict, set etc ) except "None"

##### Parameters in Function ###
## Parameters redefine what a function is doing
# 1, non-default Parameter e.g def message(name , age): pass
# 2, default Parameter e.g  def message(name = 'Doe' , age = 34): pass
# 3, args Parameter e.g def message(*args , *age): pass
# 4, kwargs Parameter e.g def message(**kwargs , **age): pass
