#Python Functions Basic II
print("CountDown Function :")
def countdown(number):
    countdown = []
    for i in range(number, -1, -1):
        countdown.append(i)
    print(countdown)
countdown(5)
print("")

print("Print and Return Function :")
def print_and_return(print_value, returnvalue):
    print("Printed Value : " + str(print_value))
    return returnvalue
print("Return Value : " + str(print_and_return(1, 2)))
print("")

inputs = [3, 4, 5, 6, 7, 8]
print("First Plus Length : ")
def first_plus_length(list = []):
    firstpluslength = list[0] + len(list)
    outputs = [list[0], len(list), firstpluslength]
    return outputs
print("The First Number is : " + str(first_plus_length(inputs)[0]))
print("The Length Is : " + str(first_plus_length(inputs)[1]))
print("The Sum Is : " + str(first_plus_length(inputs)[2]))
print("")

inputs2 = [4, 5, 5, 1, 7, 12, 9, 2, 4, 5, 10]
print("Values Greater Than the Second : ")
def values_greater_than_the_second(list = []):
    outputs = []
    if(len(list) < 2):
        return False
    for i in range(0, len(list), 1):
        if(list[i] > list[1]):
            outputs.append(list[i])
    return outputs
print("Base Array : " + str(inputs2))
print("New Array : " + str(values_greater_than_the_second(inputs2)))
print("")

print("This Length, That Value")
def this_length_that_value(length, value):
    num_array = []
    for i in range(0, length, 1):
        num_array.append(value)
    return num_array
print(this_length_that_value(10, 4))
