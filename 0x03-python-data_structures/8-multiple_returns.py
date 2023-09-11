#!/usr/bin/python3

def multiple_returns(sentence):

<<<<<<< HEAD
    if not sentence:

        sentence = None

    if sentence:

        sen_len = len(sentence)

    else:

        sen_len = 0

    return (sen_len, sentence if not sentence else sentence[:1])
=======
    length = len(sentence)

    first_char = sentence[0] if length > 0 else "None"

    tup = length, first_char

    return(tup)


>>>>>>> bf9e2de82e4cec68ecf4aea6d965e0ec4f0dabc9
