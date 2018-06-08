# exemple 1
def my_function():
  print("Hello from a function")

my_function()
# exemple 2
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")
# exemple 3
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")
# exemple 4
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))
# exemple 5
myfunc = lambda i: i*2
print(myfunc(2))
# exemple 6
myfunc = lambda x,y: x*y
print(myfunc(3,6))
# exemple 7
def myfunc(n):
  return lambda i: i*n

doubler = myfunc(2)
tripler = myfunc(3)
val = 11
print("Doubled: " + str(doubler(val)) + ". Tripled: " + str(tripler(val)))
