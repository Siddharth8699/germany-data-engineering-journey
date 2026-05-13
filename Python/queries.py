from db_connect import get_connection

def fetch_students():

    conn = None
    cur = None

    try:
        conn = get_connection()
        cur = conn.cursor()
        query = "SELECT * FROM students"
        cur.execute(query)

        rows = cur.fetchall()
        for row in rows:
            print(row)

    except Exception as e:
        print("Error while fetching students")
        print(e)


    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()



    

    

def insert_student(name, country, age):

    conn = None
    cur = None

    try:
        conn = get_connection()
        cur = conn.cursor()
        query = '''INSERT INTO students(name, country, age)
                VALUES (%s, %s, %s)'''
        cur.execute(query, (name, country, age))

        conn.commit()
        print("Student inserted successfully")

    except Exception as e:
        print("Error while inserting student")
        print(e)

    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

        

    


def update_student(name, country, age, id):

    conn = None
    cur = None

    try:
        conn = get_connection()
        cur = conn.cursor()
        query = '''update students
                set name = %s,
                country = %s,
                age = %s
                where id = %s'''
        cur.execute(query,(name, country, age, id))

        conn.commit()
        print("Student updated successfully")

    except Exception as e:
        print("Error while updating student")
        print(e)

    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()




def delete_student(id):

    conn = None
    cur = None

    try:
        conn = get_connection()
        cur = conn.cursor()
        query = '''delete from students
                    where id = %s'''
        cur.execute(query,(id,))

        conn.commit()
        print("Student deleted successfully")

    except Exception as e:
        print("Error while deleting student")
        print(e)

    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

