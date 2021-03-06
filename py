def add_sub(x,y):
    c=x+y;
    d=x-y;
    return c,d 
a,s=add_sub(3,5)
print(a,s)
===================================================
i=5
def val(a):
    print(a)
i=10
val(i)
=====================================================
def tst(arg1,arg2):
    arg1=10;
    arg2[0]="abi"
    print(arg1,arg2)
'''def tst1(arg1,arg2):
    arg1=30
    arg2[0]="tst"
    print(arg1,arg2)'''
tst(11,[1,2,3,5])
tst(10,[11,22,33])
==========================================================
#Keyword-Based Arguments:
def fn(value):
    print(value)
    return

fn(value=123) # output => 123
fn(value="Python!") # output => Python!
fn(value1="Python!") #error
==============================================================
Arguments With Default Values:
def daysInYear(is_leap_year=False):
    if not is_leap_year:
        print("365 days")
    else:
        print("366 days")
    return

daysInYear()
daysInYear(True)
==================================================================
def dum(b,*v):
    print("%s[item : %d]"%(b,len(v)),v)
    for i in v:
        print("-",i)
dum("Elec","lap","mob","wash")
====================================================================
#Global Variables In A Function:
global x 
x=100
y = 55
def fn() :
    global x,y
    x = [3, 7]
    y = {1, 33, 55}
    # a local 'y' is assigned and created here
    # whereas, 'x' refers to the global name
print(x,y)
fn()
print(x, y)
============================================================================
#how a globally declared name behaves in two different Python functions.
foo = 99

def fn1() :
    global foo
    foo = 'new' # new local foo created

def fn2() :
    global foo
    foo = 'update' # va
print(foo)
fn1()
print(foo)
fn2()
print(foo)
===================================================================================
def fn1() :
   global x	
   x = [1,2] 
   y = [20, 200]
   print(x,y)
   # a local 'y' is created – availableonly within 'f1'
   # 'x' can be accessed anywhere after a call to 'f1'
fn1()
#print(x,y)
try :
    print(x, y) # name 'y' is not defined – error
except Exception as ex:
    print('y ->', ex)
    print('x ->', x)
======================================================================================
#Name Resolution In A Python Function

#var = 5
def fn1() :
   #var = [3, 5, 7, 9]
   def fn2() :
      #var = (21, 31, 41)
      print(var)
   fn2()
fn1()	# uncomment var assignments one-by-one and check the output
print(var)
=================================================================================
def fn1():
   print('In fn1')
   X = 100
   def fn2(): 
      print('In fn2')
      print(X) # Remembers X in enclosing def scope
    return fn2 # Return fn2 but don't call it
#print(x)
action = fn1() # Make, return function
action()
==============================================================================================
def returnDemo(val1, val2) :
   print(val1,val2)
   val1 = 'Windows'
   val2 = 'OS X'
   return val1, val2 # return multiple values in a tuple

var1 = 4
var2 = [2, 4, 6, 8]

print("before return =>", var1, var2)
var1, var2 = returnDemo(var1, var2)
print("after return  =>", var1, var2)