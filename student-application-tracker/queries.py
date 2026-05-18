# ========================================================================================
# ARCHITECTURAL EVOLUTION OF DATA ACCESS LAYERS
# ========================================================================================
#
# PERSISTED ARCHITECTURE PHASE TIMELINE:
#
# ─── PHASE 1: DIRECT MONOLITHIC QUERIES (Historical Legacy) ─────────────────────────────
#  • Implementation: Every function manually opened its own connection, built a 
#    dedicated cursor, executed raw SQL, committed, and managed its own close/cleanup.
#  • Discoveries & Flaws: Massive boilerplate repetition across 30+ functions. 
#    High risk of leaked connections, unhandled rollbacks, and fragile maintenance.
#
# ─── PHASE 2: ISOLATED ABSTRACT EXECUTION ENGINE (Current Production Grid) ──────────────
#  • Implementation: Consolidates connection lifecycles, statement preparation, and 
#    error boundaries into a singular, trusted execution channel (`_execute_query_secure`).
#  • Breakthroughs: Enforces strict connection teardowns via try/except/finally blocks,
#    natively implements atomic transaction rollbacks, and eliminates redundant code.
#    Decouples raw query transport from computational formatting wrappers.
# ========================================================================================

import psycopg2 
from db_connect import get_connection
from utils import format_numeric_result, validate_schema_structure, get_table_display_column


# ========================================================================================
# GENERATION 2 — ABSTRACT DATABASE EXECUTION ENGINE (MASTER TRANSPORT)
# Core Infrastructure Layer: Responsible for connection state preservation, transaction
# integrity, safe cursor extraction, and structural exception containment.
# ========================================================================================


def _execute_query_secure(query, params = None, fetch="fetchall"):
    """
    Core Database Engine. Centralizes connection lifecycle, transactions, and error boundaries.
    Defaults to 'fetchall' data retrieval for optimal performance across read-heavy workflows.
    """
    conn = None
    cur = None

    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(query, params)
        conn.commit()

        if fetch:
            rows = getattr(cur, fetch)()
            return rows
        
        return None
    
    except psycopg2.Error as e:
        if conn:
            conn.rollback()
        print(f"Error while executing query: {e}")
        return None if fetch == "fetchone" else []  
      
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()



# =====================================================================
# SYSTEM GENERIC PERSISTENCE WORKFLOWS
# Core utilities for dynamic table reads, global entity verifications, 
# and master row-count checks across any database table.
# =====================================================================

def _get_all_records(table_name):

    query = f"select * from {table_name} order by id"
    return _execute_query_secure(query)


def _check_entity_exists(table_name, id):
    
        query = f"select 1 from {table_name} where id = %s"
        params = (id,)
        result =  _execute_query_secure(query, params, fetch = "fetchone")
        return result is not None


def _search_entity_by_feature(table_name, feature_column, feature_value, exact_match=True):

    if not feature_value:
        return []
    
    if exact_match:
        query = f"select * from {table_name} where {feature_column} = %s order by id"
        params = (feature_value,)

    else:
        query = f"select * from {table_name} where {feature_column} ILIKE %s order by id"
        params = (f"%{feature_value}%",)

    
    result = _execute_query_secure(query, params)
    return result if result else []


def _get_entity_sorted_by_feature(table_name, feature_column, ascending=True):
    
    direction = "ASC" if ascending else "DESC"
    query = f"select * from {table_name} order by {feature_column} {direction}"
    result = _execute_query_secure(query)
    return result if result else []


def _get_entity_by_comparison(table_name, feature_column, operator, threshold_value):

    query = f"select * from {table_name} where {feature_column} {operator} %s order by {feature_column}"
    params = (threshold_value,)
    result = _execute_query_secure(query, params)
    return result if result else []


def _get_entity_by_range(table_name, feature_column, min_number, max_number):
    
    query = f"select * from {table_name} where {feature_column} between %s and %s order by {feature_column}"
    params = (min_number, max_number)
    result = _execute_query_secure(query, params)
    return result if result else []


def _get_entity_scalar_aggregate(table_name, aggregate_function, aggregate_column):
    
    query = f"select {aggregate_function}({aggregate_column}) from {table_name}"
    result = _execute_query_secure(query, fetch = "fetchone")
    if result and result[0] is not None:

        raw_value = result[0]
        clean_value = format_numeric_result([raw_value])[0]
        return clean_value
        
    return 0
    

