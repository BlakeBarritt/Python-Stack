# 1.
def countdown(num):
    list = []
    for i in range (num,0,-1):
        list.append(i)
    return list
print (countdown(5))
# Created new list, iterating down from any give number to -[1] -- the range is exclusive in Python. append() is a built-in Python method that adds items to end of list. Return list to store values.

# 2.
def printAndReturn(nums):
    print(nums[0])
    return nums[1]
print (printAndReturn([5,12]))
# Created function that received a list. Telling the function to print the list value at position [0] and return the list value at position [1].

# 3.
def firstPlusLength(nums):
    return nums[0] + len(nums)
print(firstPlusLength([1,2,3,4,5]))
# Created function with empty array called nums. Return the value of nums[0] + length of the array

# 4.
def valuesGreaterThanSecond(array):
    newArray = []
    for i in array:
        if len(array) < 2:
            return False
        elif i > array[1]:
            newArray.append(i)
    print (len(newArray))
    return newArray

print(valuesGreaterThanSecond([5,2,3,2,1,4]))

# Set new array inside function to append to. For any value i in the array -- only use index position in range function -- if the length of the array is < 2, return fales. Else if statement, if the value of i is greater than the value of the array at 1, append to new array.

# 5.
def thisLengthThatValue (size, value):
    newArray = []
    for i in range(size):
        newArray.append(value)
    return newArray

print (thisLengthThatValue(6,2))

# Set new array inside function to append to. For the length of the new array as given by size parameter, append the value given in value to newArray.