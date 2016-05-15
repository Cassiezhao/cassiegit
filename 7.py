#!/home/cassiezhao/cassiegit

x= 'i am global var'

def fun ():
    global x 
    x =100
    global y 
    y=200    
    #print x

fun()

print "#"*49

print x  
print y
