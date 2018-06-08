#
thislist = ["apple", "banana", "cherry"]
print(thislist)
#
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"

print(thislist)
###############################################

###############
# construteur #
###############
thislist = list(("apple", "banana", "cherry"))
print(thislist)


##################
# methode append #
##################
thislist = list(("apple", "banana", "cherry"))
thislist.append("damson")

print(thislist)
#
a = ["apple", "banana", "cherry"]

b = ["Ford", "BMW", "Volvo"]

a.append(b)

print(a)


##################
# methode remove #
##################
thislist = list(("apple", "banana", "cherry"))
thislist.remove("banana")

print(thislist)


################
# fonction len #
################
thislist = list(("apple", "banana", "cherry"))
print(len(thislist))


#################
# methode clear #
#################
fruits = ["apple", "banana", "cherry"]

fruits.clear()

print(fruits)


################
# methode copy #
################
fruits = ["apple", "banana", "cherry"]

x = fruits.copy()

print(x)


#################
# methode count #
#################
fruits = ["apple", "banana", "cherry"]

x = fruits.count("cherry")

print(x)
#
fruits = [1, 4, 2, 9, 7, 8, 9, 3, 1]

x = fruits.count(9)

print(x)


##################
# methode extend #
##################
fruits = ['apple', 'banana', 'cherry']

cars = ['Ford', 'BMW', 'Volvo']

fruits.extend(cars)

print(fruits)
#
fruits = ['apple', 'banana', 'cherry']

points = (1, 4, 5, 9)

fruits.extend(points)

print(fruits)


#################
# methode index #
#################
fruits = ['apple', 'banana', 'cherry']

x = fruits.index("cherry")

print(x)
#
fruits = [4, 55, 64, 32, 16, 32]

x = fruits.index(32)

print(x)


##################
# methode insert #
##################
fruits = ['apple', 'banana', 'cherry']

x = fruits.insert(1,"orange")

print(x)


###############
# methode pop #
###############
fruits = ['apple', 'banana', 'cherry']

fruits.pop(1)

print(fruits)
#
fruits = ['apple', 'banana', 'cherry']

x = fruits.pop(1)

print(x)


###################
# methode reverse #
###################
fruits = ['apple', 'banana', 'cherry']

fruits.reverse()

print(fruits)


################
# methode sort #
################
cars = ['Ford', 'BMW', 'Volvo']

cars.sort()

print(cars)
#
cars = ['Ford', 'BMW', 'Volvo']

cars.sort(reverse=True)

print(cars)
#
# A function that returns the length of the value:
def myFunc(e):
  return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

cars.sort(key=myFunc)

print(cars)
#
# A function that returns the length of the value:
def myFunc(e):
  return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

cars.sort(key=myFunc)

print(cars)
