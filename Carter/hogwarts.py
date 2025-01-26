#define a list of dictionaries, where each dictionary represents a student
#Each student has a name, house, and a patronus.
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": "None"}
]
#Iterate over the list of students using enumerate to get both the index and student data
#start index at 1 for user-friendly numbering
for index, student in enumerate(students, 1):
    #print the student's information in a formatted string
    #The output includes the student's number, name, house and patronus
    print(f'{index}. {student["name"]}, {student["house"]}, {student["patronus"]}')


    #remember
