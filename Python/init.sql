-- ====================================================================
-- DATABASE MASTER SETUP SCRIPT (COMPLETE PRODUCTION SUITE)
-- Project: Student Application Tracking & Analytics Engine
-- Phase: 2 Master Ledger (Schema, Seed Matrix, & 22 Analytical Reports)
-- ====================================================================

-- --------------------------------------------------------------------
-- STEP 1: DESTRUCTIVE CLEANUP (Ensures safe, idempotent resets)
-- --------------------------------------------------------------------
DROP TABLE IF EXISTS applications CASCADE;
DROP TABLE IF EXISTS jobs CASCADE;
DROP TABLE IF EXISTS students CASCADE;
DROP TABLE IF EXISTS companies CASCADE;

-- --------------------------------------------------------------------
-- STEP 2: SCHEMA DEFINITIONS (DDL Core Architecture)
-- --------------------------------------------------------------------
CREATE TABLE companies (
    id SERIAL PRIMARY KEY,
    company_name VARCHAR(100) NOT NULL,
    country VARCHAR(50) NOT NULL,
    industry VARCHAR(100) NOT NULL
);

CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    country VARCHAR(50) NOT NULL,
    age INT NOT NULL
);

CREATE TABLE jobs (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    salary INT NOT NULL,
    location VARCHAR(50) NOT NULL,
    company_id INT REFERENCES companies(id) ON DELETE CASCADE
);

CREATE TABLE applications (
    id SERIAL PRIMARY KEY,
    student_id INT REFERENCES students(id) ON DELETE CASCADE,
    job_id INT REFERENCES jobs(id) ON DELETE CASCADE,
    application_date DATE DEFAULT CURRENT_DATE,
    status VARCHAR(50) DEFAULT 'Applied'
);

-- --------------------------------------------------------------------
-- STEP 3: MOCK DATASET INGESTION (Targeted Seed Records Matrix)
-- --------------------------------------------------------------------

-- 1. Insert Corporate Entities (Includes targets for macroeconomic industry metrics)
INSERT INTO companies (company_name, country, industry) VALUES 
('Google', 'USA', 'Technology'),                     -- ID 1
('BMW Group', 'Germany', 'Automotive'),               -- ID 2
('SAP', 'Germany', 'Software'),                       -- ID 3
('Siemens', 'Germany', 'Engineering'),                 -- ID 4
('Ghost Finance Group', 'UK', 'Finance');             -- ID 5 (Target for 'Dead Corporate Profiles')

-- 2. Insert Student Profiles (Includes demographic spreads and unengaged nodes)
INSERT INTO students (name, country, age) VALUES 
('Lukas Müller', 'Germany', 23),                      -- ID 1 (High-activity applicant)
('Amit Sharma', 'India', 25),                         -- ID 2 (International applicant)
('Sophia Dubois', 'France', 22),                      -- ID 3 (International applicant)
('John Doe', 'USA', 21),                              -- ID 4 (Domestic applicant)
('Elena Rostova', 'Russia', 24),                      -- ID 5 (Target for 'Aging Applications')
('Anna Schmidt', 'Germany', 19);                      -- ID 6 (Target for 'Unengaged Talent Pool')

-- 3. Insert Job Openings (Includes high-tier wage entries and orphan roles)
INSERT INTO jobs (title, salary, location, company_id) VALUES 
('Junior Data Engineer', 65000, 'Munich', 2),         -- ID 1
('Cloud Architect Intern', 55000, 'Walldorf', 3),     -- ID 2 (Target for 'Stale Listings' - 0 Apps)
('Backend Developer', 95000, 'New York', 1),          -- ID 3 (Highly competitive target)
('AI Research Scientist', 160000, 'Zürich', 1),       -- ID 4 (Premium tier compensation)
('Full Stack Engineer', 85000, 'Berlin', 3),          -- ID 5
('DevOps Specialist', 78000, 'Stuttgart', 4),         -- ID 6
('Data Scientist', 110000, 'San Francisco', 1);       -- ID 7

-- 4. Insert Application Lifecycles (Chronologically tiered with realistic statuses)
INSERT INTO applications (student_id, job_id, application_date, status) VALUES 
-- January Split Window
(1, 1, '2026-01-15', 'Rejected'),                    
(2, 3, '2026-01-20', 'Accepted'),                    

-- February Split Window
(3, 3, '2026-02-10', 'Interview Scheduled'),          
(4, 3, '2026-02-14', 'Interviewing'),                 

-- March Split Window
(1, 5, '2026-03-05', 'Applied'),                     

-- Trailing Unresolved Pipeline (Older than 14 days)
(5, 6, CURRENT_DATE - INTERVAL '25 days', 'Applied'), 

-- Active Real-Time Pipeline Nodes
(1, 6, CURRENT_DATE - INTERVAL '1 day', 'Applied'),   
(2, 1, CURRENT_DATE - INTERVAL '2 days', 'Applied');  

-- --------------------------------------------------------------------
-- STEP 4: PRODUCTION ANALYTICAL SUITE (The 22 Relational Queries)
-- --------------------------------------------------------------------

-- 1. View Student Application Lifecycles (Name, Job, Company, Status)
select s.name, j.title, c.company_name, a.status from students as s
join applications as a on s.id = a.student_id
join jobs as j on a.job_id = j.id
join companies as c on j.company_id = c.id;

