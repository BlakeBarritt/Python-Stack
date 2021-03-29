# Note: Avoid using class keywords like int, str, list, and dict as variable/parameter names.

#     Update Values in Dictionaries and Lists

    x = [ [5,2,3], [10,8,9] ] 
    students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'}
    ]
    sports_directory = {
        'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
        'soccer' : ['Messi', 'Ronaldo', 'Rooney']
    }
    z = [ {'x': 10, 'y': 20} ]

def update_values(x, students, sports_directory, z):
# Change the value 10 in x to be 15
    x[1][0] = 15
#Change the last_name of the first student
    students[0]['last_name'] = "Bryant"
# Change Messi to Andres in sports_directory
    sports_directory['soccer'][0] = "Andres"
# Change the value of 20 in z to 30
    z[0]['y'] = 30


    Iterate Through a List of Dictionaries

    # Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value. For example, given the following list:

    students = [
             {'first_name':  'Michael', 'last_name' : 'Jordan'},
             {'first_name' : 'John', 'last_name' : 'Rosales'},
             {'first_name' : 'Mark', 'last_name' : 'Guillen'},
             {'first_name' : 'KB', 'last_name' : 'Tonel'}
        ]
    
def iterate_dictionary(some_list):
    # Loop through list
    print_string = ""
    for i in range(len(some_list)) #iterate through some_list - the list of dictionaries
    # Print the keys and values
    for key in some_list[i]: # iterate through each dictionary to access all the keys
        print_string = f"{key} - {some_list[i][key]}"
        print(print_string)
        print_string = ""
    print(f"{} - {}, {} - {}")
    


    iterateDictionary(students) 
    # should output: (it's okay if each key-value pair ends up on 2 separate lines;
    # bonus to get them to appear exactly as below!)
    first_name - Michael, last_name - Jordan
    first_name - John, last_name - Rosales
    first_name - Mark, last_name - Guillen
    first_name - KB, last_name - Tonel

    # Get Values From a List of Dictionaries

    # Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary. For example, iterateDictionary2('first_name', students) should output:

def iterate_dictionary2(key_value, some_list):
    # loop through list
    for i in range(len(some_list)):
        # print the value of the key
        print(some_list[i][key_value])
    
    
    iterate_dictionary2("first_name", students)
    iterate_dictionary2("last_name", students)
    
    Michael
    John
    Mark
    KB

    And iterateDictionary2('last_name', students) should output:

    Jordan
    Rosales
    Guillen
    Tonel

    # Iterate Through a Dictionary with List Values

    # Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with the size of its list, and then prints the associated values within each key's list. For example:

def printInfo(some_dict):
    #Loop through dictionary
    for key in some_dict:
        # print length of list and the key
        print(f"{len(some_dict[key])} {key.upper()}")
        
        # Loop to print each item in the list
        for i in range(len(some_dict[key])):
            print(some_dict[key[i]])

    dojo = {
       'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
       'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
    }
    printInfo(dojo)
    # output:
    7 LOCATIONS
    San Jose
    Seattle
    Dallas
    Chicago
    Tulsa
    DC
    Burbank
        
    8 INSTRUCTORS
    Michael
    Amy
    Eduardo
    Josh
    Graham
    Patrick
    Minh
    Devon