def _get_entity_aggregate_breakdown(table_name, aggregate_function, column_name, grouped_column):
    
    query = f"select {grouped_column}, {aggregate_function}({column_name}) from {table_name} group by {grouped_column}"
    result = _execute_query_secure(query)
    if not result:
        return []
        
    group_names = [row[0] for row in result]
    raw_numbers = [row[1] for row in result]
    
    clean_numbers = format_numeric_result(raw_numbers)
    
    # Zip the group names and cleaned numbers back together into a beautiful dictionary
    # Example: zip(['HR', 'IT'], [25, 30]) -> {'HR': 25, 'IT': 30}
    return [[group, num] for group, num in zip(group_names, clean_numbers)]


def delete_record_by_id(table_name, id):

    query = f"delete from {table_name} where id = %s returning *"
    params = (id, )
    result = _execute_query_secure(query, params)
    return result if result else []

#practise
def get_extreme_records_matrix(table_name, target_column, order_direction="DESC", limit_count=1):
    """
    Pure abstract executor to pull Top-N whole rows dynamically.
    """
    # 1. Run the imported check from utils
    validate_schema_structure(table_name, target_column)
    
    # 2. Sanitize options
    clean_direction = "ASC" if order_direction.upper() == "ASC" else "DESC"
    try:
        limit_count = max(1, int(limit_count))
    except (ValueError, TypeError):
        limit_count = 1

    # 3. Build and execute query
    query = f"""
        SELECT * FROM {table_name} 
        ORDER BY {target_column} {clean_direction} 
        LIMIT %s
    """
    
    result = _execute_query_secure(query, params=(limit_count,), fetch="fetchall")
    return [list(row) for row in result] if result else []

#practise
def get_table_lookup_list(table_name):
    """
    Pure abstract lookup executor. Automatically detects descriptive columns 
    and returns a clean list of (id, display_name) for UI dropdown components.
    """
    # 1. Validate the table and fetch its specific display column name
    display_column = get_table_display_column(table_name)
    
    # 2. Construct the query using the verified safe structural values
    # It dynamically becomes: SELECT id, title FROM jobs ORDER BY title ASC
    query = f"SELECT id, {display_column} FROM {table_name} ORDER BY {display_column} ASC"
    
    # 3. Route to the secure engine (No dynamic parameters needed here since structure is whitelisted)
    result = _execute_query_secure(query, params=None, fetch="fetchall")
    
    return result if result else []


# =========================
# STUDENT QUERIES
# =========================


def get_all_students():
    return _get_all_records("students")


def insert_student(name, country, age):
    query = '''INSERT INTO students(name, country, age)
            VALUES (%s, %s, %s) returning *'''
    params = (name, country, age)
    result = _execute_query_secure(query, params)
    return result if result else []
        

def update_student(name, country, age, student_id):

    query = '''update students
                set name = %s,
                country = %s,
                age = %s
                where id = %s returning *'''
    params = (name, country, age, student_id)
    result = _execute_query_secure(query, params)
    return result if result else []


def student_exists(student_id):
    return _check_entity_exists("students", student_id)


def delete_student(student_id):
    return delete_record_by_id("students", student_id)


def search_students_by_country(country_name):
    return _search_entity_by_feature("students", "country", country_name, False)


def search_students_by_name(name):
    return _search_entity_by_feature("students", "name", name, False)


def get_students_older_than(age):
    return _get_entity_by_comparison("students", "age", ">", age)
    
    

def get_students_between_ages(min_age,max_age):
    return _get_entity_by_range("students", "age", min_age, max_age)


def get_students_sorted_by_name():
    return _get_entity_sorted_by_feature("students", "name")


def get_students_sorted_by_age_asc():
    return _get_entity_sorted_by_feature("students", "age")


def get_students_sorted_by_age_desc():
    return _get_entity_sorted_by_feature("students", "age", False)


def get_students_sorted_by_country_and_age():
    query = "select * from students order by country, age"
    result = _execute_query_secure(query)
    return result if result else []


def get_total_students():
    return _get_entity_scalar_aggregate("students", "count", "*")


def get_average_student_age():
    return _get_entity_scalar_aggregate("students", "avg", "age")


def get_oldest_student_age():
    return _get_entity_scalar_aggregate("students", "max", "age")



def get_youngest_student_age():
    return _get_entity_scalar_aggregate("students", "min", "age")


def get_student_count_by_country():
    return _get_entity_aggregate_breakdown("students", "count", "*", "country")


