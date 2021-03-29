#1
def a():
    return 5
print(a())
# Passes argument of 5 into function a

#2
def a():
    return 5
print(a()+a())
# a(5) + a(5) = 10

#3
def a():
    return 5
    return 10
print(a())
# Value of 5 has already been stored

#4
def a():
    return 5
    print(10)
print(a())
# Value of 5 is the only argument passed into the function

#5
def a():
    print(5)
x = a()
print(x)
# Told to print 5, but x has no arguments passed into the function a yet

#6
def a(b,c):
    print(b+c)
print(a(1,2) + a(2,3))
# Will print b+c and then next line will print 3 and 5

#7
def a(b,c):
    return str(b)+str(c)
print(a(2,5))
# Converts 2 and 5 into strings, so the function will concatenate 2 and 5 to 25.

#8
def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a())
# Will print 100 and then because b > 10, will return 10

#9
def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))
print(a(5,3))
print(a(2,3) + a(5,3))
# Will return 7, then 14, then 7+14 = 21

#10
def a(b,c):
    return b+c
    return 10
print(a(3,5))
# Will just return 8

#11
b = 500
print(b)
def a():
    b = 300
    print(b)
print(b)
a()
print(b)
# Will print 500, then 300 inside the function, then outside the function back to 500

#12
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
a()
print(b)
# By returning b, we are now setting the value of b at 300

#13
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
b=a()
print(b)
# I was wrong on the previous problem. By returning b and then setting b = a(), we are changing the value of b to 300.

#14
def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a()
# I believed it would just be 1,2,3. But I believe because we are placing b inside the a function, the actual output is 1,3,2.

#15
def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)
# At line 131 we are calling a(). First printing 1, then at 125 b() is called. First printing 3 and then returing 5. After b() is. Setting x = to 5 running through b(). Print (x) which is = 5. Then returning 10, on a(), the output of the function. Line 131 sets y= output of a(), which is 10 (the return).