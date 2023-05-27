# What This Code does:

# input:
# Hi Hell

# output:
# Jk Lipp

# logic:
# take a string as an input "Hi Hell" and shift the
# first string by the length of it:

# "Hi" --> "Jk" | since the length is 2. We shift each letter by 2.
# "Hell" --> "Lipp"

# note: cases must be the same.

import string
alpha_list = list(string.ascii_lowercase) # to initialize alphabets as a list

def shiftAndMirror(word):
    splittedList = word.split(" ") # splittedList = ["Hi","Hell"]
    modList = [] # list for storing modified input
    for worde in splittedList:
        single = list(worde) # single = ["H","i"]
        single_len = len(single) # self explanatory
        String = ""
        for value in single: # value = H and so on..
            value_index = alpha_list.index(value.lower())
            mod_index = (value_index + single_len) % 26
            if value.isupper() == True: # Checking if the input value is UPPER CASE.
                String = String + alpha_list[mod_index].upper() # if yes we concat the output in UPPER CASE
            else:
                String = String + alpha_list[mod_index] # if no just concat. That's it.
        modList.append(String) # we append the output string in modList, modList = ["Jk","Lipp"]
    return " ".join(modList) # we join and return the value "Jk Lipp"


input_string = input("Enter the string: ")
print(shiftAndMirror(word = input_string))