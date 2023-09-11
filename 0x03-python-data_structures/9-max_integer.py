#!/usr/bin/python3

def max_integer(my_list=[]):

    if len(my_list) == 0:

        return ("None")

    x = my_list[0]

    for i in my_list:

        if i > x:

            x = i

    return (x)
<<<<<<< HEAD
=======


>>>>>>> bf9e2de82e4cec68ecf4aea6d965e0ec4f0dabc9
