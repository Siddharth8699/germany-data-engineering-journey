from db_connect import get_connection


# =========================
# STUDENT QUERIES
# =========================


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
        query = "select * from students where country ILIKE %s order by id"
        search_name = f"%{country}%"
        cur.execute(query,(search_name,))
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
        query = "select country, round(avg(age), 2) AS average_age from students group by country"
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


# =========================
# COMPANY QUERIES
# =========================


def fetch_companies():

    conn = None
    cur = None

    try:
        conn = get_connection()
        cur = conn.cursor()
        query = "SELECT * FROM companies order by id"
        cur.execute(query)

        rows = cur.fetchall()
        return rows

    except Exception as e:
        print("Error while fetching companies")
        print(e)


    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()


def insert_company(company_name, country, industry):

    conn = None
    cur = None

    try:
        conn = get_connection()
        cur = conn.cursor()
        query = '''INSERT INTO companies(company_name, country, industry)
                VALUES (%s, %s, %s) returning *'''
        cur.execute(query, (company_name, country, industry))

        rows = cur.fetchall()
        conn.commit()
        return rows
    

    except Exception as e:

        if conn:
            conn.rollback()

        print("Error while inserting companies")
        print(e)

    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()


def update_companies(company_name, country, industry, company_id):

    conn = None
    cur = None

    try:
        conn = get_connection()
        cur = conn.cursor()
        query = '''update companies
                set company_name = %s,
                country = %s,
                industry = %s
                where id = %s returning *'''
        cur.execute(query,(company_name, country, industry, company_id))

        rows = cur.fetchall()
        conn.commit()
        return rows

    except Exception as e:

        if conn:
            conn.rollback()

        print("Error while updating companies")
        print(e)

    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()


def company_exists(company_id):

    conn = None
    cur = None

    try:

        conn = get_connection()
        cur = conn.cursor()
        query = "select * from companies where id = %s"
        cur.execute(query,(company_id,))
        student = cur.fetchone()

        if student is None:
            return False
        
        else:
            return True
        
    except Exception as e:
        print("Error while checking company existence")
        print(e)

        return False

    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()


def delete_company(company_id):

    conn = None
    cur = None

    try:
        conn = get_connection()
        cur = conn.cursor()
        query = '''delete from companies
                    where id = %s returning *'''
        cur.execute(query,(company_id,))
        
        rows = cur.fetchall()
        conn.commit()
        return rows

    except Exception as e:

        if conn:
            conn.rollback()

        print("Error while deleting companies")
        print(e)

    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()


def search_companies_by_name(company_name):

    conn = None
    cur = None

    try:
        conn = get_connection()
        cur = conn.cursor()
        query = "select * from companies where company_name ILIKE %s order by id"
        search_name = f"%{company_name}%"
        cur.execute(query,(search_name,))
        rows = cur.fetchall()
        return rows
    
    except Exception as e:
        print("Error while searching companies by name")
        print(e)


    finally:

        if cur:
            cur.close()
        if conn:
            conn.close()


def search_companies_by_country(country):

    conn = None
    cur = None

    try:

        conn = get_connection()
        cur = conn.cursor()
        query = "select * from companies where country ILIKE %s order by id"
        search_country = f"%{country}%"
        cur.execute(query,(search_country,))
        rows = cur.fetchall()
        return rows
    
    except Exception as e:
        print("Error while searching companies by country")
        print(e)


    finally:

        if cur:
            cur.close()
        if conn:
            conn.close()


def search_companies_by_industry(industry):

    conn = None
    cur = None

    try:

        conn = get_connection()
        cur = conn.cursor()
        query = "select * from companies where industry ILIKE %s order by id"
        search_industry = f"%{industry}%"
        cur.execute(query,(search_industry,))
        rows = cur.fetchall()
        return rows
    
    except Exception as e:
        print("Error while searching companies by industry")
        print(e)


    finally:

        if cur:
            cur.close()
        if conn:
            conn.close()


