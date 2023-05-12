from Stack import *


# Only one disk can be moved at a time.
# Each move consists of taking the upper disk from one
# of the stacks and placing it on top of another stack or on an empty rod.
# No disk may be placed on top of a smaller disk.
# user input

def print_stacks(stack_list):
    count = 1
    for stack in stack_list:
        print("Stack" + str(count) + " : ", end="")
        (stack.print_stack()) #MAKE PRINT STACK FROM BOTTOM TO TOP -> have stack start at bottom by going through stack
        #have a list of all the ones popped.and then return that list
        count += 1


# stacks list
stack_list = []

# add all elements
num_elements = input("How many disks would you like: ")
while (isinstance(num_elements, int)):
    num_elements = input("Invalid number. How many would you like? ")

num_elements = int(num_elements)

count = num_elements
for i in range(num_elements):
    stack_list.append(Stack())
    stack_list[0].push_v(count)
    count -= 1  # makes num decend

print_stacks(stack_list)
