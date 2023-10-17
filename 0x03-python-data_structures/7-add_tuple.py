#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):

<<<<<<< HEAD
    len_a, len_b = len(tuple_a), len(tuple_b)

    new_tuple = ((tuple_a[0] if len_a >= 1 else 0) +

                 (tuple_b[0] if len_b >= 1 else 0),

                 (tuple_a[1] if len_a >= 2 else 0) +

                 (tuple_b[1] if len_b >= 2 else 0))

    return new_tuple
=======
    tuple_a += (0, 0)

    tuple_b += (0, 0)

    return(tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])


>>>>>>> bf9e2de82e4cec68ecf4aea6d965e0ec4f0dabc9