def sort_companies_by_company_name():

    conn = None
    cur = None

    try:
        conn = get_connection()
        cur = conn.cursor()
        query = "select * from companies order by company_name"
        cur.execute(query)
        rows = cur.fetchall()
        return rows
    
    except Exception as e:
        print("Error while sorting companies by name")
        print(e)


    finally:

        if cur:
            cur.close()
        if conn:
            conn.close()


def total_companies():

    conn = None
    cur = None

    try:
        conn = get_connection()
        cur = conn.cursor()
        query = "select count(*) from companies"
        cur.execute(query)
        rows = cur.fetchone()
        return rows[0]
    
    except Exception as e:
        print("Error while calculating companies")
        print(e)


    finally:

        if cur:
            cur.close()
        if conn:
            conn.close()


def companies_per_country():

    conn = None
    cur = None

    try:
        conn = get_connection()
        cur = conn.cursor()
        query = "select country, count(*) from companies group by country"
        cur.execute(query)
        rows = cur.fetchall()
        return rows
    
    except Exception as e:
        print("Error while calculating companies per country")
        print(e)


    finally:

        if cur:
            cur.close()
        if conn:
            conn.close()

def companies_per_industry():

    conn = None
    cur = None

    try:
        conn = get_connection()
        cur = conn.cursor()
        query = "select industry, count(*) from companies group by industry"
        cur.execute(query)
        rows = cur.fetchall()
        return rows
    
    except Exception as e:
        print("Error while calculating companies per industry")
        print(e)


    finally:

        if cur:
            cur.close()
        if conn:
            conn.close()


# =========================
# JOBS QUERIES
# =========================

def fetch_jobs():

    conn = None
    cur = None

    try:
        conn = get_connection()
        cur = conn.cursor()
        query = "SELECT * FROM jobs order by id"
        cur.execute(query)

        rows = cur.fetchall()
        return rows

    except Exception as e:
        print("Error while fetching jobs")
        print(e)


    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()



def insert_job(title, salary, location, company_id):

    conn = None
    cur = None

    try:
        conn = get_connection()
        cur = conn.cursor()
        query = '''INSERT INTO jobs(title, salary, location, company_id)
                VALUES (%s, %s, %s, %s) returning *'''
        cur.execute(query, (title, salary, location, company_id))

        rows = cur.fetchall()
        conn.commit()
        return rows
    

    except Exception as e:

        if conn:
            conn.rollback()

        print("Error while inserting companies")
        print(e)

    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()


def fetch_company_ids_and_names():

    conn = None
    cur = None

    try:
        conn = get_connection()
        cur = conn.cursor()
        query = '''select id, company_name from companies order by id'''
        cur.execute(query)

        rows = cur.fetchall()
        conn.commit()
        return rows
    

    except Exception as e:

        if conn:
            conn.rollback()

        print("Error while fetching companies id and name")
        print(e)

    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()



def job_exists(job_id):

    conn = None
    cur = None

    try:

        conn = get_connection()
        cur = conn.cursor()
        query = "select * from jobs where id = %s"
        cur.execute(query,(job_id,))
        student = cur.fetchone()

        if student is None:
            return False
        
        else:
            return True
        
    except Exception as e:
        print("Error while checking company existence")
        print(e)

        return False

    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()



def update_jobs(title, salary, location, company_id, job_id):

    conn = None
    cur = None

    try:
        conn = get_connection()
        cur = conn.cursor()
        query = '''update jobs
                set title = %s,
                salary = %s,
                location = %s,
                company_id = %s
                where id = %s returning *'''
        cur.execute(query,(title, salary, location, company_id, job_id))

        rows = cur.fetchall()
        conn.commit()
        return rows

    except Exception as e:

        if conn:
            conn.rollback()

        print("Error while updating jobs")
        print(e)

    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()



