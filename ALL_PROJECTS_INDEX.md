COMPLETE PROJECT INDEX & FILE GUIDE
====================================

This document lists all 11 projects in the workspace with their important files and descriptions.
Use this for quick reference during exam preparation.

---

PROJECT 1: biodata_project
==========================
Purpose: Simple form to accept and display biodata without database.

Important Files:
1. biodata_project/biodata/forms.py
   - Defines BiodataForm with fields: name, age, email, phone, address
   - Form fields are CharField, IntegerField, EmailField with Bootstrap styling
   
2. biodata_project/biodata/views.py
   - biodata_form view: accepts POST/GET requests
   - On POST with valid form: extracts cleaned_data and renders display template
   - On GET: renders form template

3. biodata_project/biodata/urls.py
   - Routes root path '' to biodata_form view

4. biodata_project/biodata/templates/biodata/form.html
   - HTML form with fields for name, age, email, phone, address

5. biodata_project/biodata/templates/biodata/display.html
   - Displays submitted biodata fields

6. biodata_project/biodata_project/urls.py (project level)
   - Includes biodata app URLs at path 'biodata/' or root

Setup: No database needed. Uses plain Form (not ModelForm).

---

PROJECT 2: student_cie_project
==============================
Purpose: Accept student info and CIE marks, filter students with CIE < 20 in database.

Important Files:
1. student_cie_project/student_cie/models.py
   - Model: Student (usn, name, subject_code, cie_marks)
   - usn is unique CharField
   - cie_marks is IntegerField

2. student_cie_project/student_cie/forms.py
   - StudentForm: ModelForm for Student model
   - Fields: usn, name, subject_code, cie_marks

3. student_cie_project/student_cie/views.py
   - add_student: form to create new student records
   - display_low_cie: filters Student.objects with cie_marks < 20
   - all_students: displays all student records

4. student_cie_project/student_cie/urls.py
   - Routes: '' (add), 'low-cie/' (low CIE), 'all-students/' (all)

5. student_cie_project/student_cie/templates/student_cie/
   - add_student.html, display_students.html, all_students.html

6. student_cie_project/student_cie/admin.py
   - StudentAdmin registered with list_display and search_fields

Setup: Requires makemigrations and migrate (uses SQLite database).

---

PROJECT 3: exam_fee_project
============================
Purpose: Manage student exam fees, mark fee status, delete unpaid students.

Important Files:
1. exam_fee_project/exam_fee/models.py
   - Model: ExamStudent (usn, name, semester, fee_amount, fee_paid)
   - usn is unique CharField
   - fee_amount is DecimalField, fee_paid is BooleanField

2. exam_fee_project/exam_fee/forms.py
   - ExamStudentForm: ModelForm for ExamStudent
   - Fields: usn, name, semester, fee_amount (form omits fee_paid field)

3. exam_fee_project/exam_fee/views.py
   - add_student: creates student record; sets fee_paid=True if fee_amount > 0
   - list_students: displays all ExamStudent records
   - delete_unpaid: deletes all records where fee_paid=False

4. exam_fee_project/exam_fee/urls.py
   - Routes: '' (add), 'list/' (list all), 'delete-unpaid/' (delete unpaid)

5. exam_fee_project/exam_fee/templates/exam_fee/
   - add_student.html, list_students.html

6. exam_fee_project/exam_fee/admin.py
   - ExamStudentAdmin registered

Setup: Requires makemigrations and migrate (uses SQLite database).

---

PROJECT 4: exam_management_project
===================================
Purpose: Manage student exam grades, filter students with grade='O' (Excellent).

Important Files:
1. exam_management_project/exam_app/models.py
   - Model: Student (usn, name, semester, subject_code, grade)
   - grade field uses choices: A, B, C, D, E, O (Excellent)

2. exam_management_project/exam_app/forms.py
   - StudentForm: ModelForm for Student

3. exam_management_project/exam_app/views.py
   - add_student: accepts new student records
   - ograde_students: filters Student.objects with grade='O'
   - all_students: displays all students

4. exam_management_project/exam_app/urls.py
   - Routes: '' (add), 'ograde/' (O-grade filter), 'all-students/' (all)

5. exam_management_project/exam_app/templates/exam_app/
   - add_student.html, ograde_students.html, all_students.html

6. exam_management_project/exam_app/admin.py
   - StudentAdmin registered

Setup: Requires makemigrations and migrate (uses SQLite database).

---

PROJECT 5: final_year_project (placements)
===========================================
Purpose: Track student placements; filter students placed in Amazon.

Important Files:
1. final_year_project/placements/models.py
   - Model: Placement (usn, name, company)
   - usn and name are CharFields, company is CharField

2. final_year_project/placements/forms.py
   - PlacementForm: ModelForm for Placement

3. final_year_project/placements/views.py
   - add_placement: accepts placement records
   - amazon_list: filters Placement with company__icontains='amazon' (case-insensitive)
   - all_placements: displays all placement records

4. final_year_project/placements/urls.py
   - Routes: '' (add), 'amazon/' (Amazon filter), 'all/' (all)

5. final_year_project/placements/templates/placements/
   - add_placement.html, amazon_list.html, all_placements.html

6. final_year_project/placements/admin.py
   - PlacementAdmin registered

Setup: Requires makemigrations and migrate (uses SQLite database).

---

PROJECT 6: faculty_project
==========================
Purpose: Manage faculty info; filter CSE branch professors.

