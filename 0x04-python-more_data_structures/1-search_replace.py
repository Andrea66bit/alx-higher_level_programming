#!/usr/bin/python3

def search_replace(my_list, search, replace):

<<<<<<< HEAD
    return [replace if search == n else n for n in my_list]
=======
    new_list = list(map(lambda x: replace if x == search else x, my_list))

    return (new_list)
>>>>>>> bf9e2de82e4cec68ecf4aea6d965e0ec4f0dabc9
