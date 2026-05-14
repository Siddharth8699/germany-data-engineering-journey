import queries
import utils

while True:
    try:
        choice = input('''
        1. fetch students
        2. insert student
        3. update student
        4. delete student
        5. exit
        Enter your choice: ''')

        if choice == "1":
            rows = queries.fetch_students()
            if rows:
                utils.display_students(rows)

            else:
                print("No students found")
            

        elif choice == "2":
            name = utils.get_non_empty_string("Enter the name: ")
            country = utils.get_non_empty_string("Enter the country: ")
            age = utils.get_valid_age()
            rows = queries.insert_student(name,country,age)
            utils.display_students(rows)

        elif choice == "3":
            student_id = utils.get_valid_id()

            if queries.student_exists(student_id):
                name = utils.get_non_empty_string("Enter the name: ")
                country = utils.get_non_empty_string("Enter the country: ")
                age = utils.get_valid_age()

                rows = queries.update_student(name,country,age,student_id)
                utils.display_students(rows)

            else:
                print("Student not found")

        elif choice == "4":
            id = utils.get_valid_id()

            if queries.student_exists(student_id):
                rows = queries.delete_student(student_id)
                utils.display_students(rows)

            else:
                print("Student not found")


        elif choice == '5':
            print("Closing EduFlow...")
            break

        else:
            print("Enter a valid input")

    except Exception as e:
        print("Something went wrong")
        print(e)


