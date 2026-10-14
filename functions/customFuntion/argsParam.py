#### Args Parameter ###
### Args Parameter allows any lenght of arguments 
## and it returns them in tuple

def add_num(*args : float):
     
     print(sum(args))
     
     
add_num(23 , 45 , 56, 89 , 43, 90)
add_num(4 , 5 , 7,4)
add_num(-3 , -5 ,90,-76)
add_num(3.9877 , 45.0067 ,-987.78 , 453.9876)



def remove(*info):
    print(info)
    
remove("I like python " , "I want to dance" , 'we are fine')
remove("I Need to sleep ")
remove("I am doing fine ")

    

