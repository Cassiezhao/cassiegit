#!/home/cassiezhao/cassiegit
#coding:utf-8

from __future__  import division

def add(x,y):
    return x + y

def cheng(x,y):
    return x * y

def chu(x,y):
    return x / y

def jian(x,y):
    return x - y

operator ={"+":add,"-":jian,"*":cheng,"/":chu}

print operator["/"](3,2)

#print operator.get("%")(3,2)
def f(x,o,y):
    print operator.get(o)(x,y)

f(3,"+",2)
