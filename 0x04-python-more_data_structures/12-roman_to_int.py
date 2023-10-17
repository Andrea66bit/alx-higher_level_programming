#!/usr/bin/python3

<<<<<<< HEAD
def roman_to_int(roman_string: str):

    if roman_string is None or type(roman_string) != str:

        return 0

    data = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    numbers = [data[x] for x in roman_string] + [0]

    rep = 0


    for i in range(len(numbers) - 1):

        if numbers[i] >= numbers[i+1]:

            rep += numbers[i]

        else:

            rep -= numbers[i]


    return rep
=======
def to_subtract(list_num):

    to_sub = 0

    max_list = max(list_num)


    for n in list_num:

        if max_list > n:

            to_sub += n


    return (max_list - to_sub)



def roman_to_int(roman_string):

    if not roman_string:

        return 0


    if not isinstance(roman_string, str):

        return 0


    rom_n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    list_keys = list(rom_n.keys())


    num = 0

    last_rom = 0

    list_num = [0]


    for ch in roman_string:

        for r_num in list_keys:

            if r_num == ch:

                if rom_n.get(ch) <= last_rom:

                    num += to_subtract(list_num)

                    list_num = [rom_n.get(ch)]

                else:

                    list_num.append(rom_n.get(ch))


                last_rom = rom_n.get(ch)


    num += to_subtract(list_num)


    return (num)
>>>>>>> bf9e2de82e4cec68ecf4aea6d965e0ec4f0dabc9
