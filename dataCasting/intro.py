#### Data Casting ::: it an approach of converting data from 
### one type to another

age = '34' ### numeric string
#### To convert 'age' variable to integer we use
## int contructor   ::: int()
int_value = int(age)
### Checking data type of "int_value" 
## we use type constructor
print(type(int_value))
result = int_value + 5
print(result)

salary = "23455.98" ### numeric string
#### To convert 'salary' variable to float we use
## float contructor   ::: float()

float_salary = float(salary)
## we use type constructor
print(type(float_salary))
result = float_salary + 5988.98
print(result)


### Boolean Conversion
## 12 , -344 , 'yyuhiu', 0.00074, -5776.88 :: True
## 0, 0.0000 , '' :::: False

is_married = 'True'  ### String type
#### To convert 'is_married' variable to boolean  we use
## bool contructor   ::: bool()
bool_result = bool(is_married)
## we use type constructor
print(type(bool_result))
result = bool_result
print(result)

#### String coversion
user_id = 77878
### To convert "user_id" to string 
### we use str() constructor
user_id = str(user_id)
print(type(user_id))

new_id = user_id + 655
print(new_id) 