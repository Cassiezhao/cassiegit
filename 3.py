#!/home/cassiezhao/cassiegit
import time
s="hello"
l=[1,2,3,'a','b']
t=(7,8,9,'x','y')
d={1:111,2:222,5:555,3:333}

for x in range(1,11):
    print x
    if x == 3:
	pass
    if x == 2:
        print "hello 22222222222"
	continue
    if x == 5:
	exit() 
    if x == 6:
    	break
    print "#"*50

print "ending"
#for k,v in d.items():
#    print k
#    print v
#else:
#    print "ending"
#print d.items()

#for x in l:
#    if x >= 2:
#    	print x

#for x in range(len(s)):
#    print s[x]

for x in range(100):
    print x
    time.sleep(1)
