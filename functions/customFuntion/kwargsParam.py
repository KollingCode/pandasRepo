#### Kwargs Parameter ###
### Kwargs Parameter allows any lenght of key/word parameter 
## and it returns them in dictionary

def add_num(**kwargs : float):
     
     print(kwargs)
     
     
add_num(one = 23 , two = 45 , three = 56)
add_num(ss = 4 , rrr = 5 )
add_num(dd = -3 , ff= -5)
add_num(a = 3.9877 , b = 45.0067 )



def remove(**info):
    print(info)
    
remove(one = "I like python" ,gg =  "I want to dance" , fff = 'we are fine')
remove(ee = "I Need to sleep ")
remove(sss = "I am doing fine ")

    

