#!/usr/bin/python3

<<<<<<< HEAD
def best_score(my_dict):

    return max(my_dict, key=my_dict.get) if my_dict else None


=======
def best_score(a_dictionary):

    if not a_dictionary:

        return (None)


    return (max(a_dictionary, key=a_dictionary.get))
>>>>>>> bf9e2de82e4cec68ecf4aea6d965e0ec4f0dabc9
