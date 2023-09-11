#!/usr/bin/python3

def uniq_add(my_list=[]):

<<<<<<< HEAD
    return sum(set(my_list))
=======
    uniq_list = set(my_list)

    num = 0


    for i in uniq_list:

        num += i


    return (num)
>>>>>>> bf9e2de82e4cec68ecf4aea6d965e0ec4f0dabc9