def delete_job(job_id):

    conn = None
    cur = None

    try:
        conn = get_connection()
        cur = conn.cursor()
        query = '''delete from jobs
                    where id = %s returning *'''
        cur.execute(query,(job_id,))
        
        rows = cur.fetchall()
        conn.commit()
        return rows

    except Exception as e:

        if conn:
            conn.rollback()

        print("Error while deleting jobs")
        print(e)

    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()


def search_jobs_by_title(title):

    conn = None
    cur = None

    try:
        conn = get_connection()
        cur = conn.cursor()
        query = "select * from jobs where title ILIKE %s order by id"
        search_name = f"%{title}%"
        cur.execute(query,(search_name,))
        rows = cur.fetchall()
        return rows
    
    except Exception as e:
        print("Error while searching companies by name")
        print(e)


    finally:

        if cur:
            cur.close()
        if conn:
            conn.close()


def search_jobs_by_location(location):

    conn = None
    cur = None

    try:
        conn = get_connection()
        cur = conn.cursor()
        query = "select * from jobs where location ILIKE %s order by id"
        search_name = f"%{location}%"
        cur.execute(query,(search_name,))
        rows = cur.fetchall()
        return rows
    
    except Exception as e:
        print("Error while searching companies by name")
        print(e)


    finally:

        if cur:
            cur.close()
        if conn:
            conn.close()


def jobs_with_salary_above(salary):

    conn = None
    cur = None
    try:
        conn = get_connection()
        cur = conn.cursor()
        query = "select * from jobs where salary > %s order by salary"
        cur.execute(query,(salary,))
        rows = cur.fetchall()
        return rows
    
    except Exception as e:
        print("Error while searching jobs with salaray above")
        print(e)


    finally:

        if cur:
            cur.close()
        if conn:
            conn.close()


def jobs_between_salary1_and_salary2(salary1,salary2):

    conn = None
    cur = None
    try:
        conn = get_connection()
        cur = conn.cursor()
        query = "select * from jobs where salary between %s and %s order by salary"
        cur.execute(query,(salary1, salary2))
        rows = cur.fetchall()
        return rows
    
    except Exception as e:
        print("Error while searching salary in between")
        print(e)


    finally:

        if cur:
            cur.close()
        if conn:
            conn.close()



def sort_jobs_by_salary_increasing():

    conn = None
    cur = None

    try:
        conn = get_connection()
        cur = conn.cursor()
        query = "select * from jobs order by salary asc"
        cur.execute(query)
        rows = cur.fetchall()
        return rows
    
    except Exception as e:
        print("Error while sorting jobs by salary increasingly")
        print(e)


    finally:

        if cur:
            cur.close()
        if conn:
            conn.close()


def sort_jobs_by_salary_decreasing():

    conn = None
    cur = None

    try:
        conn = get_connection()
        cur = conn.cursor()
        query = "select * from jobs order by salary desc"
        cur.execute(query)
        rows = cur.fetchall()
        return rows
    
    except Exception as e:
        print("Error while sorting jobs by salary decreasingly")
        print(e)


    finally:

        if cur:
            cur.close()
        if conn:
            conn.close()



def sort_jobs_by_title():

    conn = None
    cur = None

    try:
        conn = get_connection()
        cur = conn.cursor()
        query = "select * from jobs order by title"
        cur.execute(query)
        rows = cur.fetchall()
        return rows
    
    except Exception as e:
        print("Error while sorting jobs by title")
        print(e)


    finally:

        if cur:
            cur.close()
        if conn:
            conn.close()


def total_jobs():

    conn = None
    cur = None

    try:
        conn = get_connection()
        cur = conn.cursor()
        query = "select count(*) from jobs"
        cur.execute(query)
        rows = cur.fetchone()
        return rows[0]
    
    except Exception as e:
        print("Error while calculating total jobs")
        print(e)


    finally:

        if cur:
            cur.close()
        if conn:
            conn.close()



def average_salary_jobs():

    conn = None
    cur = None

    try:
        conn = get_connection()
        cur = conn.cursor()
        query = "select round(avg(salary), 2) from jobs"
        cur.execute(query)
        rows = cur.fetchone()
        return rows[0]
    
    except Exception as e:
        print("Error while calculating average salary job")
        print(e)


    finally:

        if cur:
            cur.close()
        if conn:
            conn.close()



