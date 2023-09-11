#!/usr/bin/python3

def replace_in_list(my_list, idx, element):

<<<<<<< HEAD
    if idx < 0:

        return my_list

    if idx >= len(my_list):

        return my_list

    my_list[idx] = element

    return my_list
=======
    if 0 <= idx < len(my_list):

        my_list[idx] = element

    return(my_list)
>>>>>>> bf9e2de82e4cec68ecf4aea6d965e0ec4f0dabc9
