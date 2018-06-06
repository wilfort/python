a = "hello"
print(a[1])# returns "e"

b = "world"
print(b[2:5])# returns "rld"

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

a = "Hello, World!"
print(len(a))# returns number chaine chareter

a = "Hello, World!"
print(a.lower())# returns chaine chareter minicules

a = "Hello, World!"
print(a.upper())# returns chaine chareter majuscule

a = "Hello, World!"
print(a.replace("H", "J"))# returns chaine chareter avec replacement chareter H par J

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

print("Enter your name:")
x = input()#secie de donner par clavier
print("Hello, " + x)