def highest_paying_job():

    conn = None
    cur = None

    try:
        conn = get_connection()
        cur = conn.cursor()
        query = "select * from jobs order by salary desc limit 1"
        cur.execute(query)
        rows = cur.fetchall()
        return rows
    
    except Exception as e:
        print("Error while calculating highest salary job")
        print(e)


    finally:

        if cur:
            cur.close()
        if conn:
            conn.close()



def lowest_paying_job():

    conn = None
    cur = None

    try:
        conn = get_connection()
        cur = conn.cursor()
        query = "select * from jobs order by salary asc limit 1"
        cur.execute(query)
        rows = cur.fetchall()
        return rows
    
    except Exception as e:
        print("Error while calculating lowest salary job")
        print(e)


    finally:

        if cur:
            cur.close()
        if conn:
            conn.close()


    
# =========================
# Applications QUERIES
# =========================


def fetch_applications():

    conn = None
    cur = None

    try:
        conn = get_connection()
        cur = conn.cursor()
        query = "SELECT * FROM applications order by id"
        cur.execute(query)

        rows = cur.fetchall()
        return rows

    except Exception as e:
        print("Error while fetching jobs")
        print(e)


    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()



def insert_applications(student_id, job_id, application_date, status):

    conn = None
    cur = None

    try:
        conn = get_connection()
        cur = conn.cursor()
        query = '''INSERT INTO applications(student_id, job_id, application_date, status)
                VALUES (%s, %s, %s, %s) returning *'''
        cur.execute(query, (student_id, job_id, application_date, status))

        rows = cur.fetchall()
        conn.commit()
        return rows
    

    except Exception as e:

        if conn:
            conn.rollback()

        print("Error while inserting companies")
        print(e)

    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()



def fetch_student_ids_and_names():

    conn = None
    cur = None

    try:
        conn = get_connection()
        cur = conn.cursor()
        query = '''select id, name from students order by id'''
        cur.execute(query)

        rows = cur.fetchall()
        conn.commit()
        return rows
    

    except Exception as e:

        if conn:
            conn.rollback()

        print("Error while fetching students id and name")
        print(e)

    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()



def fetch_jobs_ids_and_names():

    conn = None
    cur = None

    try:
        conn = get_connection()
        cur = conn.cursor()
        query = '''select id, title from jobs order by id'''
        cur.execute(query)

        rows = cur.fetchall()
        conn.commit()
        return rows
    

    except Exception as e:

        if conn:
            conn.rollback()

        print("Error while fetching jobs id and name")
        print(e)

    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()



def update_applications(application_date, status, application_id):

    conn = None
    cur = None

    try:
        conn = get_connection()
        cur = conn.cursor()
        query = '''update applications
                set application_date = %s,
                status = %s
                where id = %s returning *'''
        cur.execute(query,(application_date, status, application_id))

        rows = cur.fetchall()
        conn.commit()
        return rows

    except Exception as e:

        if conn:
            conn.rollback()

        print("Error while updating applications")
        print(e)

    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()



def application_exists(application_id):

    conn = None
    cur = None

    try:

        conn = get_connection()
        cur = conn.cursor()
        query = "select * from applications where id = %s"
        cur.execute(query,(application_id,))
        student = cur.fetchone()

        if student is None:
            return False
        
        else:
            return True
        
    except Exception as e:
        print("Error while checking company existence")
        print(e)

        return False

    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()



def delete_application(application_id):

    conn = None
    cur = None

    try:
        conn = get_connection()
        cur = conn.cursor()
        query = '''delete from applications
                    where id = %s returning *'''
        cur.execute(query,(application_id,))
        
        rows = cur.fetchall()
        conn.commit()
        return rows

    except Exception as e:

        if conn:
            conn.rollback()

        print("Error while deleting applications")
        print(e)

    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()



