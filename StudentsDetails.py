import csv

# Create an empty list to store the student information
students = []

# Loop until the user is done
while True:
    # Prompt the user for the student's roll number
    roll = input("Enter the student's roll number (or 'done' to finish): ")
    if roll.lower() == 'done':
        break
    
    # Prompt the user for the student's name
    name = input("Enter the student's name: ")
    
    # Prompt the user for the student's marks
    marks = input("Enter the student's marks: ")
    
    # Add the student's information to the list
    students.append({'roll': roll, 'name': name, 'marks': marks})

# Open a file for writing
with open('students.csv', 'w', newline='') as csvfile:
    # Create a CSV writer object
    writer = csv.DictWriter(csvfile, fieldnames=['roll', 'name', 'marks'])

    # Write the column headers
    writer.writeheader()

    # Write the student rows
    for student in students:
        writer.writerow(student)

import csv

# Open the CSV file for reading
with open('students.csv', 'r') as csvfile:
    # Create a CSV reader object
    reader = csv.DictReader(csvfile)

    # Create a list to store the modified rows
    rows = []

    # Iterate over the rows in the CSV file
    for row in reader:
        # Get the student's marks
        marks = int(row['marks'])

        # Determine the grade based on the marks
        if marks >= 90:
            grade = 'A'
        elif marks >= 80:
            grade = 'B'
        elif marks >= 70:
            grade = 'C'
        elif marks >= 60:
            grade = 'D'
        elif marks >= 50:
            grade = 'E'
        else:
            grade = 'Fail'

        # Add the grade to the row dictionary
        row['grade'] = grade

        # Add the modified row to the list
        rows.append(row)

# Open the CSV file for writing
with open('students.csv', 'w', newline='') as csvfile:
    # Create a CSV writer object
    writer = csv.DictWriter(csvfile, fieldnames=['roll', 'name', 'marks', 'grade'])
    # Write the column headers
    writer.writeheader()

    # Write the modified rows
    for row in rows:
        writer.writerow(row)

import csv
# Open the CSV file for reading
with open('students.csv', 'r') as f:
  # Create a CSV reader object
    reader = csv.reader(f)
  # Print the table header
    print("------    ----          -----")
  # Iterate through the rows of the CSV file
    for row in reader:
    # Print the student information in a tabular format
        print("{:8}  {:12}  {:4}".format(row[0], row[1], row[2]))
