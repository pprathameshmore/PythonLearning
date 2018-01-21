#@Author Prathamesh More

a = 60
b = 13

c = 0

print('a = ',a,':',bin(a), 'b = ', b,bin(b))

#AND Operation

c = a & b
print('AND OPERATION : ',c)
print('c = ',bin(c))

c = a | b
print('OR OPERATION : ',c)
print('c = ',bin(c))

c = a ^ b
print('EXOR OPERATION : ',c)
print('c = ',bin(c))

c = ~a
print('COMPLEMENT : ',c)
print('c = ',bin(a))

c = a << 2
print('LEFT SHIFT ', c)
print('c = ',bin(c))

c = a >> 2
print('RIGHT SHIFT : ', c)
print('c = ',bin(c))