def search_applications_by_status(status):

    conn = None
    cur = None

    try:
        conn = get_connection()
        cur = conn.cursor()
        query = "select * from applications where status ILIKE %s order by id"
        search_name = f"%{status}%"
        cur.execute(query,(search_name,))
        rows = cur.fetchall()
        return rows
    
    except Exception as e:
        print("Error while searching applications by status")
        print(e)


    finally:

        if cur:
            cur.close()
        if conn:
            conn.close()



def search_applications_by_student_id(student_id):

    conn = None
    cur = None

    try:
        conn = get_connection()
        cur = conn.cursor()
        query = "select * from applications where student_id = '%s' order by id"
        cur.execute(query,(student_id,))
        rows = cur.fetchall()
        return rows
    
    except Exception as e:
        print("Error while searching applications by student id")
        print(e)


    finally:

        if cur:
            cur.close()
        if conn:
            conn.close()



def search_applications_by_job_id(job_id):

    conn = None
    cur = None

    try:
        conn = get_connection()
        cur = conn.cursor()
        query = "select * from applications where job_id = '%s' order by id"
        cur.execute(query,(job_id,))
        rows = cur.fetchall()
        return rows
    
    except Exception as e:
        print("Error while searching applications by job id")
        print(e)


    finally:

        if cur:
            cur.close()
        if conn:
            conn.close()



def sort_applications_by_date():

    conn = None
    cur = None

    try:
        conn = get_connection()
        cur = conn.cursor()
        query = "select * from applications order by application_date asc"
        cur.execute(query)
        rows = cur.fetchall()
        return rows
    
    except Exception as e:
        print("Error while sorting applications by application_date")
        print(e)


    finally:

        if cur:
            cur.close()
        if conn:
            conn.close()



def sort_applications_by_status():

    conn = None
    cur = None

    try:
        conn = get_connection()
        cur = conn.cursor()
        query = "select * from applications order by status asc"
        cur.execute(query)
        rows = cur.fetchall()
        return rows
    
    except Exception as e:
        print("Error while sorting applications by status")
        print(e)


    finally:

        if cur:
            cur.close()
        if conn:
            conn.close()



def total_applications():

    conn = None
    cur = None

    try:
        conn = get_connection()
        cur = conn.cursor()
        query = "select count(*) from applications"
        cur.execute(query)
        rows = cur.fetchone()
        return rows[0]
    
    except Exception as e:
        print("Error while calculating total applications")
        print(e)


    finally:

        if cur:
            cur.close()
        if conn:
            conn.close()




def applications_by_status():

    conn = None
    cur = None

    try:
        conn = get_connection()
        cur = conn.cursor()
        query = "select status, count(*) as number_of_applications from applications group by status order by status"
        cur.execute(query)
        rows = cur.fetchall()
        return rows
    
    except Exception as e:
        print("Error while calculating total applications by status")
        print(e)


    finally:

        if cur:
            cur.close()
        if conn:
            conn.close()



def get_students_application_job_and_company():

    conn = None
    cur = None

    try:
        conn = get_connection()
        cur = conn.cursor()
        query = '''select s.name, j.title, c.company_name, a.status from students as s
        join applications as a on s.id = a.student_id
        join jobs as j on a.job_id = j.id
        join companies as c on j.company_id = c.id'''
        cur.execute(query)
        rows = cur.fetchall()
        return rows
    
    except Exception as e:
        print("Error while calculating getting students application job name and company")
        print(e)


    finally:

        if cur:
            cur.close()
        if conn:
            conn.close()



def get_students_applied_to_company(company_name):

    conn = None
    cur = None

    try:
        conn = get_connection()
        cur = conn.cursor()
        query = '''select s.name, c.company_name from students as s
        join applications as a on s.id = a.student_id
        join jobs as j on a.job_id = j.id
        join companies as c on j.company_id = c.id
        where c.company_name ILIKE %s '''
        search_name = f"%{company_name}%"
        cur.execute(query,(search_name,))
        rows = cur.fetchall()
        return rows
    
    except Exception as e:
        print("Error while calculating student applied to a particular company")
        print(e)


    finally:

        if cur:
            cur.close()
        if conn:
            conn.close()



