# l=list(["Ganesh","haasidh","aasidh"])
# # l.remove(3)
# # l[1]=('e')
# for i in range(0,len(l[0])):
#     print(l[0][i]*3,end=' ') 
# thelist=[i for i in range(5)]
# print(end='')
# print(thelist) 
x = ['Apples', 'Oranges', 'Guavas', 'Grapes', 'Mangoes', 'Apricots', 'Olives']
y = [i for i in x if i[0].lower() in ['a','e','i','o','u']]
print(y)
l=[range(0,10)]
fruits = ['Apples', 'Oranges', 'Guavas', 'Grapes', 'Mangoes', 'Apricots', 'Olives']
fruits = [fruit for fruit in fruits if fruit[0].lower() in ['a', 'e', 'i', 'o', 'u']]
print(fruits,l)

import math as m
 st=''
for i in range(1,6):
    st+=str(m.factorial(i))
print(st)