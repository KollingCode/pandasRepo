greet : str  = "Hello World"

### Uppercase Method
upper = greet.upper()
print('Upper Case ::: ', upper)

### Lowercase Method
lower = greet.lower()
print("Lower Case ::: ", lower)

### Titlecase Method
title = greet.title()
print("Title Case ::: ", title)

### Swapcase Method
title = greet.swapcase()
print("Swap Case ::: ", title)

### Titlecase Method
title = greet.capitalize()
print("Capitalized ::: ", title)

#### String Stripping ###

user_name = "     John Doe             "
print(user_name)
new_name = user_name.strip()
print(new_name)
l_new_name = user_name.lstrip()
print(l_new_name)
r_new_name = user_name.rstrip()
print(r_new_name)

user_name = "aaaaaaJohn Doeaaaaaaa"
chr_new_name = user_name.strip('a')
print(chr_new_name)


user_name = "aaaaaaJohn Doeaaaaaaa"
l_chr_new_name = user_name.lstrip('a')
print(l_chr_new_name)

user_name = "aaaaaaJohn Doeaaaaaaa"
r_chr_new_name = user_name.rstrip('a')
print(r_chr_new_name)

#### String Find method ####
user_name = "John Doe Martins"
print(user_name.find('Do'))
print(user_name.find('Mar' , 5 ))
print(user_name.find('ti', 5 , 15))

#### String Index method ####
user_name = "John Doe Martins"
print(user_name.index('Do'))
print(user_name.index('Mar' , 5 ))
print(user_name.index('ti', 5 , 15))


#### String Count method ####
user_name = "John Doe Martins"
print(user_name.count('o'))
print(user_name.count('n' , 5 ))
print(user_name.count('n', 5 , 15))

#### String Split method ####
user_name = "John Doe Martins"
split_data = user_name.split()
print(split_data)

#### String Join method ####
join_data = ",".join(split_data)
print(join_data)


#### String Suffix and Prefix Method
data = 'user_data.json'
dt1 =data.removesuffix('.json')
print(dt1)

data = 'user_data.json'
dt2 =data.removeprefix('user_')
print(dt2)

### String Replace Method

data = 'user_data.json'
dat2 = data.replace('.json' , ".py")
print(dat2)

### String StartsWith and EndsWith Methods
data = 'user_data.json'
res1 = data.startswith('us')
print(res1)
res2 = data.endswith('on')
print(res2)