def get_students_with_multiple_applications():

    conn = None
    cur = None

    try:
        conn = get_connection()
        cur = conn.cursor()
        query = '''select s.id, s.name, count(*) as no_of_applications from students as s
        join applications as a on s.id = a.student_id
        group by s.id, s.name
        having count(*) > 1
        order by s.id'''
        cur.execute(query)
        rows = cur.fetchall()
        return rows
    
    except Exception as e:
        print("Error while calculating getting students application job name and company")
        print(e)


    finally:

        if cur:
            cur.close()
        if conn:
            conn.close()



def get_job_openings_per_company():

    conn = None
    cur = None

    try:
        conn = get_connection()
        cur = conn.cursor()
        query = '''select c.id, c.company_name, count(*) as job_openings from jobs as j
                join companies  as c on j.company_id = c.id
                group by c.id, c.company_name
                order by c.id'''
        cur.execute(query)
        rows = cur.fetchall()
        return rows
    
    except Exception as e:
        print("Error while calculating jobs opening per company")
        print(e)


    finally:

        if cur:
            cur.close()
        if conn:
            conn.close()



def get_application_count_per_company():

    conn = None
    cur = None

    try:
        conn = get_connection()
        cur = conn.cursor()
        query = '''select c.id, c.company_name, count(*) as no_of_applications from applications as a
                join jobs as j on a.job_id = j.id
                join companies as c on j.company_id = c.id
                group by c.id, c.company_name'''
        cur.execute(query)
        rows = cur.fetchall()
        return rows
    
    except Exception as e:
        print("Error while calculating applications volume per company")
        print(e)


    finally:

        if cur:
            cur.close()
        if conn:
            conn.close()



def get_company_with_highest_applications():

    conn = None
    cur = None

    try:
        conn = get_connection()
        cur = conn.cursor()
        query = '''select c.id, c.company_name, count(*) as no_of_applications from applications as a
                join jobs as j on a.job_id = j.id
                join companies as c on j.company_id = c.id
                group by c.id, c.company_name
                order by count(*) desc
                limit 1'''
        cur.execute(query)
        rows = cur.fetchall()
        return rows
    
    except Exception as e:
        print("Error while calculating company with highest applications")
        print(e)


    finally:

        if cur:
            cur.close()
        if conn:
            conn.close()



def get_company_with_highest_average_salary():

    conn = None
    cur = None

    try:
        conn = get_connection()
        cur = conn.cursor()
        query = '''select c.id, c.company_name, round(avg(salary), 2) as average_salary from jobs as j
                join companies as c on j.company_id = c.id
                group by c.id, c.company_name
                order by average_salary desc
                limit 1'''
        cur.execute(query)
        rows = cur.fetchall()
        return rows
    
    except Exception as e:
        print("Error while calculating company with highest average salary")
        print(e)


    finally:

        if cur:
            cur.close()
        if conn:
            conn.close()



def get_company_open_to_international_students():

    conn = None
    cur = None

    try:
        conn = get_connection()
        cur = conn.cursor()
        query = '''select s.name, s.country, c.company_name, c.country, a.status from students as s
                join applications as a on s.id = a.student_id
                join jobs as j on a.job_id = j.id
                join companies as c on j.company_id = c.id
                where s.country <> c.country
                order by s.name'''
        cur.execute(query)
        rows = cur.fetchall()
        return rows
    
    except Exception as e:
        print("Error while calculating company with international students")
        print(e)


    finally:

        if cur:
            cur.close()
        if conn:
            conn.close()



