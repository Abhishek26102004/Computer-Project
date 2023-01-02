import csv

# Create an empty list to store the student information
students = []

# Loop until the user is done
while True:
    # Prompt the user for the student's BatchID number
    BatchID = input("Enter the student's BatchID (or 'done' to finish): ")
    if BatchID.lower() == 'done':
        break
    
    # Prompt the user for the student's name
    BatchName = input("Enter the Batch Name: ")
    
    # Prompt the user for the student's marks
    marks = input("Enter the student's Marks in percentage:")
    # Prompt the user for the student's Department Name
    DepartmentName = input("Enter the student's Department Name: ")
    # Prompt the user for the student's List of Corse
    ListofCourses = input("Enter the student's List of Courses: ")

    ListofStudents = input("Enter the student's List: ")
    
    # Add the student's information to the list
    students.append({'BatchID':BatchID,'BatchName':BatchName, 'marks': marks,'DepartmentName':DepartmentName, 'ListofCourses':ListofCourses,'ListofStudents':ListofStudents})

# Open a file for writing
with open('students.csv', 'w', newline='') as csvfile:
    # Create a CSV writer object
    writer = csv.DictWriter(csvfile, fieldnames=['BatchID', 'BatchName', 'marks','DepartmentName','ListofCourses','ListofStudents'])
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
    writer = csv.DictWriter(csvfile, fieldnames=['BatchID', 'BatchName', 'marks', 'grade','DepartmentName','ListofCourses','ListofStudents'])
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
