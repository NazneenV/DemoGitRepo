'''p="welcome"
print(p[4:])
print(p[4:-1])
print(ord('B'))
print(max('X,Y,A,B,D'))
s="python"
for i in s:
    print(i,end="")'''

var1=10
def fn1():
 var1=100 #here ,defining a local var with the same name as global var
 print(var1)
fn1()
print(var1) #global variable's var1 value remains unchanged
# output
#100 if there is a clash in the name i.e both local and global var have same name-preference given to local var
#10

var2=10
print(var2)
def fn1():
 global var2 #here since
 var2=100 #now no difference bet var2 outside and inside
 print(var2)
fn1()
print(var2)
#expected output
#10
#100
#100