def get_all_jobs_info():

    conn = None
    cur = None

    try:
        conn = get_connection()
        cur = conn.cursor()
        query = '''select j.id, j.title, c.company_name, c.country, j.salary from jobs as j
        join companies as c on j.company_id = c.id
        order by j.id'''
        cur.execute(query)
        rows = cur.fetchall()
        return rows
    
    except Exception as e:
        print("Error while getting all jobs")
        print(e)


    finally:

        if cur:
            cur.close()
        if conn:
            conn.close()



def get_highest_5_paying_jobs():

    conn = None
    cur = None

    try:
        conn = get_connection()
        cur = conn.cursor()
        query = '''select j.id, j.title, c.company_name, c.country, j.salary from jobs as j
        join companies as c on j.company_id = c.id
        order by j.salary desc
        limit 5'''
        cur.execute(query)
        rows = cur.fetchall()
        return rows
    
    except Exception as e:
        print("Error while getting highest 5 paying jobs")
        print(e)


    finally:

        if cur:
            cur.close()
        if conn:
            conn.close()



def get_average_salary_by_industry():

    conn = None
    cur = None

    try:
        conn = get_connection()
        cur = conn.cursor()
        query = '''select c.industry, round(avg(j.salary), 2) as average_salary from jobs as j
                join companies as c on j.company_id = c.id
                group by c.industry
                order by average_salary'''
        cur.execute(query)
        rows = cur.fetchall()
        return rows
    
    except Exception as e:
        print("Error while calculating avg salary by industry")
        print(e)


    finally:

        if cur:
            cur.close()
        if conn:
            conn.close()



def job_postings_with_no_applications():

    conn = None
    cur = None

    try:
        conn = get_connection()
        cur = conn.cursor()
        query = '''select j.id, j.title, c.company_name from jobs as j
                jOIN companies c ON j.company_id = c.id
                left join applications as a on j.id = a.job_id
                where a.job_id is null'''
        cur.execute(query)
        rows = cur.fetchall()
        return rows
    
    except Exception as e:
        print("Error while getting job postings with no applications")
        print(e)


    finally:

        if cur:
            cur.close()
        if conn:
            conn.close()     



def job_postings_with_most_applications():

    conn = None
    cur = None

    try:
        conn = get_connection()
        cur = conn.cursor()
        query = '''select j.id, j.title, count(*) as no_of_applications from jobs as j
                join companies as c on j.company_id = c.id
                group by j.id, j.title
                order by no_of_applications desc
                limit 1'''
        cur.execute(query)
        rows = cur.fetchall()
        return rows
    
    except Exception as e:
        print("Error while getting job postings with most applications")
        print(e)


    finally:

        if cur:
            cur.close()
        if conn:
            conn.close()   



def get_interview_rate_per_company():

    conn = None
    cur = None

    try:
        conn = get_connection()
        cur = conn.cursor()
        query = '''select *, round((interview_scheduled_count * 100/total_applications), 2) as interview_rate 
                from (
                    select c.id, c.company_name, count(*) as total_applications, 
                    sum(
                        case
                            when a.status ILIKE '%interview%'
                            then 1
                            else 0
                        end
                    ) as interview_scheduled_count 
                    from applications as a
                    join jobs as j on a.job_id = j.id
                    join companies as c on j.company_id = c.id
                    group by c.id, c.company_name
                    ) as company_stats'''
        cur.execute(query)
        rows = cur.fetchall()
        return rows
    
    except Exception as e:
        print("Error while getting interview rate per company")
        print(e)


    finally:

        if cur:
            cur.close()
        if conn:
            conn.close()   



def get_number_of_rejected_applications_per_industry():

    conn = None
    cur = None

    try:
        conn = get_connection()
        cur = conn.cursor()
        query = '''select c.industry, 
                sum(
                    case
                        when a.status ILIKE '%rejected%'
                        then 1
                        else 0
                    end                                   
                ) as no_of_rejections 
                from companies as c
                join jobs as j on c.id = j.company_id
                join applications as a on j.id = a.job_id
                group by c.industry'''
        cur.execute(query)
        rows = cur.fetchall()
        return rows
    
    except Exception as e:
        print("Error while getting interview rate per company")
        print(e)


    finally:

        if cur:
            cur.close()
        if conn:
            conn.close()    



