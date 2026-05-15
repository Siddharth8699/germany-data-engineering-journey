import queries
import utils

while True:
    try:
        choice = input('''
        1. Student Management
        2. Company Management
        3. Job Management
        4. Application Management
        5. Relational Queries & Reports
        6. Exit
        Enter your choice: ''')

        if choice == "1":

            while True:

                choice = input('''
                1. View All Students
                2. Add Student
                3. Update Student
                4. Delete Student

                5. Search Students By Name
                6. Search Students By Country
                7. Students Older Than Age
                8. Students Between Ages

                9. Sort Students By Name
                10. Sort Students By Increasing Age
                11. Sort Students By Decreasing Age
                12. Sort Students By Country Then Age

                13. Total Students
                14. Average Student Age
                15. Youngest Student Age
                16. Oldest Student Age
                17. Students Per Country
                18. Average Age Per Country

                19. Back

                Enter your choice: ''')

                if choice == "1":
                    rows = queries.fetch_students()
                    if rows:
                        utils.display_data(utils.STUDENT_HEADERS, rows)

                    else:
                        print("No students found")

                elif choice == "2":
                    name = utils.get_non_empty_string("Enter the name: ")
                    country = utils.get_non_empty_string("Enter the country: ")
                    age = utils.get_valid_age()
                    rows = queries.insert_student(name,country,age)
                    utils.display_data(utils.STUDENT_HEADERS, rows)

                elif choice == "3":
                    student_id = utils.get_valid_id()

                    if queries.student_exists(student_id):
                        name = utils.get_non_empty_string("Enter the name: ")
                        country = utils.get_non_empty_string("Enter the country: ")
                        age = utils.get_valid_age()

                        rows = queries.update_student(name,country,age,student_id)
                        utils.display_data(utils.STUDENT_HEADERS, rows)

                    else:
                        print("Student not found")

                elif choice == "4":
                    student_id = utils.get_valid_id()

                    if queries.student_exists(student_id):
                        rows = queries.delete_student(student_id)
                        utils.display_data(utils.STUDENT_HEADERS, rows)

                    else:
                        print("Student not found")


                elif choice == "5":
                    name = utils.get_non_empty_string("Enter the name: ")
                    rows = queries.search_students_by_name(name)

                    if rows:
                        utils.display_data(utils.STUDENT_HEADERS, rows)

                    else:
                        print("No students found")


                elif choice == "6":
                    country = utils.get_non_empty_string("Enter the country: ")
                    rows = queries.search_students_by_country(country)

                    if rows:
                        utils.display_data(utils.STUDENT_HEADERS, rows)
                    else:
                        print("No students found")


                elif choice == "7":
                    age = utils.get_valid_age()
                    rows = queries.students_older_than_year_old(age)

                    if rows:
                        utils.display_data(utils.STUDENT_HEADERS, rows)
                    else:
                        print("No students found")


                elif choice == "8":
                    age1 = utils.get_valid_age("Enter the age1: ")
                    age2 = utils.get_valid_age("Enter the age2: ")
                    rows = queries.students_between_age1_and_age2(age1,age2)

                    if rows:
                        utils.display_data(utils.STUDENT_HEADERS, rows)
                    else:
                        print("No students found")


                elif choice == "9":
                    rows = queries.sort_students_by_name()
                    if rows:
                        utils.display_data(utils.STUDENT_HEADERS, rows)
                    else:
                        print("No students found")

                elif choice == "10":
                    rows = queries.sort_students_by_increasing_age()
                    if rows:
                        utils.display_data(utils.STUDENT_HEADERS, rows)
                    else:
                        print("No students found")

                elif choice == "11":
                    rows = queries.sort_students_by_decreasing_age()
                    if rows:
                        utils.display_data(utils.STUDENT_HEADERS, rows)
                    else:
                        print("No students found")

                elif choice == "12":
                    rows = queries.sort_students_by_country_then_age()
                    if rows:
                        utils.display_data(utils.STUDENT_HEADERS, rows)
                    else:
                        print("No students found")


                elif choice == "13":
                    rows = queries.total_students()
                    print(rows)

                elif choice == "14":
                    rows = queries.average_age_students()
                    print(rows)

                elif choice == "15":
                    rows = queries.min_age_students()
                    print(rows)

                elif choice == "16":
                    rows = queries.max_age_students()
                    print(rows)

                elif choice == "17":
                    rows = queries.students_per_country()
                    for row in rows:
                        print(row)

                elif choice == "18":
                    rows = queries.average_age_per_country()
                    for country, average_age in rows:
                        print(f"{country:<20}", f"{average_age:<10}")

                elif choice == "19":
                    break

                else:
                    print("Enter a valid input")

        elif choice == "2":

            while True:

                choice = input('''
                1. View All Companies
                2. Add Company
                3. Update Company
                4. Delete Company

                5. Search Companies By Name
                6. Search Companies By Country
                7. Search Companies By Industry

                8. Sort Companies By Name
                9. Sort Companies By Country

                10. Total Companies
                11. Companies Per Country
                12. Companies Per Industry

                13. Back

                Enter your choice: ''')

                if choice == "1":
                    rows = queries.fetch_companies()
                    if rows:
                        utils.display_data(utils.COMPANY_HEADERS, rows)
                    else:
                        print("Company not found")

                elif choice == "2":
                    company_name = utils.get_non_empty_string("Enter the company name: ")
                    country = utils.get_non_empty_string("Enter the country: ")
                    industry = utils.get_non_empty_string("Enter the industry: ")
                    rows = queries.insert_company(company_name,country,industry)
                    utils.display_data(utils.COMPANY_HEADERS, rows)

                elif choice == "3":
                    company_id = utils.get_valid_id()
                    if queries.company_exists(company_id):
                        company_name = utils.get_non_empty_string("Enter the company name: ")
                        country = utils.get_non_empty_string("Enter the country: ")
                        industry = utils.get_non_empty_string("Enter the industry: ")
                        rows = queries.update_companies(company_name,country,industry,company_id)
                        utils.display_data(utils.COMPANY_HEADERS, rows)

                    else:
                        print("Company not found")

                elif choice == "4":
                    company_id = utils.get_valid_id()
                    if queries.company_exists(company_id):
                        rows = queries.delete_company(company_id)
                        utils.display_data(utils.COMPANY_HEADERS, rows)
                    else:
                        print("Company not found")

                elif choice == "5":
                    company_name = utils.get_non_empty_string("Enter the company name: ")
                    rows = queries.search_companies_by_name(company_name)
                    if rows:
                        utils.display_data(utils.COMPANY_HEADERS, rows)
                    else:
                        print("Company not found")

                elif choice == "6":
                    country = utils.get_non_empty_string("Enter the country: ")
                    rows = queries.search_companies_by_country(country)
                    if rows:
                        utils.display_data(utils.COMPANY_HEADERS, rows)
                    else:
                        print("Company not found")

                elif choice == "7":
                    industry = utils.get_non_empty_string("Enter the industry: ")
                    rows = queries.search_companies_by_industry(industry)
                    if rows:
                        utils.display_data(utils.COMPANY_HEADERS, rows)
                    else:
                        print("Company not found")

                elif choice == "8":
                    rows = queries.sort_companies_by_company_name()
                    if rows:
                        utils.display_data(utils.COMPANY_HEADERS, rows)
                    else:
                        print("Company not found")


                elif choice == "9":
                    rows = queries.sort_companies_by_country()
                    if rows:
                        utils.display_data(utils.COMPANY_HEADERS, rows)
                    else:
                        print("Company not found")

                elif choice == "10":
                    rows = queries.total_companies()
                    print(rows)

                elif choice == "11":
                    rows = queries.companies_per_country()
                    for row in rows:
                        for value in row:
                            print(f"{value:<20}", end=" ")
                        print()

                elif choice == "12":
                    rows = queries.companies_per_industry()
                    for row in rows:
                        for value in row:
                            print(f"{value:<20}", end=" ")
                        print()

                elif choice == "13":
                    break

                else:
                    print("Enter a valid input")



        elif choice == "3":

            while True:

                choice = input('''
                1. View All Jobs
                2. Add Job
                3. Update Job
                4. Delete Job

                5. Search Jobs By Title
                6. Search Jobs By Location
                7. Jobs Above Salary
                8. Jobs Between Salary Range

                9. Sort Jobs By Salary Increasing
                10. Sort Jobs By Salary Decreasing
                11. Sort Jobs By Title

                12. Total Jobs
                13. Average Job Salary
                14. Highest Paying Job
                15. Lowest Paying Job

                16. Back

                Enter your choice: ''')

                if choice == "1":
                    rows = queries.fetch_jobs()
                    if rows:
                        utils.display_data(utils.JOB_HEADERS, rows)
                    else:
                        print("Job not found")

                elif choice == "2":
                    rows = queries.fetch_company_ids_and_names()
                    for row in rows:
                        for value in row:
                            print(f"{value:<20}", end=" ")
                        print()

                    company_id = utils.get_valid_id()

                    if queries.company_exists(company_id):
                        title = utils.get_non_empty_string("Enter the title: ")
                        salary = utils.get_valid_salary()
                        location = utils.get_non_empty_string("Enter the location: ")
                        rows = queries.insert_job(title, salary, location, company_id)
                        utils.display_data(utils.JOB_HEADERS, rows)
                    
                    else:
                        print("Company not found")

                
                elif choice == "3":
                    #fix id and id when running. run again later.
                    job_id = utils.get_valid_id("Enter the job_id: ")
                    if queries.job_exists(job_id):
                        company_id = utils.get_valid_id("Enter the company_id: ")

                        if queries.company_exists(company_id):
                            title = utils.get_non_empty_string("Enter the title: ")
                            salary = utils.get_valid_salary()
                            location = utils.get_non_empty_string("Enter the location: ")
                            rows = queries.update_jobs(title, salary, location, company_id, job_id)
                            utils.display_data(utils.JOB_HEADERS, rows)

                    else:
                        print("Job not found")


                elif choice == "4":
                    job_id = utils.get_valid_id()
                    if queries.job_exists(job_id):
                        rows = queries.delete_job(job_id)
                        utils.display_data(utils.JOB_HEADERS, rows)
                    
                    else:
                        print("Job not found")


                elif choice == "5":
                    title = utils.get_non_empty_string("Enter the title: ")
                    rows = queries.search_jobs_by_title(title)
                    if rows:
                        utils.display_data(utils.JOB_HEADERS, rows)

                    else:
                        print("Job not found")

                    
                elif choice == "6":
                    location = utils.get_non_empty_string("Enter the location: ")
                    rows = queries.search_jobs_by_location(location)
                    if rows:
                        utils.display_data(utils.JOB_HEADERS, rows)

                    else:
                        print("Job not found")


                elif choice == "7":
                    salary = utils.get_valid_salary()
                    rows = queries.jobs_with_salary_above(salary)
                    if rows:
                        utils.display_data(utils.JOB_HEADERS, rows)

                    else:
                        print("Job not found")


                elif choice == "8":
                    salary1 = utils.get_valid_salary("Enter the salary1: ")
                    salary2 = utils.get_valid_salary("Enter the salary2: ")
                    rows = queries.jobs_between_salary1_and_salary2(salary1,salary2)
                    if rows:
                        utils.display_data(utils.JOB_HEADERS, rows)

                    else:
                        print("Job not found")

                
                elif choice == "9":
                    rows = queries.sort_jobs_by_salary_increasing()
                    if rows:
                        utils.display_data(utils.JOB_HEADERS, rows)

                    else:
                        print("Job not found")



                elif choice == "10":
                    rows = queries.sort_jobs_by_salary_decreasing()
                    if rows:
                        utils.display_data(utils.JOB_HEADERS, rows)

                    else:
                        print("Job not found")


                elif choice == "11":
                    rows = queries.sort_jobs_by_title()
                    if rows:
                        utils.display_data(utils.JOB_HEADERS, rows)

                    else:
                        print("Job not found")


                elif choice == "12":
                    rows = queries.total_jobs()
                    print(rows)


                elif choice == "13":
                    rows = queries.average_salary_jobs()
                    print(rows)


                elif choice == "14":
                    rows = queries.highest_paying_job()
                    if rows:
                        utils.display_data(utils.JOB_HEADERS, rows)
                    else:
                        print("Job not found")


                elif choice == "15":
                    rows = queries.lowest_paying_job()
                    if rows:
                        utils.display_data(utils.JOB_HEADERS, rows)
                    else:
                        print("Job not found")

                
                elif choice == "16":
                    break

                else:
                    print("Enter a valid input")



        elif choice == "4":

            while True:

                choice = input('''
                1. View All Applications
                2. Add Application
                3. Update Application Status
                4. Delete Application

                5. Search Applications By Status
                6. Search Applications By Student ID
                7. Search Applications By Job ID

                8. Sort Applications By Date
                9. Sort Applications By Status

                10. Total Applications
                11. Applications Per Status

                12. Back

                Enter your choice: ''')

                if choice == "1":
                    rows = queries.fetch_applications()
                    if rows:
                        utils.display_data(utils.APPLICATION_HEADERS, rows)
                    else:
                        print("Application not found")

                elif choice == "2":
                    rows = queries.fetch_student_ids_and_names()
                    utils.display_data(["ID", "Name"], rows)

                    while True:
                        student_id = utils.get_valid_id("Enter the student id: ")
                        if queries.student_exists(student_id):
                            break

                        print("Student not found")

                    rows = queries.fetch_jobs_ids_and_names()
                    utils.display_data(["ID", "title"], rows)

                    while True:
                        job_id = utils.get_valid_id("Enter the job id: ")
                        if queries.job_exists(job_id):
                            break

                        print("Job not found")

                    application_date = utils.get_valid_date()
                    status = utils.get_non_empty_string("Enter the status: ")
                    rows = queries.insert_applications(student_id, job_id, application_date, status)
                    utils.display_data(utils.APPLICATION_HEADERS, rows)

                elif choice == "3":
                    while True:
                        application_id = utils.get_valid_id("Enter application id: ")
                        if queries.application_exists(application_id):
                            break

                        print("Application not found")

                    application_date = utils.get_valid_date()
                    status =  utils.get_non_empty_string("Enter the status: ")
                    rows = queries.update_applications(application_date, status, application_id)
                    utils.display_data(utils.APPLICATION_HEADERS, rows)

                elif choice == "4":
                    while True:
                        application_id = utils.get_valid_id("Enter application id: ")
                        if queries.application_exists(application_id):
                            break

                        print("Application not found")

                    rows = queries.delete_application(application_id)
                    utils.display_data(utils.APPLICATION_HEADERS, rows)


                elif choice == "5":
                    status = utils.get_non_empty_string("Enter the status: ")
                    rows = queries.search_applications_by_status(status)
                    if rows:
                        utils.display_data(utils.APPLICATION_HEADERS, rows)

                    else:
                        print("Application not found")


                elif choice == "6":
                    student_id = utils.get_valid_id("Enter the student id: ")
                    if queries.student_exists(student_id):
                        rows = queries.search_applications_by_student_id(student_id)
                        if rows:
                            utils.display_data(utils.APPLICATION_HEADERS, rows)

                        else:
                            print("Application not found")


                elif choice == "7":
                    job_id = utils.get_valid_id("Enter the job id: ")
                    if queries.job_exists(job_id):
                        rows = queries.search_applications_by_job_id(job_id)
                        if rows:
                            utils.display_data(utils.APPLICATION_HEADERS, rows)

                        else:
                            print("Application not found")


                elif choice == "8":
                    rows = queries.sort_applications_by_date()
                    utils.display_data(utils.APPLICATION_HEADERS, rows)


                elif choice == "9":
                    rows = queries.sort_applications_by_status()
                    utils.display_data(utils.APPLICATION_HEADERS, rows)

                elif choice == "10":
                    rows = queries.total_applications()
                    print(rows)


                elif choice == "11":
                    rows = queries.applications_by_status()
                    if rows:
                        utils.display_data(['Status','number_of_applications'], rows)

                    else:
                        print("Application not found")

                    
                elif choice == "12":
                    break


                else:
                    print("Enter a valid input")




        elif choice == "5":

            while True:

                choice = input('''
                        ============== RELATIONAL QUERIES & REPORTS ==============

                        ---------- STUDENT APPLICATION INSIGHTS ----------

                        1. View Students And Applied Jobs
                        2. View Students With Company Names
                        3. View Student Applications With Status
                        4. View Students Applied To Specific Company
                        5. View Students Applied To Multiple Jobs

                        ---------- COMPANY ANALYTICS ----------

                        6. View Jobs Per Company
                        7. View Applications Per Company
                        8. Company With Most Applications
                        9. Company Offering Highest Average Salary
                        10. Companies Hiring In Germany

                        ---------- JOB ANALYTICS ----------

                        11. View Jobs With Company Names
                        12. Highest Paying Jobs With Companies
                        13. Average Salary Per Company
                        14. Jobs With No Applications
                        15. Most Applied Jobs

                        ---------- APPLICATION ANALYTICS ----------

                        16. Applications Per Status
                        17. Students With Interview Scheduled
                        18. Rejected Applications Per Company
                        19. Application Count Per Student
                        20. Recent Applications

                        ---------- ADVANCED RELATIONAL QUERIES ----------

                        21. Students Who Applied To Multiple Companies
                        22. Companies Without Jobs
                        23. Students Without Applications
                        24. Average Applicant Age Per Company
                        25. Country With Most Applicants

                        26. Back

                        Enter your choice: ''')
                
                

        elif choice == "6":
            break

        else:
            print("Enter a valid input: ")


    except Exception as e:
        print("Something went wrong")
        print(e)


