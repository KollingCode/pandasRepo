### It shows the address of an object
name = "John"
age = 23 
obj_addr = id(name)
obj_addr1 = id(age)
print(f'Object Address :: {obj_addr} , {obj_addr1}')
# print()
# input()
### It returns a character from an integer (unicode) 
chr_val = chr(13534)
print(chr_val)
### It returns a unicode from a character 
ord_val = ord("y")
print(ord_val)

print(bin(35))
print(oct(567))
print(hex(789))
print(max([23 ,98, 45,90,45,82,]))
print(min([23 ,98, 45,90,45,82,]))
print(sum([23 ,98, 45,90,45,82,]))

print(pow(2 , 3))
res = 71 / 4.67
print(round(res , 5))
num = +123.9033
print(abs(num))