-- 2. Filter Applications by Target Company Name
select s.id, s.name, j.title, c.company_name from students as s
join applications as a on s.id = a.student_id
join jobs as j on a.job_id = j.id
join companies as c on j.company_id = c.id
where c.company_name ILIKE 'Google';

-- 3. High-Activity Applicants (Students with > 2 Applications)
select s.id, s.name, count(*) as no_of_applications from students as s
join applications as a on s.id = a.student_id
group by s.id, s.name
having count(*) > 2
order by s.id;

-- 4. Job Board Footprint (Total Jobs & Openings Per Company)
select c.id, c.company_name, count(*) as job_openings from jobs as j
join companies as c on j.company_id = c.id
group by c.id, c.company_name;

-- 5. Application Volume Market Share Per Company
select c.id, c.company_name, count(*) as no_of_applications from applications as a
join jobs as j on a.job_id = j.id
join companies as c on j.company_id = c.id
group by c.id, c.company_name;

-- 6. Core Leaderboard (Company with Most Applications)
select c.id, c.company_name, count(*) as no_of_applications from applications as a
join jobs as j on a.job_id = j.id
join companies as c on j.company_id = c.id
group by c.id, c.company_name
order by count(*) desc
limit 1;

-- 7. Compensation Leader (Company Offering Highest Average Salary)
select c.id, c.company_name, round(avg(j.salary), 2) as average_salary from jobs as j
join companies as c on j.company_id = c.id
group by c.id, c.company_name
order by average_salary desc
limit 1;

-- 8. Cross-Border Talent (Companies Hiring International Students)
select s.name as student_name, s.country as student_country, c.company_name, c.country as company_country, a.status from students as s
join applications as a on s.id = a.student_id
join jobs as j on a.job_id = j.id
join companies as c on j.company_id = c.id
where s.country <> c.country
order by s.name;

-- 9. Complete Job Postings Registry with Corporate Parent Names
select j.id, j.title, c.company_name, c.country, j.salary from jobs as j
join companies as c on j.company_id = c.id
order by j.id;

-- 10. Premium Roles (Top 5 Highest Paying Jobs & Their Companies)
select j.id, j.title, c.company_name, c.country, j.salary from jobs as j
join companies as c on j.company_id = c.id
order by j.salary desc
limit 5;

-- 11. Market Wage Benchmark by Industry (Average Offered Salary Per Industry)
select c.industry, round(avg(j.salary), 2) as average_salary from jobs as j
join companies as c on j.company_id = c.id
group by c.industry
order by average_salary desc;

-- 12. Stale Listings (Active Job Postings with Zero Applications)
select j.id, j.title, c.company_name from jobs as j
join companies as c on j.company_id = c.id
left join applications as a on j.id = a.job_id
where a.job_id is null;

-- 13. Highly Competitive Positions (Jobs with Most Applications)
select j.id, j.title, count(a.id) as no_of_applications from jobs as j
join companies as c on j.company_id = c.id
join applications as a on j.id = a.job_id
group by j.id, j.title
order by no_of_applications desc
limit 1;

-- 14. Strategic Funnel Insight (Interview Conversion Rate Per Corporate Entity)
select *, round((interview_scheduled_count * 100.0 / total_applications), 2) as interview_rate
from
(select c.id, c.company_name, count(*) as total_applications, sum(case when a.status ILIKE '%interview%' then 1 else 0 end) as interview_scheduled_count from applications as a
join jobs as j on a.job_id = j.id
join companies as c on j.company_id = c.id
group by c.id, c.company_name) as company_stats;

-- 15. Industry Churn Analysis (Total Rejections Per Sector)
select c.industry, sum(case when a.status ILIKE '%rejected%' then 1 else 0 end) as no_of_rejections from companies as c
join jobs as j on c.id = j.company_id
join applications as a on j.id = a.job_id
group by c.industry;

-- 16. Talent Diversification (Students Applying to Multiple Competitors)
select s.id, s.name, count(distinct c.id) as no_of_different_companies from students as s
join applications as a on s.id = a.student_id
join jobs as j on a.job_id = j.id
join companies as c on j.company_id = c.id
group by s.id, s.name;

-- 17. Dead Corporate Profiles (Companies with Zero Active Job Postings)
select c.id, c.company_name from companies as c
left join jobs as j on c.id = j.company_id
where j.id is null;

-- 18. Unengaged Talent Pool (Students with Zero Submitted Applications)
select s.id, s.name from students as s
left join applications as a on s.id = a.student_id
where a.student_id is null;

-- 19. Talent Age Demographics Per Industry (Average Applicant Age Per Sector)
select c.industry, round(avg(s.age), 2) as average_age from students as s
join applications as a on s.id = a.student_id
join jobs as j on a.job_id = j.id
join companies as c on j.company_id = c.id
group by c.industry;

-- 20. Geographic Velocity (Country with the Highest Volume of Job Applicants)
select s.country, count(*) as no_of_applicants from students as s
join applications as a on s.id = a.student_id
group by country
order by no_of_applicants desc
limit 1;

-- 21. Monthly Application Trends (Peak Application Months)
select mon, yr, count(*) as number_of_applications
from
(select *, extract(month from application_date) as mon, extract(year from application_date) as yr from applications) as t
group by mon,yr;

-- 22. Aging Applications (Unresolved Applications Older Than 14 Days)
select *
from
(select *, (current_date - application_date) as no_of_days from applications) as t
where status ILIKE 'applied' and no_of_days > 14;