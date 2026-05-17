# ==========================================
# IMPORTS
# ==========================================

import os
import sys
from datetime import datetime, date
# (Whatever other libraries or modules you are importing)



# ==========================================
# CUSTOM EXCEPTIONS & SIGNALS
# ==========================================


class BackSignal(Exception):
    """Custom exception to break out of input workflows instantly."""
    pass



# =====================================================================
# TABLE VIEW CONFIGURATIONS & HEADERS
# =====================================================================


STUDENT_HEADERS = ["ID", "Name", "Country", "Age"]
COMPANY_HEADERS = ["ID", "Company", "Country", "Industry"]
JOB_HEADERS = ["ID", "Title", "Salary", "Location", "Company ID"]
APPLICATION_HEADERS = ["ID", "Student ID", "Job ID", "Application Date", "Status"]



# =====================================================================
# GENERATION 1 — BASIC VALIDATION HELPERS
# Phase 1: Taught us loops, try/except, type conversion, and basic checks.
# Flaw: No cancellation path; users get stuck or kicked out to the main menu.
# =====================================================================



"""
def get_valid_age(message="Enter the Age: "):
    while True:
        try:
            age = int(input(message))
            if age <= 0:
                print("Age must be greater than 0")
            else:
                return age
        except ValueError:
            print("Please enter numbers only")

def get_valid_salary(message="Enter the Salary: "):
    while True:
        try:
            salary = int(input(message))
            if salary <= 0:
                print("Salary must be greater than 0")
            else:
                return salary
        except ValueError:
            print("Please enter a valid salary")

def get_valid_id(message="Enter the ID: "):
    while True:
        try:
            student_id = int(input(message))
            if student_id <= 0:
                print("ID should be greater than 0")
            else:
                return student_id
        except ValueError:
            print("Please enter numbers only")

def get_non_empty_string(prompt):
    while True:
        s = input(prompt)
        if s.strip() == "":
            print("String cant be empty or only have spaces")
        else:
            cleaned = s.replace(" ","")
            if cleaned.isalpha():
                return s.strip().title()
            else:
                print("Please enter alphabets and spaces only")

def get_valid_date(message="Enter the date (YYYY-MM-DD): "):
    while True:
        try:
            date_input = input(message)
            valid_date = datetime.strptime(date_input, "%Y-%m-%d").date()
            if valid_date > date.today():
                print("Date cannot be in the future")
            else:
                return valid_date
        except ValueError:
            print("Invalid date format. Use YYYY-MM-DD")
"""


# =====================================================================
# GENERATION 2 — BACK NAVIGATION WORKFLOWS
# Phase 2 Upgrade: Introduced workflow recovery, retry systems, and 'B' key signals.
# Flaw: High code repetition; every data type required its own boilerplate while loop.
# =====================================================================



"""
def get_valid_age_or_back():
    while True:
        age = input("Enter the valid age or b to go back: ")
        if age.upper() == 'B':
            return 'BACK'
        try:
            age = int(age)
        except ValueError:
            print("Please enter a valid integer age: ")
            continue
        if age < 18:
            print("Age should be atleast 18.")
            continue
        return age

def get_valid_salary_or_back():
    while True:
        salary = input("Enter salary (B to go back): ").strip()
        if salary.upper() == "B":
            return "BACK"
        try:
            salary = float(salary)
        except ValueError:
            print("Please enter a valid numeric salary.")
            continue
        if salary <= 0:
            print("Salary must be greater than 0.")
            continue
        return salary

def get_valid_id_or_back():
    while True:
        student_id = input("Enter the student id or B to go Back: ").strip()
        if student_id.upper() == "B":
            return "BACK"
        try:
            student_id = int(student_id)
        except ValueError:
            print("Enter a valid interger id.")
            continue
        if not queries.student_exists(student_id):
            print("Student not found.")
            continue
        return student_id

def get_non_empty_string_or_back(prompt):
    while True:
        s = input(f"{prompt}  or (B to go back): ").strip()
        if s.upper() == "B":
            return "BACK"
        if s == "":
            print("String cannot be empty.")
            continue
        cleaned = s.replace(" ", "")
        if cleaned.isalpha():
            return s.title()
        print("Please enter alphabets and spaces only.")

def get_valid_date_or_back():
    while True:
        date_input = input("Enter date (YYYY-MM-DD) or (B to go back): ").strip()
        if date_input.upper() == "B":
            return "BACK"
        try:
            valid_date = datetime.strptime(date_input, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format. Use YYYY-MM-DD.")
            continue
        if valid_date > date.today():
            print("Date cannot be in the future.")
            continue
        return valid_date
"""


