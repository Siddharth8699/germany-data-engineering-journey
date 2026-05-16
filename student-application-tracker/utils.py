from datetime import datetime, date

STUDENT_HEADERS = ["ID", "Name", "Country", "Age"]

COMPANY_HEADERS = ["ID", "Company", "Country", "Industry"]

JOB_HEADERS = ["ID", "Title", "Salary", "Location", "Company ID"]

APPLICATION_HEADERS = [
    "ID",
    "Student ID",
    "Job ID",
    "Application Date",
    "Status"
]


def get_valid_age(message="Enter the Age: "):

    while True:

        try:
            age = int(input(message))

            if age <= 0:
                print("Age must be greater than 0")

            else:
                return age
            
        except ValueError:
            print("Please enter numbers only")



def get_valid_salary(message="Enter the Salary: "):

    while True:

        try:
            salary = int(input(message))

            if salary <= 0:
                print("Salary must be greater than 0")

            else:
                return salary
            
        except ValueError:
            print("Please enter a valid salary")


def get_valid_id(message="Enter the ID: "):

    while True:

        try:
            student_id = int(input(message))

            if student_id <= 0:
                print("ID should be greater than 0")

            else:
                return student_id

        except ValueError:
            print("Please enter numbers only")


def get_non_empty_string(prompt):

    while True:

        s = input(prompt)

        if s.strip() == "":
            print("String cant be empty or only have spaces")
        
        else:
            cleaned = s.replace(" ","")
            if cleaned.isalpha():
                return s.strip().title()
            else:
                print("Please enter alphabets and spaces only")
            
        

def display_data(headers, rows):

    print()

    for header in headers:
        print(f"{header:<20}", end=" ")

    print()
    print("-" * (len(headers) * 20))

    for row in rows:
        for value in row:
            print(f"{str(value):<20}", end=" ")
        print()


def get_valid_date(message="Enter the date (YYYY-MM-DD): "):

    while True:

        try:

            date_input = input(message)

            valid_date = datetime.strptime(
                date_input,
                "%Y-%m-%d"
            ).date()

            if valid_date > date.today():
                print("Date cannot be in the future")

            else:
                return valid_date

        except ValueError:
            print("Invalid date format. Use YYYY-MM-DD")