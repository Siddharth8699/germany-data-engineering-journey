from db_connect import get_connection

def fetch_students():

    conn = None
    cur = None

    try:
        conn = get_connection()
        cur = conn.cursor()
        query = "SELECT * FROM students order by id"
        cur.execute(query)

        rows = cur.fetchall()
        return rows

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
                VALUES (%s, %s, %s) returning *'''
        cur.execute(query, (name, country, age))

        rows = cur.fetchall()
        conn.commit()
        return rows
    

    except Exception as e:

        if conn:
            conn.rollback()

        print("Error while inserting student")
        print(e)

    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

        

def update_student(name, country, age, student_id):

    conn = None
    cur = None

    try:
        conn = get_connection()
        cur = conn.cursor()
        query = '''update students
                set name = %s,
                country = %s,
                age = %s
                where id = %s returning *'''
        cur.execute(query,(name, country, age, student_id))

        rows = cur.fetchall()
        conn.commit()
        return rows

    except Exception as e:

        if conn:
            conn.rollback()

        print("Error while updating student")
        print(e)

    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()



def delete_student(student_id):

    conn = None
    cur = None

    try:
        conn = get_connection()
        cur = conn.cursor()
        query = '''delete from students
                    where id = %s returning *'''
        cur.execute(query,(student_id,))
        
        rows = cur.fetchall()
        conn.commit()
        return rows

    except Exception as e:

        if conn:
            conn.rollback()

        print("Error while deleting student")
        print(e)

    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()


def student_exists(student_id):

    conn = None
    cur = None

    try:

        conn = get_connection()
        cur = conn.cursor()
        query = "select * from students where id = %s"
        cur.execute(query,(student_id,))
        student = cur.fetchone()

        if student is None:
            return False
        
        else:
            return True
        
    except Exception as e:
        print("Error while checking student existence")
        print(e)

        return False

    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()
