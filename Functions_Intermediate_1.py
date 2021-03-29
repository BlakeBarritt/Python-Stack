import random
def randInt(min = 0, max = 100):
# set min and max if no arguments are provided
    num = random.random() * (max-min) + min
# multiplying by (max-min) to get range size. Then add minimum to get the floor of our range
    return (int(num))
# convert to integer
print(randInt())
print(randInt(max = 50))
print(randInt(min = 50))
print(randInt(min = 50, max = 500))