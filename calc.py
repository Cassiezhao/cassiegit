print(100+200+300)
print('please input a name')
name = input()
print('hello',name)
print('please enter a number')
s=input('age:')
age=int(s)
if age >= 18:
    print('your age is',age)
    print('adult')
elif age>=6:
    print('your age is',age) 
    print('teeneager')
else:
    print('your age is',age)
    print('kid')
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 打印list:
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

d={'mike':85,'bob':75,'tracy':80}
print(d['mike'])
print('thomas' in d )
print(d.get('thomas',-1))
d.pop('bob')
print(d)

s=set([1,2,2,3,4,5,6])
print(s)
s.add(8)
print(s)

s2=set([9,2,3,4,5,6])
print(s&s2)
print(s|s2)
s.remove(4)