# =====================================================================
# GENERATION 3 — ABSTRACT REUSABLE VALIDATION SYSTEMS (CURRENT)
# Master Core Architecture: Single unified processing engine that intercepts 'BACK'
# options, wraps try/except loops, and lets specific functions scale beautifully.
# =====================================================================




def _execute_abstract_input_workflow(prompt_msg, cast_callback, validation_callback=None):
    """
    Core Master Engine. Standardizes application-wide workflow interactions.
    Handles 'B' backtracking, custom casting errors, and validation checks.
    """
    while True:
        raw_string = input(f"{prompt_msg} (or press 'B' to go back): ").strip()
        
        # Step 1: Universal Intercept Control Flow
        if raw_string.upper() in ['B', 'BACK']:
            raise BackSignal() # 🚀 FIXED: Changed 'return' to 'raise' so it actually escapes to main.py
            
        # Step 2: Explicit Data Transformation / Casting
        try:
            transformed_data = cast_callback(raw_string)
        except Exception as error_context:
            print(f"Invalid format: {error_context}")
            continue
            
        # Step 3: Business Rule Evaluation
        if validation_callback:
            error_message = validation_callback(transformed_data)
            if error_message:
                print(f"Validation Error: {error_message}")
                continue
                
        return transformed_data



# =====================================================================
# REUSABLE FRONT-END COMPLIANCE INTERFACES
# =====================================================================


def get_clean_string(prompt):
    """Captures clean, title-cased alpha-only textual structures."""
    def cast_logic(s):
        if not s:
            raise ValueError("Input workspace cannot be blank.")
        if not s.replace(" ", "").isalpha():
            raise ValueError("Input must only contain alphabetic letters and spaces.")
        return s.title()
        
    return _execute_abstract_input_workflow(prompt, cast_logic, validation_callback=None)



def get_clean_integer(prompt, min_threshold=0, exists_db_callback=None, missing_db_err_msg=None):
    """Captures valid whole integers with range checks and optional DB identity confirmation."""
    def cast_logic(s):
        return int(s)
        
    def validation_logic(value):
        if value < min_threshold:
            return f"Value must be at least {min_threshold}."
        if exists_db_callback and not exists_db_callback(value):
            return missing_db_err_msg or "Reference matching ID could not be located in database."
        return None
        
    return _execute_abstract_input_workflow(prompt, cast_logic, validation_logic)



def get_clean_float(prompt, min_value=0.0):
    """Captures accurate scalar values (salary, metrics)."""
    def cast_logic(s):
        return float(s)
        
    def validation_logic(value):
        if value <= min_value:
            return f"Numeric metric value must be strictly greater than {min_value}."
        return None
        
    return _execute_abstract_input_workflow(prompt, cast_logic, validation_logic)


def get_clean_date(prompt="Enter the target date (YYYY-MM-DD)"):
    """Parses system dates and confirms historical constraints."""
    def cast_logic(s):
        return datetime.strptime(s, "%Y-%m-%d").date()
        
    def validation_logic(parsed_date):
        if parsed_date > date.today():
            return "Future dates are unauthorized for this tracking system."
        return None
        
    return _execute_abstract_input_workflow(prompt, cast_logic, validation_logic)





# =====================================================================
# CONSOLE DISPLAY INTERFACES
# =====================================================================



def display_data(headers, rows):
    """Prints uniform database grids across standard terminal boundaries."""
    print()
    for header in headers:
        print(f"{header:<25}", end=" ")
    print()
    print("-" * (len(headers) * 25))

    for row in rows:
        for value in row:
            print(f"{str(value):<25}", end=" ")
        print()


def display_metric(label, value):
    """Safely wraps single summary values into a table output grid."""
    safe_value = value if value is not None else 0
    display_data([label], [[safe_value]])