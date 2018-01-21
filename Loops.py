#@Author Prathamesh More

#while loop

a = 0

while(a < 10):
    print('The count is ',a)
    a = a + 1
    

list = [1,2,4,5,6,7,8,9]


for a in list:
    print('List contents : ', a)


for a in range(5):
    print('List contents : ', a)

for  a in range(len(list)):
    print('Length : ',a)


dict = ('Prathamesh','Nawaz','Namita')

for names in dict:
    print(names)

for char in 'Prathamesh More':
    print(char)