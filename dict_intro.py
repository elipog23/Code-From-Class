#--------------------WEEK 2 DAY 2--------------------------
# Dictionaries

# Dictionaries are implemented as hash maps or has tables with hash functions
# A dictionary is a pairing between the set of keys and the set of values.
# Every entry in the dictionary is key : value pair.

phone_pair = {"Mia": "555-424-3376"} # Mia is the key -- phone number is the value.
print(phone_pair) # Prints whole pair w/ curly brackets
print(phone_pair["Mia"]) # Looks up name and prints phone number

# Immutable vs. Mutable types
# Mutable data can be changed and often is in memory. A structured data list is a 
# mutable data structure. Strings are immutable. When it looks like a string is being,
# changed, there is actually a new string object created and the old one is discarded.
# username = ''
# username = last + '_' + first[0]
# username = username + first[1]

# The keys of a dictionary have to be an immutable type. This is so that the 
# hash function obtains the same value everytime.

# Values in a dictionary can be any type/

# Empty dictionary
my_dict = ()

phone_list = {"Caroline" : "555-9375", "Mori" : "555-2838", "Keoki" : "555-9932"}
print(phone_list.keys())
print(phone_list.values())

# Add to dictionary

phone_list["Saanvi"] = "222-5273"

# An exercise for you
def freq_count(phrase):
    '''
    Purpose: Count the number of occurrences for each character in the phrase 
    and return a dictionary with those counts.
    
    Parameters: phrase - the phrase we are getting the frequency for; str
    
    Return Value: - a dictionary with a freq count for each character in phrase'''

    char_count = {}

    for character in phrase:
        if character in char_count:
         char_count[character] += 1
        else:
           char_count[character] = 1

    return char_count

def freq_count_words(phrase):
   '''
   Change freq_count so that it returns the frequency count of words in the phrase
   instead of the characters.
   '''

   word_count = {}

   words = phrase.split()
   
   for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

        return word_count



def classList(students, year):
    '''
    Purpose: To take a dictionary students with student : grad year pairs and produce 
    a list with students who graduate in the parameter year
    
    Parameters:
        students - a dictionary with names as keys and class year as values; dict 
        year -  the year that the students are graduating; int

    Return Value: List of students who are graduating in the year; list
    '''
    names = []

    for person in students:
        if students[person] == year:
            names.append(person)

    return names



    


if __name__ == "__main__":   
    print(freq_count("frizzy"))
    print(freq_count("Today is my birthday and I'm turning 16"))
    print(freq_count_words("Today is my birthday and today I'm going to my home"))



    
