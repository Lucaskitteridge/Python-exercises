# use def to define a new function

def say_hi(name):
  # code needs to be indented to be considered part of the function. If not, it is no longer considered part of the function
  print("Hello " + name)
  
#calling a function is like JS
say_hi("Lucas")

#return just like js

def cube(num):
  return num*num*num

print(cube(3))