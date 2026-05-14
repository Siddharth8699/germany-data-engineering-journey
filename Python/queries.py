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

        print("Error while inserting students")
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

        print("Error while updating students")
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

        print("Error while deleting students")
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


def search_students_by_country(country):

    conn = None
    cur = None

    try:

        conn = get_connection()
        cur = conn.cursor()
        query = "select * from students where country = %s order by id"
        cur.execute(query, (country,))
        rows = cur.fetchall()
        return rows
    
    except Exception as e:
        print("Error while searching students by country")
        print(e)


    finally:

        if cur:
            cur.close()
        if conn:
            conn.close()


def search_students_by_name(name):

    conn = None
    cur = None

    try:
        conn = get_connection()
        cur = conn.cursor()
        query = "select * from students where name ILIKE %s order by id"
        search_name = f"%{name}%"
        cur.execute(query,(search_name,))
        rows = cur.fetchall()
        return rows
    
    except Exception as e:
        print("Error while searching students by name")
        print(e)


    finally:

        if cur:
            cur.close()
        if conn:
            conn.close()


def students_older_than_year_old(age):

    conn = None
    cur = None
    try:
        conn = get_connection()
        cur = conn.cursor()
        query = "select * from students where age > %s order by age"
        cur.execute(query,(age,))
        rows = cur.fetchall()
        return rows
    
    except Exception as e:
        print("Error while searching students by name")
        print(e)


    finally:

        if cur:
            cur.close()
        if conn:
            conn.close()


def students_between_age1_and_age2(age1,age2):

    conn = None
    cur = None
    try:
        conn = get_connection()
        cur = conn.cursor()
        query = "select * from students where age between %s and %s order by age"
        cur.execute(query,(age1,age2))
        rows = cur.fetchall()
        return rows
    
    except Exception as e:
        print("Error while searching students by name")
        print(e)


    finally:

        if cur:
            cur.close()
        if conn:
            conn.close()


def sort_students_by_name():

    conn = None
    cur = None

    try:
        conn = get_connection()
        cur = conn.cursor()
        query = "select * from students order by name"
        cur.execute(query)
        rows = cur.fetchall()
        return rows
    
    except Exception as e:
        print("Error while sorting students by name")
        print(e)


    finally:

        if cur:
            cur.close()
        if conn:
            conn.close()


def sort_students_by_increasing_age():

    conn = None
    cur = None

    try:
        conn = get_connection()
        cur = conn.cursor()
        query = "select * from students order by age asc"
        cur.execute(query)
        rows = cur.fetchall()
        return rows
    
    except Exception as e:
        print("Error while sorting students by age")
        print(e)


    finally:

        if cur:
            cur.close()
        if conn:
            conn.close()


def sort_students_by_decreasing_age():

    conn = None
    cur = None

    try:
        conn = get_connection()
        cur = conn.cursor()
        query = "select * from students order by age desc"
        cur.execute(query)
        rows = cur.fetchall()
        return rows
    
    except Exception as e:
        print("Error while sorting students by age")
        print(e)


    finally:

        if cur:
            cur.close()
        if conn:
            conn.close()


def sort_students_by_country_then_age():

    conn = None
    cur = None

    try:
        conn = get_connection()
        cur = conn.cursor()
        query = "select * from students order by country, age"
        cur.execute(query)
        rows = cur.fetchall()
        return rows
    
    except Exception as e:
        print("Error while sorting students by country,age")
        print(e)


    finally:

        if cur:
            cur.close()
        if conn:
            conn.close()


def total_students():

    conn = None
    cur = None

    try:
        conn = get_connection()
        cur = conn.cursor()
        query = "select count(*) from students"
        cur.execute(query)
        rows = cur.fetchone()
        return rows[0]
    
    except Exception as e:
        print("Error while counting students")
        print(e)


    finally:

        if cur:
            cur.close()
        if conn:
            conn.close()


def average_age_students():

    conn = None
    cur = None

    try:
        conn = get_connection()
        cur = conn.cursor()
        query = "select round(avg(age),2) from students"
        cur.execute(query)
        rows = cur.fetchone()
        return rows[0]
    
    except Exception as e:
        print("Error while calculating average age of students")
        print(e)


    finally:

        if cur:
            cur.close()
        if conn:
            conn.close()



def max_age_students():

    conn = None
    cur = None

    try:
        conn = get_connection()
        cur = conn.cursor()
        query = "select max(Age) from students"
        cur.execute(query)
        rows = cur.fetchone()
        return rows[0]
    
    except Exception as e:
        print("Error while calculating max age of students")
        print(e)


    finally:

        if cur:
            cur.close()
        if conn:
            conn.close()



def min_age_students():

    conn = None
    cur = None

    try:
        conn = get_connection()
        cur = conn.cursor()
        query = "select min(Age) from students"
        cur.execute(query)
        rows = cur.fetchone()
        return rows[0]
    
    except Exception as e:
        print("Error while calculating min age of students")
        print(e)


    finally:

        if cur:
            cur.close()
        if conn:
            conn.close()


def students_per_country():

    conn = None
    cur = None

    try:
        conn = get_connection()
        cur = conn.cursor()
        query = "select country, count(*) from students group by country"
        cur.execute(query)
        rows = cur.fetchall()
        return rows
    
    except Exception as e:
        print("Error while calculating students per country")
        print(e)


    finally:

        if cur:
            cur.close()
        if conn:
            conn.close()


def average_age_per_country():

    conn = None
    cur = None

    try:
        conn = get_connection()
        cur = conn.cursor()
        query = "select country, round(avg(age),2) from students group by country"
        cur.execute(query)
        rows = cur.fetchall()
        return rows
    
    except Exception as e:
        print("Error while calculating average age of students per country")
        print(e)


    finally:

        if cur:
            cur.close()
        if conn:
            conn.close()