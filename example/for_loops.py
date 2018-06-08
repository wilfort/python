# exemple 1
print("\n\nExample\n")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) 

# exemple 2
# break
print("\n\nExample\n")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x) 

# exemple 3
# continue
print("\n\nExample\n")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x) 

# exemple 4
# function range()
print("\n\nExample\n")
for x in range(6):
  print(x) 

# exemple 5
# commence à 2
print("\n\nExample\n")
for x in range(2, 6):
  print(x) 

# exemple 6
# commence à 2 puis par saute de 3
print("\n\nExample\n")
for x in range(2, 30, 3):
  print(x) 

# exemple 7
# function recursion
def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results\n")
tri_recursion(6)