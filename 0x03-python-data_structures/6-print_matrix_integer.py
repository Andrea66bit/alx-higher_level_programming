#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):

    for i in matrix:

        print(' '.join('{:d}'.format(j)for j in i))
<<<<<<< HEAD
=======


vi 7-add_tuple.py


#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):

    tuple_a += (0, 0)

    tuple_b += (0, 0)

    return(tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
>>>>>>> bf9e2de82e4cec68ecf4aea6d965e0ec4f0dabc9
