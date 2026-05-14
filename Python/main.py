import queries
import utils

while True:
    try:
        choice = input('''
        1. Student Management
        2. Search & Filtering
        3. Sorting & Ordering
        4. Analytics & Reports
        5. Future Relational Features
        6. Exit
        Enter your choice: ''')

        if choice == "1":

            while True:

                choice = input('''
                1. View All Students
                2. Add Student
                3. Update Student
                4. Delete Student
                5. Back
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

                elif choice == "5":
                    break

                else:
                    print("Enter a valid input")


        elif choice == "2":

            while True:

                choice = input('''
                1. Search By Name
                2. Search By Country
                3. Students Older Than Age
                4. Students Between Ages
                5. Back
                Enter your choice: ''')

                if choice == "1":
                    name = utils.get_non_empty_string("Enter the name: ")
                    rows = queries.search_students_by_name(name)

                    if rows:
                        utils.display_students(rows)

                    else:
                        print("No students found")


                elif choice == "2":
                    country = utils.get_non_empty_string("Enter the country: ")
                    rows = queries.search_students_by_country(country)

                    if rows:
                        utils.display_students(rows)

                    else:
                        print("No students found")



                elif choice == "3":
                    age = utils.get_valid_age()
                    rows = queries.students_older_than_year_old(age)

                    if rows:
                        utils.display_students(rows)

                    else:
                        print("No students found")


                elif choice == "4":
                    age1 = utils.get_valid_age()
                    age2 = utils.get_valid_age()
                    rows = queries.students_between_age1_and_age2(age1,age2)

                    if rows:
                        utils.display_students(rows)

                    else:
                        print("No students found")

                elif choice == "5":
                    break

                else:
                    print("Enter a valid input")


        elif choice == "3":

            while True:

                choice = input('''
                1. Sort By Name
                2. Sort By Age Ascending
                3. Sort By Age Descending
                4. Sort By Country Then Age
                5. Back
                Enter your choice: ''')

                if choice == "1":
                    rows = queries.sort_students_by_name()
                    if rows:
                        utils.display_students(rows)

                    else:
                        print("No students found")

                elif choice == "2":
                    rows = queries.sort_students_by_increasing_age()
                    if rows:
                        utils.display_students(rows)

                    else:
                        print("No students found")

                elif choice == "3":
                    rows = queries.sort_students_by_decreasing_age()
                    if rows:
                        utils.display_students(rows)

                    else:
                        print("No students found")

                elif choice == "4":
                    rows = queries.sort_students_by_country_then_age()
                    if rows:
                        utils.display_students(rows)

                    else:
                        print("No students found")

                elif choice == "5":
                    break

                else:
                    print("Enter a valid input")


        elif choice == "4":

            while True:

                choice = input('''
                1. Total Students
                2. Average Student Age
                3. Youngest Student
                4. Oldest Student
                5. Students Per Country
                6. Average Age Per Country
                7. Back
                Enter your input: ''')

                if choice == "1":
                    rows = queries.total_students()
                    print(rows)

                elif choice == "2":
                    rows = queries.averae_age_students()
                    print(rows)

                elif choice == "3":
                    rows = queries.min_age_students()
                    print(rows)

                elif choice == "4":
                    rows = queries.max_age_students()
                    print(rows)

                elif choice == "5":
                    rows = queries.students_per_country()
                    for row in rows:
                        print(row)

                elif choice == "6":
                    rows = queries.average_age_per_country()
                    for row in rows:
                        print(row)

                elif choice == "7":
                    break

                else:
                    print("Enter a valid input")













        elif choice == "5":

            while True:

                choice = input('''
                1. Course Management
                2. Student Enrollments
                3. View Student Courses
                4. View Course Students
                5. Back''')


        
            

        


        


        

    except Exception as e:
        print("Something went wrong")
        print(e)


