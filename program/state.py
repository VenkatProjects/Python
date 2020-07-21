# if_else

x = 20
if x<20:
    print("x is less than 20", "x:",x)
elif x == 30:
    print("x is eaual to 20")
else:
        print("x is greater than 20", 'x:',x)

#Nested_if

y = 21
if y < 20:
    print("y is less than 20")
    if y < 15:
        print("y is less than 15")
    else:
        print("y is greater than 15")
else: 
    print("y is greater than 20")

# For Loop 

nums = [x for x in range(0,10)]

for x in nums:
    if (x == 4): continue
    print(x)
print("done")

#While Loop

a=1
while a != 0:
    print(a)
    a-=1

#break

nums = [x for x in range(0,10)]
index = 0
while index < len(nums):
    print(nums[index])
    index+=1
print("done")

m = "venkatesn  k    "
print(m.strip())

# Lambda

def downloadFile(url):
    print("establish connection"+url)
    print("open connetion " + url)
    print("download data")
    print("close connection" + url)
downloadFile("ftp://www.abc.org")



def createMultiplier(x):
    return lambda y: x * y
mul = createMultiplier(10)

def excute(f,arg):
    print("called f with " +str(arg))
    return f(arg)

print(excute(mul, 15))
print(excute(mul,25))

def myfunc(n):
    return lambda a : a * n
mydoubler = myfunc(2)
print(mydoubler(11))


