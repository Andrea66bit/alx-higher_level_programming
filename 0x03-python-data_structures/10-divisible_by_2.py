#!/usr/bin/python3

def divisible_by_2(my_list=[]):

<<<<<<< HEAD
    new_list = []

    if my_list:

        for num in my_list:

            new_list.append(False if num % 2 else True)

        return new_list
=======
    boolist = my_list[:]

    for count, i in enumerate(my_list):

        if i % 2 == 0:

            boolist[count] = True

        else:

            boolist[count] = False

    return(boolist)


>>>>>>> bf9e2de82e4cec68ecf4aea6d965e0ec4f0dabc9
