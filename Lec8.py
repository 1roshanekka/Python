b1 = True
b2 = False
#Should be Capital Letter T & F

print(type(b1))
print(type(b2))
print()

#float & string to integer
a = int(5.7)
b = int("10")
print()

#computer will take 5 and remove .7 (float to integer)
print(a, type(a))
print(b, type(b))
print()

#integer & string to float
a = float(9)
b = float("5.3")

print(a, type(a))
print(b, type(b))
print()

#integer and float to string
a = str(9)
b = str(5.3)

print(a, type(a))
print(b, type(b))
print()

#integer to Boolean

a = bool(10)
b = bool(0)
c = bool(-10)

print(a, type(a))
print(b, type(b))
print(c, type(c))
print()
# anything other than 0 prints TRUE
#only 0 prints FALSE

#float to boolean
a = bool(10.5)
b = bool(0.0)
c = bool(-10.4)

print(a, type(a))
print(b, type(b))
print(c, type(c))
print()

#String to boolean
a = bool("India")
b = bool("10")
c = bool("-10.4")
d = bool("0")
e = bool(" ")
f = bool("")

print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))
print(e, type(e))
print(f, type(f))
print()