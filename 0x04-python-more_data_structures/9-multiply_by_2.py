#!/usr/bin/python3

<<<<<<< HEAD
def multiply_by_2(my_dict):

    return {key: val*2 for key, val in my_dict.items()}
=======
def multiply_by_2(a_dictionary):

    new_dir = a_dictionary.copy()

    list_keys = list(new_dir.keys())


    for i in list_keys:

        new_dir[i] *= 2


    return (new_dir)


>>>>>>> bf9e2de82e4cec68ecf4aea6d965e0ec4f0dabc9
