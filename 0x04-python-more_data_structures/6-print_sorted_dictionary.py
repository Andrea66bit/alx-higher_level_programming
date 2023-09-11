#!/usr/bin/python3

<<<<<<< HEAD
def print_sorted_dictionary(my_dict):

    for k in sorted(my_dict.keys()):

        print("{}: {}".format(k, my_dict[k]))
=======
def print_sorted_dictionary(a_dictionary):

    list_ord = list(a_dictionary.keys())

    list_ord.sort()

    for i in list_ord:

        print("{}: {}".format(i, a_dictionary.get(i)))
>>>>>>> bf9e2de82e4cec68ecf4aea6d965e0ec4f0dabc9
