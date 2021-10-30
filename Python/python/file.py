# This code is the declaration of all the varibles within the program.
num1 = 42
num2 = 2.3
boolean = True
string = 'Hello World'
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
fruit = ('blueberry', 'strawberry', 'banana')
print(type(fruit)) # This line prints the array of fruit
print(pizza_toppings[1]) # This line prints the "Pepperoni" out of pizza toppings
pizza_toppings.append('Mushrooms')
print(person['name']) # This line prints 'John' out of the person dictionary array
person['name'] = 'George'
person['eye_color'] = 'blue'
print(fruit[2]) # This line prints the 'Jalepenos' out of the fruit array

# These are the condiontals and will print based on what the number is
if num1 > 45:
    print("It's greater")
else:
    print("It's lower") # This line will print

if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!") #This line will print
else:
    print("Just right!")

for x in range(5):
    print(x) #This will print 5 times
for x in range(2,5):
    print(x) #This will print 3 times
for x in range(2,10,3):
    print(x) #This will print 3 times counting by 2 : 2 5 8 
x = 0
while(x < 5):
    print(x)
    x += 1 #This will print 5 times while x is < than 5

pizza_toppings.pop()
pizza_toppings.pop(1)

print(person) # This will print the person array
person.pop('eye_color')
print(person) # This will print the person array without eye color

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement') # This print after 1st if statement always no matter what the topping is
    if topping == 'Olives':
        break

def print_hello_ten_times():
    for num in range(10):
        print('Hello')

print_hello_ten_times() # This prints hello 10 times

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4) # This prints hello x times

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times() # This prints hello 10 times
print_hello_x_or_ten_times(4) # This prints hello x times


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)