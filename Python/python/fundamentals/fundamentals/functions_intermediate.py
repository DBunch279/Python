x = [ [5, 2, 3] , [10, 8, 9] ]
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Ronney']
}
z = [ {'x' : 10, 'y' : 20} ]

print("Change Values within Items : ")
def changevalue(number, last_name, name_change, number_dict):
    x[1][0] = number
    students[0]['last_name'] = last_name
    sports_directory['soccer'][0] = name_change
    z[0]['y'] = number_dict
    print(x)
    print(students)
    print(sports_directory)
    print(z)
changevalue(15, 'Bryant', 'Andres', 30)
print("")

print("Iterate Through Dictionary : ")
def interate_dictionary(list):
    for i in range(0, len(list), 1):
        print("first_name - " + str(list[i]['first_name'] + ", last_name - " + str(list[i]['last_name'])))
interate_dictionary(students)
print("")

print("Iterate Through Dictionary 2 : ")
def iterate_dictionary2(key_name, some_list = []):
    new_array = []
    for i in range (0, len(some_list), 1):
        new_array.append(some_list[i][key_name])
    return new_array
print(iterate_dictionary2("first_name", students))
print(iterate_dictionary2("last_name", students))
print("")

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
print("Iterate Through Dictionary 3 : ")
def printinfo(key_name, some_dict = {}):
    new_array = []
    for i in range(0, len(some_dict[key_name]), 1):
        new_array.append(some_dict[key_name][i])
    return new_array
print(printinfo('locations', dojo))
print(printinfo('instructors', dojo))

