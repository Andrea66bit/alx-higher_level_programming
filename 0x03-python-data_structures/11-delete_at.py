#!/usr/bin/python3

def delete_at(my_list=[], idx=0):

<<<<<<< HEAD
    if idx < 0:

        return my_list

    elif idx >= len(my_list):

        return my_list

    del my_list[idx]

    return my_list
=======
    if 0 <= idx < len(my_list):

        del(my_list[idx])

    return(my_list)
>>>>>>> bf9e2de82e4cec68ecf4aea6d965e0ec4f0dabc9
