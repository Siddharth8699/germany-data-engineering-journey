import queries

try:
    choice = input('''
    1. fetch students
    2. insert student
    3. update student
    4. delete student
    Enter your choice: ''')

    if choice == "1":
        queries.fetch_students()

    elif choice == "2":
        name = input("enter the name: ")
        country = input("enter the country: ")
        age = int(input("enter the age: "))

        queries.insert_student(name,country,age)

    elif choice == "3":
        name = input("enter the name: ")
        country = input("enter the country: ")
        age = int(input("enter the age: "))
        id = int(input("enter the id: "))

        queries.update_student(name,country,age,id)

    elif choice == "4":
        id = int(input("enter the id: "))

        queries.delete_student(id)

    else:
        print("Enter a valid input")

except Exception as e:
    print("Soemthing went wrong")
    print(e)


