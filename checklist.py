#!/usr/bin/env python
# -*- coding: utf-8 -*-
print("Hello World")
checklist = list()

def my_fun_function(say_this):
    print(say_this)

my_fun_function("Hello World")

checklist.append("Hello")
print(checklist)

checklist.append("World")
print(checklist)

def create(item):
    checklist.append(item)

 # checklist[0]

def read(index):
     item = checklist[index]
     print(item)

def update(index, item):
    checklist[index] = item

def destroy(index):
    checklist.pop(index)

def list_all_items():
    index = 0
    for list_items in checklist:
        print("{}- {}".format(index, list_items))
        index += 1

def test():
    create("purple sox")
    create("red cloak")
    print(read(0))
    print(read(1))
    update(0, "purple socks")
    destroy(1)
    print(read(0))
    print(read(1))
    list_all_items()

test()

def mark_completed(index):
    check =  "√"
    print("{} {}".format(check, index))

mark_completed(0)

def select(function_code):
    # Create item
    if function_code == "C":
        input_item = user_input("Input item: ")
        create(input_item)

    # Read item
    elif function_code == "R":
        item_index = user_input("Index Number? ")

        # Remember that item_index must actually exist or our program will crash.
        read(int(item_index))

    elif function_code == "Q":
        # This is where we want to stop our loop
        return False

    # Print all items
    elif function_code == "P":
        list_all_items()

    # Catch all
    else:
        print("Unknown Option")


def user_input(prompt):
    # the input function will display a message in the terminal
    # and wait for user input.
    user_input = raw_input(prompt)
    return user_input

user_value = user_input("Please Enter a value: ")
print(user_value)


running = True
while running:
    selection = user_input("Press C to add to list, R to Read from list, P to display list, and Q to quit: ")
    running = select(selection)
