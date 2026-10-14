#### Create a range that starts from 1 and stops at 10
### Convert it a tuple object
### Update it with these numbers : 34 , 89 and 45
### Sum up the number 
### Show the character representation of the number

#### Dictionary ###

data : dict = {
    'user1' : ['jOhn' , 23 , 12345.8],
    'user2' : ['PAuL' , 31 , 34345.8],
    'user3' : ['PEteR' ,18 , 62345.8],
    'user4' : ['ANn' , 34 , 77345.8],
    'user5' : ['JAnE' , 28 , 67345.8]
}
 ## Sum all age values and get their average age
 ## Sum up the salary values and get the highest and lowest
 ## Correct the name value to a proper name eg "Peter"
data_values = data.values()
print(data_values)
list_data = list(data_values)
for dt in list_data:
    if isinstance(dt[0] , str):
       da = dt[0].title()
       dt.insert(0 , da)
       dt.remove(dt[1])
    print(dt)
    
total_age = 0
for da in list_data:
    if isinstance(da[1] , int):
        total_age = total_age + da[1]
print("Total " , total_age)

sal_list = []
for sal in list_data:
    if isinstance(sal[2] , float):
        sal_list.append(sal[2])
print('Maximun Salary ' , max(sal_list))
print('Minimun Salary ' , min(sal_list))

num = len(sal_list)
total_sal = 0
for sal in sal_list:
    total_sal += sal
print(total_sal)
    
print("Average Salary " , round(total_sal / num , 2))
    