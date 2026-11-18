phrase = "Robots are the best!"

# Print the first character of the phrase
print(phrase[0])
print(phrase[-20])
print(-len(phrase))

# Print the length of phrase
print(len(phrase))

# If we try to print what is at index 20. Doesn't let you, there isn't actually a 
# character at index 20. IndexError: string index out of range.
# print(phrase[20])

# Print the last character of a string
print(phrase[len(phrase)-1])
print(phrase[19])

#Special Characters
# Escape Characters
# \t - tab
# \n - newline
# \\ - backslash
# \" - quote
# \' - apostrophe

wish = " My first class starts at: \t 11am"
print(wish)

#End allows you to decide how you want to end the line
lunch_main = "Steak"
lunch_side = "Fries"
lunch_drink = "Water"
lunch_dessert = "Cake"
lunch_after = "Ice Cream"
print(lunch_main, end="\t")
print(lunch_side, end="\t")
print(lunch_drink, end=",\t")
print(lunch_dessert, end=" $4.75\n")
print(lunch_after)

# Fstrings
# Fstrings allow us to fill-in-the-blank in a nice way
# {} Tells it to do substitution for what is in the variable you put in
# :.(#)f will round number to decimal place of floating number

lunch_order = f"My lunch order is: {lunch_main} \t {lunch_side} \t {lunch_drink} \t"
dessert_order = f"For Dessert: {lunch_dessert} \t Cost: ${4.756:.2f}"

print(lunch_order)
print(dessert_order)

# String Methods
print(wish.strip()) #Strip gets rid of white space at the beginning and end of a string

wish_list = wish.split() #Split created a list from wish by splitting on spaces or whatever you pass through in split
print(wish_list)

# Comma Seperated Values (csv)
lunch = "sandwich, chips, cauliflower, soda"
lunch_list = lunch.split(',')
print(lunch_list)

def strip_list(list_items):
    '''
    Purpose: TO strip any whitespace at the beginning and end of each item in list_items

    Parameters: list_items - the list of items to be stripped of white space; list str

    Return Value; list_items with the white space removed
    '''

    for index in range(len(list_items)):
        list_items[index] = list_items[index].strip()

    return list_items

print(strip_list(lunch_list))

#--------------------DAY 4---------------------------

# Slicing
# Purpose is to get substrings or subsequences
# string_var[start : stop : skip]
# Start is inclusive and end is exculsive
# Index starts at 0
print(wish)
print(wish[2:6]) # Start at index 2, and end at index 5
print(wish[:6])  # If start isn't specified, assumes start is at index 0
print(wish[5:])  # End not specified, assumes index is the last character.
print(wish[:8:3]) # Start at index 0 and end with index 7, and takes every 3rd character
print(wish[::-1]) # Reverses the string

