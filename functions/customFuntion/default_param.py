### A Default Parameter

def add_num(first_num : float = 0.0 , second_num : float = 0.0):
     res = first_num + second_num
     return res
     
     
res1 = add_num()
print(res1)
res2 = add_num()
print(res2)
res3 =add_num(-3 , -5)
print(res3)
res4 = add_num(3.9877 , 45.0067)
print(res4)




def remove(info = "###########"):
    print(info)
    
remove()  
remove("I like python ")
remove("I Need to sleep ")
remove("I am doing fine ")

    

