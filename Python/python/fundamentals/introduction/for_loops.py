def basic():
    print("Basic:")
    for i in range(150):
        print(i+1)
    return
def multiples_of_Five():
    print("Mutliples Of Five:")
    for i in range(5, 1001, 5):
        print(i)
    return
def counting_the_dojo_way():
    print("Counting, the Dojo Way:")
    for i in range(1, 101):
        if(i % 5 == 0 and (i % 10 == 0)):
            print("Coding Dojo " + str(i))
        elif(i % 5 == 0):
            print("Coding " + str(i))
    return
def whoa_that_sucker_huge():
    print("Whoa. That Sucker's Huge:")
    sum = 0
    for i in range(500001):
        if(i / 2 != 0):
            sum = sum + i
    print(sum)
    return
def countdown_by_fours():
    print("Countdown by Fours:")
    for i in range(2018, 0, -4):
        print(i)
    return
def flexible_counter():
    print("Flexible Counter:")
    lowNum = 3
    highNum = 9
    mult = 3
    for i in range(lowNum, highNum+1, 1):
        if(i % mult == 0):
            print(i)
    return

basic()
multiples_of_Five()
counting_the_dojo_way()
whoa_that_sucker_huge()
countdown_by_fours()
flexible_counter()