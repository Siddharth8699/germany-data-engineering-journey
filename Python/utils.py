def get_valid_age():

    while True:

        try:
            age = int(input("Enter the age: "))

            if age <= 0:
                print("Age must be greater than 0")

            else:
                return age
            
        except ValueError:
            print("Please enter numbers only")


def get_valid_id():

    while True:

        try:
            student_id = int(input("Enter the id: "))

            if student_id <= 0:
                print("id should be greater than 0")
            
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
                return s.strip()
            else:
                print("Please enter alphabets and spaces only")
            
        
def display_students(rows):

    print()

    print(f"{'ID':<10}{'NAME':<20}{'COUNTRY':<20}{'AGE':<10}")

    print("-" * 60)

    for row in rows:
        print(f"{row[0]:<10}{row[1]:<20}{row[2]:<20}{row[3]:<10}")