def get_average_student_age_by_country():
        return _get_entity_aggregate_breakdown("students", "avg", "age", "country")



# =========================
# COMPANY QUERIES
# =========================


def get_all_companies():
    return _get_all_records()


def insert_company(company_name, country, industry):

    query = '''INSERT INTO companies(company_name, country, industry)
                VALUES (%s, %s, %s) returning *'''
    params = (company_name, country, industry)
    result = _execute_query_secure(query, params)
    return result if result else []


def update_company(company_name, country, industry, company_id):

    query = '''update companies
                set company_name = %s,
                country = %s,
                industry = %s
                where id = %s returning *'''
    params = (company_name, country, industry, company_id)
    result = _execute_query_secure(query, params)
    return result if result else []


def company_exists(company_id):
    return _check_entity_exists("companies", company_id)


def delete_company(company_id):
    return delete_record_by_id("companies", company_id)


def search_companies_by_name(company_name):
    return _search_entity_by_feature("companies", "company_name", company_name, False)
    

def search_companies_by_country(country):
    return _search_entity_by_feature("companies", "country", country, False)


def search_companies_by_industry(industry):
    return _search_entity_by_feature("companies", "industry", industry, False)


def get_companies_sorted_by_name():
    return _get_entity_sorted_by_feature("companies", "company_name")


def get_companies_sorted_by_country():
    return _get_entity_sorted_by_feature("companies", "country")


def get_total_companies():
    return _get_entity_scalar_aggregate("companies", "count", "*")


def get_company_count_by_country():
    return _get_entity_aggregate_breakdown("companies", "count","*", "country" )


def get_company_count_by_industry():
    return _get_entity_aggregate_breakdown("companies", "count","*", "industry")



# =========================
# JOBS QUERIES
# =========================



def get_all_jobs():
    return _get_all_records("jobs")


def insert_job(title, salary, location, company_id):
    
    query = '''INSERT INTO jobs(title, salary, location, company_id)
            VALUES (%s, %s, %s, %s) returning *'''
    params = (title, salary, location, company_id)
    result = _execute_query_secure(query, params)
    return result if result else []


def get_company_ids_and_names():
    return get_table_display_column("companies")


def job_exists(job_id):
    return _check_entity_exists("jobs", job_id)


def update_job(title, salary, location, company_id, job_id):
    query = '''update jobs
            set title = %s,
            salary = %s,
            location = %s,
            company_id = %s
            where id = %s returning *'''
    params = (title, salary, location, company_id, job_id)
    result = _execute_query_secure(query, params)
    return result if result else []


def delete_job(job_id):
    return delete_record_by_id("jobs", job_id)


def search_jobs_by_title(title):
    return _search_entity_by_feature("jobs", "title", title, False)


def search_jobs_by_location(location):
    return _search_entity_by_feature("jobs", "location", location, False)


def get_jobs_with_salary_above(salary):
    return _get_entity_by_comparison("jobs", "salary", ">", salary)


def get_jobs_between_salaries(min_salary,max_salary):
    return _get_entity_by_range("jobs", "salary", min_salary, max_salary)


def get_jobs_sorted_by_salary_asc():
    return _get_entity_sorted_by_feature("jobs","salary")


def get_jobs_sorted_by_salary_desc():
    return _get_entity_sorted_by_feature("jobs","salary", False)


def get_jobs_sorted_by_title():
    return _get_entity_sorted_by_feature("jobs","title")


def get_total_jobs():
    return _get_entity_scalar_aggregate("jobs", "count", "*")


def get_average_job_salary():
    return _get_entity_scalar_aggregate("jobs", "avg", "salary")


def get_highest_paying_job():
    return get_extreme_records_matrix("jobs", "salary")


def get_lowest_paying_job():
        return get_extreme_records_matrix("jobs", "salary", "ASC")



    
# =========================
# Applications QUERIES
# =========================



def get_all_applications():
    return _get_all_records()


def insert_application(student_id, job_id, application_date, status):
    query = '''INSERT INTO applications(student_id, job_id, application_date, status)
            VALUES (%s, %s, %s, %s) returning *'''
    params = (student_id, job_id, application_date, status)
    result = _execute_query_secure(query, params)
    return result if result else []


def get_student_ids_and_names():
    return get_table_display_column("students")


def get_job_ids_and_names():
    return get_table_display_column("jobs")


