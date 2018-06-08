# exemple 1
thisdict =	{
  "apple": "green",
  "banana": "yellow",
  "cherry": "red"
}
print(thisdict)
# exemple 2
thisdict =	{
  "apple": "green",
  "banana": "yellow",
  "cherry": "red"
}
thisdict["apple"] = "red"
print(thisdict)

##############################################################

###############
# constructor #
###############
thisdict =	dict(apple="green", banana="yellow", cherry="red")
# note that keywords are not string literals
# note the use of equals rather than colon for the assignment
print(thisdict)


###############
# methode add #
###############
thisdict =	dict(apple="green", banana="yellow", cherry="red")
thisdict["damson"] = "purple"
print(thisdict)


###############
# methode del #
###############
thisdict =	dict(apple="green", banana="yellow", cherry="red")
del(thisdict["banana"])
print(thisdict)


###############
# methode len #
###############
thisdict =	dict(apple="green", banana="yellow", cherry="red")
print(len(thisdict))