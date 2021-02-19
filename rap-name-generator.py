# Guided Exploration No. 3
# Joeseph Hall

# imports the random library
import random
# creates an empty list
possible_names = []
# opens the file in write mode
outputFile = open('rap-names-output.txt', 'w')
# opens file as read only mode
with open('rap-names.txt', 'r') as dataFile:
    # finds "name" in the dataFile declared above
    for name in dataFile:
        # appends possible names into name variable and takes off rightmost character
        possible_names.append(name.rstrip())
# asks for an input number
count = int(input('How many rap names would you like to create? '))
# asks for number of name parts
parts = int(input('How many parts should the name contain? '))
for i in range(count):
    # creates name_parts list
    name_parts = []
    # starts a counted loop
    for j in range(parts):
        # jamms all the name parts together into a name
        name_parts.append(
            possible_names[random.randint(0, len(possible_names)-1)])
    # writes the name to the file
    outputFile.write(f"{' '.join(name_parts)}\n")
    # prints the rap names
    print(f"{' '.join(name_parts)}")
# closes the function
outputFile.close()