def update_application(application_date, status, application_id):
    query = '''update applications
                set application_date = %s,
                status = %s
                where id = %s returning *'''
    params = (application_date, status, application_id)
    result = _execute_query_secure(query, params)
    return result if result else []


def application_exists(application_id):
    return _check_entity_exists("applications", application_id)


def delete_application(application_id):
    return delete_record_by_id("applications", application_id)


def search_applications_by_status(status):
    return _search_entity_by_feature("applications", "status", status)


def search_applications_by_student_id(student_id):
    return _search_entity_by_feature("applications", "student_id", student_id)


def search_applications_by_job_id(job_id):
    return _search_entity_by_feature("applications", "job_id", job_id)


def get_applications_sorted_by_date():
    return _get_entity_sorted_by_feature("applications", "application_date")


def get_applications_sorted_by_status():
    return _get_entity_sorted_by_feature("applications", "status")


def get_total_applications():
    return _get_entity_scalar_aggregate("applications", "count", "*")


def get_application_count_by_status():
    return _get_entity_aggregate_breakdown("applications", "count", "*", "status")


# =========================
# Relational QUERIES
# =========================



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
    
    except psycopg2.Error as e:
        print("Error while getting students application job name and company details")
        print(e)
        return []

    finally:

        if cur:
            cur.close()
        if conn:
            conn.close()



def search_students_applied_to_company(company_name):

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
    
    except psycopg2.Error as e:
        print("Error while calculating student applied to a particular company")
        print(e)
        return []

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
    
    except psycopg2.Error as e:
        print("Error while fetching students with multiple applications")
        print(e)
        return []

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
    
    except psycopg2.Error as e:
        print("Error while calculating jobs opening per company")
        print(e)
        return []

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
    
    except psycopg2.Error as e:
        print("Error while calculating applications volume per company")
        print(e)
        return []

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
    
    except psycopg2.Error as e:
        print("Error while calculating company with highest applications")
        print(e)
        return []

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
    
    except psycopg2.Error as e:
        print("Error while calculating company with highest average salary")
        print(e)
        return []

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
    
    except psycopg2.Error as e:
        print("Error while calculating company with international students")
        print(e)
        return []

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
    
    except psycopg2.Error as e:
        print("Error while getting all jobs metadata")
        print(e)
        return []

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
    
    except psycopg2.Error as e:
        print("Error while getting highest 5 paying jobs")
        print(e)
        return []

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
    
    except psycopg2.Error as e:
        print("Error while calculating avg salary by industry")
        print(e)
        return []

    finally:

        if cur:
            cur.close()
        if conn:
            conn.close()



def get_job_postings_with_no_applications():

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
    
    except psycopg2.Error as e:
        print("Error while getting job postings with no applications")
        print(e)
        return []

    finally:

        if cur:
            cur.close()
        if conn:
            conn.close()     



def get_job_postings_with_most_applications():

    conn = None
    cur = None

    try:
        conn = get_connection()
        cur = conn.cursor()
        query = '''select j.id, j.title, count(*) as no_of_applications from jobs as j
                join companies as c on j.company_id = c.id
                LEFT JOIN applications as a ON j.id = a.job_id
                group by j.id, j.title
                order by no_of_applications desc
                limit 10'''
        cur.execute(query)
        rows = cur.fetchall()
        return rows
    
    except psycopg2.Error as e:
        print("Error while getting job postings with most applications")
        print(e)
        return []

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
    
    except psycopg2.Error as e:
        print("Error while getting interview rate per company")
        print(e)
        return []

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
    
    except psycopg2.Error as e:
        print("Error while getting rejections per industry")
        print(e)
        return []

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
    
    except psycopg2.Error as e:
        print("Error while getting students applying to multiple companies")
        print(e)
        return []

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
    
    except psycopg2.Error as e:
        print("Error while getting companies with no job listings")
        print(e)
        return []

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
    
    except psycopg2.Error as e:
        print("Error while getting students with no applications")
        print(e)
        return []

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
    
    except psycopg2.Error as e:
        print("Error while getting average student age per industry")
        print(e)
        return []

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
    
    except psycopg2.Error as e:
        print("Error while getting country with highest applicants")
        print(e)
        return []

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
    
    except psycopg2.Error as e:
        print("Error while getting monthly applications volume")
        print(e)
        return []

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
    
    except psycopg2.Error as e:
        print("Error while getting aged applications details")
        print(e)
        return []

    finally:

        if cur:
            cur.close()
        if conn:
            conn.close()




        