def get_students_with_applications_to_multiple_companies():

    conn = None
    cur = None

    try:
        conn = get_connection()
        cur = conn.cursor()
        query = '''select s.id, s.name, count(distinct c.id) as no_of_different_company from students as s
                join applications as a on s.id = a.student_id
                join jobs as j on a.job_id = j.id
                join companies as c on j.company_id = c.id
                group by s.id, s.name'''
        cur.execute(query)
        rows = cur.fetchall()
        return rows
    
    except Exception as e:
        print("Error while getting interview rate per company")
        print(e)


    finally:

        if cur:
            cur.close()
        if conn:
            conn.close()     



def get_company_with_no_job_listings():

    conn = None
    cur = None

    try:
        conn = get_connection()
        cur = conn.cursor()
        query = '''select c.id, c.company_name from companies as c
                left join jobs as j on c.id = j.company_id
                where j.id is null'''
        cur.execute(query)
        rows = cur.fetchall()
        return rows
    
    except Exception as e:
        print("Error while getting interview rate per company")
        print(e)


    finally:

        if cur:
            cur.close()
        if conn:
            conn.close()  
            



def get_students_with_no_applications():

    conn = None
    cur = None

    try:
        conn = get_connection()
        cur = conn.cursor()
        query = '''select s.id, s.name from students as s
                left join applications as a on s.id = a.student_id
                where a.student_id is null'''
        cur.execute(query)
        rows = cur.fetchall()
        return rows
    
    except Exception as e:
        print("Error while getting interview rate per company")
        print(e)


    finally:

        if cur:
            cur.close()
        if conn:
            conn.close()



def get_students_average_age_per_industry():

    conn = None
    cur = None

    try:
        conn = get_connection()
        cur = conn.cursor()
        query = '''select c.industry, round(avg(s.age), 2) as average_age from students as s
                join applications as a on s.id = a.student_id
                join jobs as j on a.job_id = j.id
                join companies as c on j.company_id = c.id
                group by c.industry'''
        cur.execute(query)
        rows = cur.fetchall()
        return rows
    
    except Exception as e:
        print("Error while getting interview rate per company")
        print(e)


    finally:

        if cur:
            cur.close()
        if conn:
            conn.close()



def get_country_with_highest_applicants():

    conn = None
    cur = None

    try:
        conn = get_connection()
        cur = conn.cursor()
        query = '''select s.country, count(*) as no_of_applicants from students as s
                join applications as a on s.id = a.student_id
                group by country
                order by no_of_applicants desc
                limit 1'''
        cur.execute(query)
        rows = cur.fetchall()
        return rows
    
    except Exception as e:
        print("Error while getting interview rate per company")
        print(e)


    finally:

        if cur:
            cur.close()
        if conn:
            conn.close()



def get_number_of_applications_monthly():

    conn = None
    cur = None

    try:
        conn = get_connection()
        cur = conn.cursor()
        query = '''select mon, yr, count(*) as number_of_applications
                from
                (select *, extract(month from application_date) as mon, extract(year from application_date) as yr from applications) as t
                group by mon,yr'''
        cur.execute(query)
        rows = cur.fetchall()
        return rows
    
    except Exception as e:
        print("Error while getting interview rate per company")
        print(e)


    finally:

        if cur:
            cur.close()
        if conn:
            conn.close()



def get_aged_applications():

    conn = None
    cur = None

    try:
        conn = get_connection()
        cur = conn.cursor()
        query = '''select *
                from
                (select *, (current_date - application_date) as no_of_days from applications) as t
                where status ILIKE 'applied' and no_of_days > 14;'''
        cur.execute(query)
        rows = cur.fetchall()
        return rows
    
    except Exception as e:
        print("Error while getting interview rate per company")
        print(e)


    finally:

        if cur:
            cur.close()
        if conn:
            conn.close()