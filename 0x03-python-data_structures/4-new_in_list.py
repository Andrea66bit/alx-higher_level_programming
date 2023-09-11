#!/usr/bin/python3

def new_in_list(my_list, idx, element):

<<<<<<< HEAD
    if idx < 0:

        return my_list

    elif idx >= len(my_list):

        return my_list

    new_list = list(my_list)

    new_list[idx] = element

    return new_list
=======
    tmp_list = my_list[:]

    if 0 <= idx < len(my_list):

        tmp_list[idx] = element

        return(tmp_list)

    return(my_list)


>>>>>>> bf9e2de82e4cec68ecf4aea6d965e0ec4f0dabc9
