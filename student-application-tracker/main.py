import queries
import utils
import logger_config
import logging

logging.info("Application started.")

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

        if choice == "6":
            print("Exiting application safely...")
            break

        # =====================================================================
        # 1. STUDENT MANAGEMENT
        # =====================================================================

        elif choice == "1":
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

                try:
                    if choice == "1":
                        rows = queries.get_all_students()
                        if rows:
                            utils.display_data(utils.STUDENT_HEADERS, rows)
                        else:
                            print("No students found")

                    elif choice == "2":
                        name = utils.get_clean_name("Enter the name: ")
                        country = utils.get_corporate_string("Enter the country: ")
                        age = utils.get_clean_integer("Enter the age: ", 18)
                        rows = queries.insert_student(name, country, age)
                        utils.display_data(utils.STUDENT_HEADERS, rows)

                    elif choice == "3":
                        student_id = utils.get_clean_integer("Enter the student id: ", 1, queries.student_exists, "student not found")
                        name = utils.get_clean_name("Enter the name: ")                       
                        country = utils.get_corporate_string("Enter the country: ")
                        age = utils.get_clean_integer("Enter the age: ", 18)
                        rows = queries.update_student(name, country, age, student_id)
                        utils.display_data(utils.STUDENT_HEADERS, rows)

                    elif choice == "4":
                        student_id = utils.get_clean_integer("Enter the student id: ", 1, queries.student_exists, "student not found")
                        rows = queries.delete_student(student_id)
                        utils.display_data(utils.STUDENT_HEADERS, rows)

                    elif choice == "5":
                        name = utils.get_clean_name("Enter the name: ")
                        rows = queries.search_students_by_name(name)
                        if rows:
                            utils.display_data(utils.STUDENT_HEADERS, rows)
                        else:
                            print("No students found")

                    elif choice == "6":
                        country = utils.get_corporate_string("Enter the country: ")
                        rows = queries.search_students_by_country(country)
                        if rows:
                            utils.display_data(utils.STUDENT_HEADERS, rows)
                        else:
                            print("No students found")

                    elif choice == "7":
                        age = utils.get_clean_integer("Enter the age: ", 18)
                        rows = queries.get_students_older_than(age)
                        if rows:
                            utils.display_data(utils.STUDENT_HEADERS, rows)
                        else:
                            print("No students found")

                    elif choice == "8":
                        min_age = utils.get_clean_integer("Enter the min age: ", 18)
                        max_age = utils.get_clean_integer("Enter the max age: ", 18)
                        rows = queries.get_students_between_ages(min_age, max_age)
                        if rows:
                            utils.display_data(utils.STUDENT_HEADERS, rows)
                        else:
                            print("No students found")

                    elif choice == "9":
                        rows = queries.get_students_sorted_by_name()
                        if rows:
                            utils.display_data(utils.STUDENT_HEADERS, rows)
                        else:
                            print("No students found")

                    elif choice == "10":
                        rows = queries.get_students_sorted_by_age_asc()
                        if rows:
                            utils.display_data(utils.STUDENT_HEADERS, rows)
                        else:
                            print("No students found")

                    elif choice == "11":
                        rows = queries.get_students_sorted_by_age_desc()
                        if rows:
                            utils.display_data(utils.STUDENT_HEADERS, rows)
                        else:
                            print("No students found")

                    elif choice == "12":
                        rows = queries.get_students_sorted_by_country_and_age()
                        if rows:
                            utils.display_data(utils.STUDENT_HEADERS, rows)
                        else:
                            print("No students found")

                    elif choice == "13":
                        rows = queries.get_total_students()
                        if rows is not None:
                            utils.display_metric('Total Registered Students', rows)
                        else:
                            print("No students found")

                    elif choice == "14":
                        rows = queries.get_average_student_age()
                        if rows is not None:
                            utils.display_metric('Average Student Age', rows)
                        else:
                            print("No students found")

                    elif choice == "15":
                        rows = queries.get_youngest_student_age()
                        if rows is not None:
                            utils.display_metric('Youngest Candidate Age', rows)
                        else:
                            print("No students found")

                    elif choice == "16":
                        rows = queries.get_oldest_student_age()
                        if rows is not None:
                            utils.display_metric('Oldest Candidate Age', rows)
                        else:
                            print("No students found")

                    elif choice == "17":
                        rows = queries.get_student_count_by_country()
                        if rows:
                            utils.display_data(['Country Origin', 'Total Student Count'], rows)
                        else:
                            print("No students found")

                    elif choice == "18":
                        rows = queries.get_average_student_age_by_country()
                        if rows:
                            utils.display_data(['Country Origin', 'Average Age Metrics'], rows)
                        else:
                            print("No students found")

                    elif choice == "19":
                        break

                    else:
                        print("Enter a valid input")

                except utils.BackSignal:
                    print("\n Form input canceled. Returning to Student Menu...")
                    continue

        # =====================================================================
        # 2. COMPANY MANAGEMENT
        # =====================================================================

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

                try:
                    if choice == "1":
                        rows = queries.get_all_companies()
                        if rows:
                            utils.display_data(utils.COMPANY_HEADERS, rows)
                        else:
                            print("Company not found")

                    elif choice == "2":
                        # FIXED: Repaired variable names to match validation logic below
                        company_name = utils.get_corporate_string("Enter the corporate name: ")
                        country = utils.get_corporate_string("Enter the country: ")
                        industry = utils.get_corporate_string("Enter the industry sector: ")
                        rows = queries.insert_company(company_name, country, industry)
                        utils.display_data(utils.COMPANY_HEADERS, rows)

                    elif choice == "3":
                        company_id = utils.get_clean_integer("Enter the company id: ", 1, queries.company_exists, "company not found")
                        company_name = utils.get_corporate_string("Enter the company name: ")
                        country = utils.get_corporate_string("Enter the country: ")
                        industry = utils.get_corporate_string("Enter the industry: ")
                        rows = queries.update_company(company_name, country, industry, company_id)
                        utils.display_data(utils.COMPANY_HEADERS, rows)

                    elif choice == "4":
                        company_id = utils.get_clean_integer("Enter the company id: ", 1, queries.company_exists, "company not found")
                        rows = queries.delete_company(company_id)
                        utils.display_data(utils.COMPANY_HEADERS, rows)

                    elif choice == "5":
                        company_name = utils.get_corporate_string("Enter the company name: ")
                        rows = queries.search_companies_by_name(company_name)
                        if rows:
                            utils.display_data(utils.COMPANY_HEADERS, rows)
                        else:
                            print("Company not found")

                    elif choice == "6":
                        country = utils.get_corporate_string("Enter the country: ")
                        rows = queries.search_companies_by_country(country)
                        if rows:
                            utils.display_data(utils.COMPANY_HEADERS, rows)
                        else:
                            print("Company not found")

                    elif choice == "7":
                        industry = utils.get_corporate_string("Enter the industry: ")
                        rows = queries.search_companies_by_industry(industry)
                        if rows:
                            utils.display_data(utils.COMPANY_HEADERS, rows)
                        else:
                            print("Company not found")

                    elif choice == "8":
                        rows = queries.get_companies_sorted_by_name()
                        if rows:
                            utils.display_data(utils.COMPANY_HEADERS, rows)
                        else:
                            print("Company not found")

                    elif choice == "9":
                        rows = queries.get_companies_sorted_by_country()
                        if rows:
                            utils.display_data(utils.COMPANY_HEADERS, rows)
                        else:
                            print("Company not found")

                    elif choice == "10":
                        rows = queries.get_total_companies()
                        if rows is not None:
                            utils.display_metric('Total Companies Registered', rows)
                        else:
                            print("No metrics available")

                    elif choice == "11":
                        rows = queries.get_company_count_by_country()
                        if rows:
                            utils.display_data(['Country', 'Company Count'], rows)
                        else:
                            print("No metrics available")

                    elif choice == "12":
                        rows = queries.get_company_count_by_industry()
                        if rows:
                            utils.display_data(['Industry', 'Company Count'], rows)
                        else:
                            print("No metrics available")

                    elif choice == "13":
                        break

                    else:
                        print("Enter a valid input")

                except utils.BackSignal:
                    print("\n Form input canceled. Returning to Company Menu...")
                    continue

        # =====================================================================
        # 3. JOB MANAGEMENT
        # =====================================================================

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

                try:
                    if choice == "1":
                        rows = queries.get_all_jobs()
                        if rows:
                            utils.display_data(utils.JOB_HEADERS, rows)
                        else:
                            print("Job not found")

                    elif choice == "2":
                        rows = queries.get_company_ids_and_names()
                        if rows:
                            utils.display_data(['Company ID', 'Company Name'], rows)
                        
                        company_id = utils.get_clean_integer("Enter the company id: ", 1, queries.company_exists, "company not found")
                        # FIXED: Swapped integer parsing to clean string parsing for job title structures
                        title = utils.get_corporate_string("Enter the job title: ")
                        salary = utils.get_clean_integer("Enter the salary: ", 1)
                        location = utils.get_corporate_string("Enter the location: ")
                        rows = queries.insert_job(title, salary, location, company_id)
                        utils.display_data(utils.JOB_HEADERS, rows)

                    elif choice == "3":
                        job_id = utils.get_clean_integer("Enter the job_id: ", 1, queries.job_exists, "job not found")
                        company_id = utils.get_clean_integer("Enter the company id: ", 1, queries.company_exists, "company not found")
                        # FIXED: Converted title entry workflow from int to text
                        title = utils.get_corporate_string("Enter the job title: ")
                        salary = utils.get_clean_integer("Enter the salary: ", 1)
                        location = utils.get_corporate_string("Enter the location: ")
                        rows = queries.update_job(title, salary, location, company_id, job_id)
                        utils.display_data(utils.JOB_HEADERS, rows)

                    elif choice == "4":
                        job_id = utils.get_clean_integer("Enter the job_id: ", 1, queries.job_exists, "job not found")
                        rows = queries.delete_job(job_id)
                        utils.display_data(utils.JOB_HEADERS, rows)

                    elif choice == "5":
                        # FIXED: Converted search parameter query pattern to match textual title fields
                        title = utils.get_corporate_string("Enter the title search sequence: ")
                        rows = queries.search_jobs_by_title(title)
                        if rows:
                            utils.display_data(utils.JOB_HEADERS, rows)
                        else:
                            print("Job not found")

                    elif choice == "6":
                        location = utils.get_corporate_string("Enter the location: ")
                        rows = queries.search_jobs_by_location(location)
                        if rows:
                            utils.display_data(utils.JOB_HEADERS, rows)
                        else:
                            print("Job not found")

                    elif choice == "7":
                        salary = utils.get_clean_integer("Enter the salary: ", 1)
                        rows = queries.get_jobs_with_salary_above(salary)
                        if rows:
                            utils.display_data(utils.JOB_HEADERS, rows)
                        else:
                            print("Job not found")

                    elif choice == "8":
                        min_salary = utils.get_clean_integer("Enter the minimum salary boundary: ", 1)
                        max_salary = utils.get_clean_integer("Enter the maximum salary boundary: ", 1)
                        rows = queries.get_jobs_between_salaries(min_salary, max_salary)
                        if rows:
                            utils.display_data(utils.JOB_HEADERS, rows)
                        else:
                            print("Job not found")

                    elif choice == "9":
                        rows = queries.get_jobs_sorted_by_salary_asc()
                        if rows:
                            utils.display_data(utils.JOB_HEADERS, rows)
                        else:
                            print("Job not found")

                    elif choice == "10":
                        rows = queries.get_jobs_sorted_by_salary_desc()
                        if rows:
                            utils.display_data(utils.JOB_HEADERS, rows)
                        else:
                            print("Job not found")

                    elif choice == "11":
                        rows = queries.get_jobs_sorted_by_title()
                        if rows:
                            utils.display_data(utils.JOB_HEADERS, rows)
                        else:
                            print("Job not found")

                    elif choice == "12":
                        rows = queries.get_total_jobs()
                        if rows is not None:
                            utils.display_metric('Total Active Jobs Available', rows)
                        else:
                            print("No metrics available")

                    elif choice == "13":
                        rows = queries.get_average_job_salary()
                        if rows is not None:
                            utils.display_metric('Average Offered Salary', rows)
                        else:
                            print("No metrics available")

                    elif choice == "14":
                        rows = queries.get_highest_paying_job()
                        if rows:
                            utils.display_data(utils.JOB_HEADERS, rows)
                        else:
                            print("Job not found")

                    elif choice == "15":
                        rows = queries.get_lowest_paying_job()
                        if rows:
                            utils.display_data(utils.JOB_HEADERS, rows)
                        else:
                            print("Job not found")

                    elif choice == "16":
                        break

                    else:
                        print("Enter a valid input")

                except utils.BackSignal:
                    print("\n Form input canceled. Returning to Job Menu...")
                    continue

        # =====================================================================
        # 4. APPLICATION MANAGEMENT
        # =====================================================================

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

                try:
                    if choice == "1":
                        rows = queries.get_all_applications()
                        if rows:
                            utils.display_data(utils.APPLICATION_HEADERS, rows)
                        else:
                            print("Application not found")

                    elif choice == "2":
                        rows = queries.get_student_ids_and_names()
                        utils.display_data(["Student ID", "Student Name"], rows)
                        
                        # FIXED: Removed redundant inner while-loop layer structures
                        student_id = utils.get_clean_integer("Enter the student id: ", 1, queries.student_exists, "student not found")

                        rows = queries.get_job_ids_and_names()
                        utils.display_data(["Job ID", "Job Title"], rows)

                        job_id = utils.get_clean_integer("Enter the job_id: ", 1, queries.job_exists, "job not found")

                        application_date = utils.get_clean_date("Enter the date: ")
                        status = utils.get_application_status("Enter the status: ")
                        rows = queries.insert_application(student_id, job_id, application_date, status)
                        utils.display_data(utils.APPLICATION_HEADERS, rows)

                    elif choice == "3":
                        # FIXED: Extracted variable out from structural nested execution loops
                        application_id = utils.get_clean_integer("Enter application id: ", 1, queries.application_exists, "Application not found")
                        application_date = utils.get_clean_date("Enter the date: ")
                        status = utils.get_application_status("Enter the status: ")
                        rows = queries.update_application(application_date, status, application_id)
                        utils.display_data(utils.APPLICATION_HEADERS, rows)

                    elif choice == "4":
                        # FIXED: Linear sequence parsing implementation applied safely
                        application_id = utils.get_clean_integer("Enter application id: ", 1, queries.application_exists, "Application not found")
                        rows = queries.delete_application(application_id)
                        utils.display_data(utils.APPLICATION_HEADERS, rows)

                    elif choice == "5":
                        # yes yes, ik we used get_calen_name for status so we have flexibility in search.
                        status = utils.get_clean_name("Enter the status: ")
                        rows = queries.search_applications_by_status(status)
                        if rows:
                            utils.display_data(utils.APPLICATION_HEADERS, rows)
                        else:
                            print("Application not found")

                    elif choice == "6":
                        student_id = utils.get_clean_integer("Enter the student id: ", 1, queries.student_exists, "student not found")
                        rows = queries.search_applications_by_student_id(student_id)
                        if rows:
                            utils.display_data(utils.APPLICATION_HEADERS, rows)
                        else:
                            print("Application not found")

                    elif choice == "7":
                        job_id = utils.get_clean_integer("Enter the job_id: ", 1, queries.job_exists, "job not found")
                        rows = queries.search_applications_by_job_id(job_id)
                        if rows:
                            utils.display_data(utils.APPLICATION_HEADERS, rows)
                        else:
                            print("Application not found")

                    elif choice == "8":
                        rows = queries.get_applications_sorted_by_date()
                        utils.display_data(utils.APPLICATION_HEADERS, rows)

                    elif choice == "9":
                        rows = queries.get_applications_sorted_by_status()
                        utils.display_data(utils.APPLICATION_HEADERS, rows)

                    elif choice == "10":
                        rows = queries.get_total_applications()
                        if rows is not None:
                            utils.display_metric('Total System Applications', rows)
                        else:
                            print("No metrics available")

                    elif choice == "11":
                        rows = queries.get_application_count_by_status()
                        if rows:
                            utils.display_data(['Application Status', 'Total Application Count'], rows)
                        else:
                            print("Application not found")

                    elif choice == "12":
                        break

                    else:
                        print("Enter a valid input")

                except utils.BackSignal:
                    print("\n Form input canceled. Returning to Application Menu...")
                    continue

        # =====================================================================
        # 5. RELATIONAL QUERIES & REPORTS
        # =====================================================================

        elif choice == "5":
            while True:
                choice = input('''
                ============================================================
                📊 RELATIONAL ANALYTICS & REPORTING ENGINE
                ============================================================

                ---------- STUDENT APPLICATION INSIGHTS ----------

                1. View Complete Student Application History (Full Context)
                2. Filter Applicant Profiles by Company Name
                3. Identify High-Volume Candidates (Multiple Applications)

                ---------- COMPANY ANALYTICS ----------

                4. View Total Job Openings Per Company
                5. View Total Applications Received Per Company
                6. View Top Company by Total Applications Received
                7. View Highest Paying Corporate Profile (By Average Salary)
                8. View International Student Applications (Cross-Border Talent)

                ---------- JOB MARKET INSIGHTS ----------

                9. View Master Job Postings Registry (With Company Details)
                10. View Top 5 Highest Paying Job Postings
                11. View Average Salary Metrics Per Industry
                12. View Stagnant Positions (Jobs with Zero Applications)
                13. View Top 10 Most Competitive Job Positions

                ---------- ADVANCED BUSINESS INSIGHTS ----------

                14. View Interview Conversion Rate Per Company
                15. View Rejected Applications Per Industry Segment
                16. Identify Application Diversification (Applying to Multiple Companies)
                17. View Inactive Corporate Accounts (Companies with No Jobs)
                18. View Unengaged Talent Pool (Students with No Applications)
                19. View Average Applicant Age Per Industry Sector
                20. View Top Applicant Country (Highest Applicant Volume)

                ---------- TEMPORAL & DATE ANALYTICS ----------

                21. View Monthly Application Volume Trends
                22. View Operational SLA Breaches (Applications Pending > 14 Days)

                ---------- SYSTEM ----------

                23. ↩️ Back to Main Menu

                Enter your choice (1-23): ''')
                
                try:
                    if choice == "1":
                        rows = queries.get_students_application_job_and_company()
                        if rows:
                            utils.display_data(['Student Name', 'Job Title', 'Company Name', 'Application Status'], rows)
                        else:
                            print("No records found")

                    elif choice == "2":
                        company_name = utils.get_corporate_string("Enter the company name: ")
                        rows = queries.search_students_applied_to_company(company_name)
                        if rows:
                            utils.display_data(['Student Name'], rows)
                        else:
                            print("No records found")

                    elif choice == "3":
                        rows = queries.get_students_with_multiple_applications()
                        if rows:
                            utils.display_data(['Student ID', 'Student Name', 'Total Applications Submitted'], rows)
                        else:
                            print("No records found")

                    elif choice == "4":
                        rows = queries.get_job_openings_per_company()
                        if rows:
                            utils.display_data(['Company ID', 'Company Name', 'Active Job Openings'], rows)
                        else:
                            print("No records found")

                    elif choice == "5":
                        rows = queries.get_application_count_per_company()
                        if rows:
                            utils.display_data(['Company ID', 'Company Name', 'Total Applications Received'], rows)
                        else:
                            print("No records found")

                    elif choice == "6":
                        rows = queries.get_company_with_highest_applications()
                        if rows:
                            utils.display_data(['Company ID', 'Company Name', 'Total Applications Received'], rows)
                        else:
                            print("No records found")

                    elif choice == "7":
                        rows = queries.get_company_with_highest_average_salary()
                        if rows:
                            utils.display_data(['Company ID', 'Company Name', 'Average Annual Salary'], rows)
                        else:
                            print("No records found")

                    elif choice == "8":
                        rows = queries.get_company_open_to_international_students()
                        if rows:
                            utils.display_data(['Student Name', 'Student Country', 'Company Name', 'Company Country', 'Application Status'], rows)
                        else:
                            print("No records found")

                    elif choice == "9":
                        rows = queries.get_all_jobs_info()
                        if rows:
                            utils.display_data(['Job ID', 'Job Title', 'Company Name', 'Company Country', 'Offered Salary'], rows)
                        else:
                            print("No records found")

                    elif choice == "10":
                        rows = queries.get_highest_5_paying_jobs()
                        if rows:
                            utils.display_data(['Job ID', 'Job Title', 'Company Name', 'Company Country', 'Premium Salary'], rows)
                        else:
                            print("No records found")

                    elif choice == "11":
                        rows = queries.get_average_salary_by_industry()
                        if rows:
                            utils.display_data(['Industry Sector', 'Average Salary Metrics'], rows)
                        else:
                            print("No records found")

                    elif choice == "12":
                        rows = queries.get_job_postings_with_no_applications()
                        if rows:
                            utils.display_data(['Job ID', 'Job Title', 'Company Name'], rows)
                        else:
                            print("No records found")

                    elif choice == "13":
                        rows = queries.get_job_postings_with_most_applications()
                        if rows:
                            utils.display_data(['Job ID', 'Job Title', 'Total Applications Gathered'], rows)
                        else:
                            print("No records found")

                    elif choice == "14":
                        rows = queries.get_interview_rate_per_company()
                        if rows:
                            utils.display_data(['Company ID', 'Company Name', 'Total Applications', 'Interviews Scheduled', 'Interview Scheduled Rate (%)'], rows)
                        else:
                            print("No records found")

                    elif choice == "15":
                        rows = queries.get_number_of_rejected_applications_per_industry()
                        if rows:
                            utils.display_data(['Industry Sector', 'Total Rejection Count'], rows)
                        else:
                            print("No records found")

                    elif choice == "16":
                        rows = queries.get_students_with_applications_to_multiple_companies()
                        if rows:
                            utils.display_data(['Student ID', 'Student Name', 'Total Companies Applied To'], rows)
                        else:
                            print("No records found")

                    elif choice == "17":
                        rows = queries.get_company_with_no_job_listings()
                        if rows:
                            utils.display_data(['Company ID', 'Company Name'], rows)
                        else:
                            print("No records found")

                    elif choice == "18":
                        rows = queries.get_students_with_no_applications()
                        if rows:
                            utils.display_data(['Student ID', 'Student Name'], rows)
                        else:
                            print("No records found")

                    elif choice == "19":
                        rows = queries.get_students_average_age_per_industry()
                        if rows:
                            utils.display_data(['Industry Sector', 'Average Applicant Age'], rows)
                        else:
                            print("No records found")

                    elif choice == "20":
                        rows = queries.get_country_with_highest_applicants()
                        if rows:
                            utils.display_data(['Demographic Country', 'Total Applicant Volume'], rows)
                        else:
                            print("No records found")

                    elif choice == "21":
                        rows = queries.get_number_of_applications_monthly()
                        if rows:
                            utils.display_data(['Month', 'Year', 'Monthly Applications Count'], rows)
                        else:
                            print("No records found")

                    elif choice == "22":
                        rows = queries.get_aged_applications()
                        if rows:
                            utils.display_data(['Application ID', 'Student ID', 'Job ID', 'Application Date', 'Status', 'Days In Queue'], rows)
                        else:
                            print("No records found")

                    elif choice == "23":
                        break

                    else:
                        print("Enter a valid input")

                except utils.BackSignal:
                    print("\n Form input canceled. Returning to Report Menu...")
                    continue
                    
        else:
            print("Enter a valid menu option allocation (1-6).")

    except Exception as e:
        print(f"System Error Shield Activated: {e}")