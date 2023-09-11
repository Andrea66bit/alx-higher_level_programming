#!/usr/bin/python3

def element_at(my_list, idx):

<<<<<<< HEAD
    if idx < 0:

        return None

    elif idx >= len(my_list):

        return None

    return my_list[idx]
=======
    return(my_list[idx] if 0 <= idx < len(my_list) else "None")
>>>>>>> bf9e2de82e4cec68ecf4aea6d965e0ec4f0dabc9
