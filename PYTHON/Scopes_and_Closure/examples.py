
#* Example 1 
#-------------------------------------
username = "Shibam"
def func():
   #username = "User"
   print(username)

print(username)
func()
print("\n")
#--------------------------------------


#* Example 2
#--------------------------------------
x = 15
def  func2(y):
   z = x + y
   return z

result = func2(5)
print(result)
print("\n")
#---------------------------------------


#* Example 3
#---------------------------------------
a = 100
def func3():
   global a   # it should be avoidable
   a = 99

print(a)
func3()
print(a)
print("\n")
#---------------------------------------


#* Example 4
#---------------------------------------

n = 55
def f1():
   n = 88
   def f2():
      print(n)
   f2()
f1()
print("\n")
#---------------------------------------------






#! Factory Functions / Closure

#* Example 5 
#----------------------------------------------
def coder(power):
   def actual(num):
      return num ** power
   return actual            # returns definition of actual

ans1 = coder(2)  # calculating squares
ans2 = coder(3)  # calculating cubes

print(ans1)
print(ans2)

print(ans1(4))
print(ans2(4))