Important Files:
1. faculty_project/faculty/models.py
   - Model: Faculty (faculty_id, title, name, branch)
   - title has choices (Professor, Associate, Assistant, Lecturer)
   - branch is CharField

2. faculty_project/faculty/forms.py
   - FacultyForm: ModelForm for Faculty

3. faculty_project/faculty/views.py
   - add_faculty: accepts faculty records
   - cse_professors: filters Faculty with branch__iexact='CSE' AND title__iexact='Professor'
   - all_faculty: displays all faculty

4. faculty_project/faculty/urls.py
   - Routes: '' (add), 'cse-professors/' (filter), 'all/' (all)

5. faculty_project/faculty/templates/faculty/
   - add_faculty.html, cse_professors.html, all_faculty.html

6. faculty_project/faculty/admin.py
   - FacultyAdmin registered

Setup: Requires makemigrations and migrate (uses SQLite database).

---

PROJECT 7: hr_project (employees)
==================================
Purpose: Manage employee records; filter employees with salary > 50000.

Important Files:
1. hr_project/employees/models.py
   - Model: Employee (name, email, phone, hired_date, job_title, salary)
   - name, email, phone, job_title are CharFields
   - hired_date is DateField
   - salary is DecimalField or FloatField

2. hr_project/employees/forms.py
   - EmployeeForm: ModelForm for Employee with date widget for hired_date

3. hr_project/employees/views.py
   - add_employee: accepts employee records
   - high_salary: filters Employee with salary__gt=50000
   - all_employees: displays all employees

4. hr_project/employees/urls.py
   - Routes: '' (add), 'high/' (high salary), 'all/' (all)

5. hr_project/employees/templates/employees/
   - add_employee.html, high_salary.html, all_employees.html

6. hr_project/employees/admin.py
   - EmployeeAdmin registered

Setup: Requires makemigrations and migrate (uses SQLite database).

---

PROJECT 8: student_update_project (students)
=============================================
Purpose: Accept student info; update student grade by searching for name.

Important Files:
1. student_update_project/students/models.py
   - Model: Student (usn, name, dept, grade)
   - All are CharFields

2. student_update_project/students/forms.py
   - StudentForm: ModelForm for Student
   - UpdateGradeForm: plain Form with name (CharField) and grade (CharField)

3. student_update_project/students/views.py
   - add_student: creates new student records
   - list_students: displays all students
   - update_grade: accepts name and grade; finds student by name (case-insensitive) and updates grade

4. student_update_project/students/urls.py
   - Routes: '' (add), 'list/' (list), 'update/' (update by name)

5. student_update_project/students/templates/students/
   - add_student.html, list_students.html, update_grade.html

6. student_update_project/students/admin.py
   - StudentAdmin registered

Setup: Requires makemigrations and migrate (uses SQLite database).

---

PROJECT 9: weather_project
===========================
Purpose: Accept city name; fetch live weather from OpenWeatherMap API.

Important Files:
1. weather_project/weather/forms.py
   - CityForm: plain Form with city CharField field

2. weather_project/weather/views.py
   - index view: 
     * Accepts city name via POST
     * Calls OpenWeatherMap API: https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric
     * API_KEY = '5adbed3462abeb36442b53e62be8a29b'
     * On success: extracts city name, temperature (°C), and weather description
     * On error: displays API error message or network error message
   - Renders weather/index.html with form, weather data, or error

3. weather_project/weather/urls.py
   - Routes: '' (root path) to index view

4. weather_project/weather/templates/weather/index.html
   - Form to accept city name
   - Display area for weather data (city, temp, description)
   - Display area for error messages

5. weather_project/requirements.txt
   - Lists Django and requests package dependencies

Setup: No database needed. Requires requests package (pip install requests).

---

PROJECT 10: hello_project
==========================
Purpose: Basic Django "Hello World" starter project.

Important Files:
1. hello_project/myapp/ (main app)
   - Likely contains views, urls, templates for basic app demo
   
2. hello_project/hello_project/ (project config)
   - settings.py, urls.py, wsgi.py, asgi.py

Setup: Basic Django project structure. Check specific files for details.

---

PROJECT 11: xss_demo
====================
Purpose: Demonstration of XSS (Cross-Site Scripting) vulnerability.

Important Files:
1. xss_demo/xss_app/
   - Views and templates for XSS demo
   - Likely shows vulnerable and safe code patterns

2. xss_demo/xss_project/ (project config)
   - settings.py, urls.py, wsgi.py, asgi.py

Setup: Basic Django project. Check specific files for XSS examples.

---

COMMON SETUP STEPS FOR ALL DATABASE PROJECTS
=============================================

For projects using SQLite (all except biodata_project and weather_project):

```
cd c:\Users\amanc\Desktop\CODE\kal test\<project_name>
..\myevn\Scripts\activate
pip install django
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Then open: http://127.0.0.1:8000/

---

QUICK REFERENCE: File Locations
================================

Each project follows Django structure:
- <project_name>/manage.py — Django management script
- <project_name>/<project_name>/settings.py — project configuration
- <project_name>/<project_name>/urls.py — project-level URL routing
- <project_name>/<app_name>/models.py — database models (if app uses DB)
- <project_name>/<app_name>/views.py — view logic and request handling
- <project_name>/<app_name>/forms.py — form definitions
- <project_name>/<app_name>/urls.py — app-level URL routing
- <project_name>/<app_name>/templates/<app_name>/ — HTML templates
- <project_name>/<app_name>/admin.py — Django admin registration

---

END OF INDEX
