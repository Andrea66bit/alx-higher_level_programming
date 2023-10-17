#!/usr/bin/python3

<<<<<<< HEAD
def simple_delete(my_dict, key=""):

    my_dict.pop(key, None)

    return my_dict
=======
def simple_delete(a_dictionary, key=""):

    if a_dictionary.get(key) is not None:

        del a_dictionary[key]

    return (a_dictionary)


>>>>>>> bf9e2de82e4cec68ecf4aea6d965e0ec4f0dabc9
