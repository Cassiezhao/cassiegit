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


def f(x,o,y):
    print operator.get(o)(x,y)


#print __name__ 

if __name__ == "__main__":
    print f(2,"*",3)
