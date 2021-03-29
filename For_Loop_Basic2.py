# 1.
def biggie_size(some_list):
    for i in range(len(some_list)):
        if some_list[i] > 0:
            some_list[i] = "big"
    return some_list
# print(biggie_size([-1, 3, 5, -5]))

# 2.
def count_positives(list):
    count = 0
    for i in range(len(list)):
        if list[i] > 0:
            count += 1
    list[len(list)-1] = count
    return list
# Set count = 0, then iterate through the list. If the value at position i is > 0, we are increasing the count. After the for loop is completed, we set the last index position value equal to the count.

# 3.
def sum_total(list):
    sum = 0
    for i in list:
        sum = sum + i
    return sum
# print(sum_total([1,2,3,4]))
# Created variable called sum, iterate through list. Set sum = current sum value + the value of the index. Return sum to save.

# 4.
def average(list):
    sum = 0
    avg = 0
    for i in list:
        sum = sum + i
        avg = sum/len(list)
    return avg

# 5.

def length(list):
    size = 0
    for i in list:
        size += 1
    return size
# I know can use the built in function to get length of a list. Tried using a for loop, think it works, but I have an undeclared i
# def length(list):
#     return len(list)

# 6.
def minimum(list):
    min = list[0]
    for i in list:
        if len(list) == 0:
            return False
        elif i < min:
            min = i
    return min

# 7.
def maximum(list):
    max = list[0]
    for i in list:
        if len(list) == 0:
            return False
        elif i > max:
            max = i
    return max
# Same as above, create variable. Set it equal to first index position. As it iterates through this, if the value of i is > current max, reset max to = current i

# 8.
def ultimate_analysis(list):
    new_dict = {'sumTotal': 0, 'average': 0, 'minimum': 0, 'maximum': 0, 'length': 0}
    sumTotal = 0
    average = 0
    minimum = 0
    maximum = 0
    length = 0
    for i in list:
        sumTotal = sumTotal + 1
        average = sumTotal/len(list)
        if i < minimum:
            minimum = i
        if i > maximum:
            maximum = i
        length += 1
    new_dict['sumTotal'] = sumTotal
    new_dict['average'] = average 
    new_dict['minimum'] = minimum 
    new_dict['maximum'] = maximum
    new_dict['length'] = length 
print(ultimate_analysis([37,2,1,-9]))
# Struggled with this, am planning on going over it in a code review tomorrow

# 9.
# Need to come back to this also and review the javascript solution we did last week/code review
def reversed(list):
    list = list[::-1]
    return list