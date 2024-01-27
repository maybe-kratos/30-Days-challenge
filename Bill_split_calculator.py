# Roultee

# take the number of people's name in string and
#  randomly select a name form ther list

string_of_people = (input("Enter the names with whitespaces between them =>"))

list_of_people = string_of_people.split(" ")

import random
random_person = random.choice(list_of_people)
print ("The Randomly selected person is ", random_person)