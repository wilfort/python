#
thistuple = ("apple", "banana", "cherry")
print(thistuple)

#
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

#
thistuple = ("apple", "banana", "cherry")
thistuple[1] = "blackcurrant"

# the value is stille the same:
print(thistuple)

###################################################

###############
# Constructor #
###############

thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)


#######
# len #
#######
thistuple = tuple(("apple", "banana", "cherry"))
print(len(thistuple))

#######################################
#                                     #
# You cannot remove items in a tuple. #
#                                     #
#######################################