#Declare list & print
sal = {"jane":15,"ksk":52}
print(sal)

sal["sa"] = 25

del sal["sa"]
print(sal)

for key, val in sal.items():
    print(key , val)
    print("jane" in sal)

# List
s = {1,2,3,4}
print(type(s))
s.add(1)
s.add(2)
s.add(3)
print(s)

print(6 in s )

#List Comprehensive

l = [ x for x in range(0,10)]
t = tuple( x for x in range(0,10))
s = { x for x in range(0,10)}
d = { x : x*x for x in range(0,10)}
print(l)
print(t)
print(s)
print(d)

g = "welcome"
g= 100
print(g)
