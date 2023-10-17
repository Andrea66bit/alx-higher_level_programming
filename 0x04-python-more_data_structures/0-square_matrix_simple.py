<<<<<<< HEAD
=======

>>>>>>> bf9e2de82e4cec68ecf4aea6d965e0ec4f0dabc9
#!/usr/bin/python3

def square_matrix_simple(matrix=[]):

<<<<<<< HEAD
    squared = []

    for line in matrix:

        squared.append([c**2 for c in line])

    return squared
=======
    new_matrix = matrix.copy()


    for i in range(len(matrix)):

        new_matrix[i] = list(map(lambda x: x**2, matrix[i]))


    return (new_matrix)
>>>>>>> bf9e2de82e4cec68ecf4aea6d965e0ec4f0dabc9
