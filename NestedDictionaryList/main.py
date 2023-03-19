# PROBLEM 1:
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 
    'last_name' : 'Jordan'},
    {'first_name' : 'John', 
    'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

    # Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
print(x[1][0]) 
x[1][0] = 15
print(x)

    # Change the last_name of the first student from 'Jordan' to 'Bryant'
students[0]['last_name'] = 'Bryant'
print(students[0]['last_name'])

    # In the sports_directory, change 'Messi' to 'Andres'
sports_directory['soccer'][0] = 'Andres'
print(sports_directory['soccer'][0])

    # Change the value 20 in z to 30
z = [ {'x': 10, 'y': 20} ]
z[0]['y'] = 30
print(z[0]['y'])

# PROBLEM 2 & 3
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(some_list):
    for x in range(len(some_list)):
        print (some_list[x])

    for x in students:
        print(x)

iterateDictionary(students)

    # Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, 
    # the function prints the value stored in that key for each dictionary.
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary2(key_name, some_list):
    # key_name = 'first_name' or 'last_name' (it's just a name for a parameter and we call back to it @iterateDictionary2('first_name,students))
    # some_list = students (it's just a name for a paramter) we call back to some_list when we call on students 
    for x in some_list:
        print(x[key_name])

iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)

# PROBLEM 4
# Create a function printInfo(some_dict) that given a dictionary whose values are all lists, 
# prints the name of each key along with the size of its list, 
# and then prints the associated values within each key's list.

dojo = {
'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

# some_dict is a paramter for dojo
# some_dict == dojo 
def printInfo(some_dict):
    print(len(some_dict['locations']), 'LOCATIONS')
    for x in some_dict['locations']:
        print(x)

    print(len(some_dict['instructors']), 'INSTRUCTORS')
    for y in some_dict['instructors']:
        print(y)

printInfo(dojo)




