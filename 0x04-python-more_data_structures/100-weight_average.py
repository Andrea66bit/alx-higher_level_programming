#!/usr/bin/python3

def weight_average(my_list=[]):

    if not my_list:

        return 0


    num = 0

    den = 0


    for tup in my_list:

        num += tup[0] * tup[1]

        den += tup[1]


    return (num / den)
<<<<<<< HEAD


=======
>>>>>>> bf9e2de82e4cec68ecf4aea6d965e0ec4f0dabc9
