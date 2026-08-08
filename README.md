# Employee Management System with PostgreSQL

A modular command-line Employee Management System built with **Python and PostgreSQL**.

The project demonstrates how Python applications interact with a relational database using `psycopg`, while implementing CRUD operations, database relationships, transactions, exception handling, attendance tracking, and SQL-based reporting.

---

## Project Overview

The Employee Management System is designed to manage employee information, departments, attendance records, and business reports through a command-line interface.

The project focuses on practical usage of:

* Python
* PostgreSQL
* psycopg
* SQL
* Database design
* CRUD operations
* Transactions
* Exception handling
* Modular Python programming

---

## Features

### Employee Management

* Add employee
* View employees
* Search employees
* Update employee information
* Delete employees

### Department Management

* Add department
* View departments
* Update department
* Delete department
* Prevent deletion of departments that still have employees

### Attendance Management

* Mark attendance
* View attendance records
* Prevent duplicate attendance for the same employee and date
* Track Present, Absent, and Leave status

### Reports

* Employee count by department
* Average salary by department
* Highest-paid employee
* Lowest-paid employee
* Attendance summary by employee
* Attendance summary by status
* Department salary statistics
* Employees with perfect attendance
* Employees with low attendance

---

## 🛠️ Tech Stack

| Technology    | Purpose                          |
| ------------- | -------------------------------- |
| Python        | Application logic                |
| PostgreSQL    | Relational database              |
| psycopg       | PostgreSQL database connectivity |
| python-dotenv | Environment variable management  |
| SQL           | Data manipulation and reporting  |
| Git           | Version control                  |
| GitHub        | Project hosting                  |

---

## Project Structure

```text
Employee-Management-System/
│
├── src/
│   ├── database.py
│   ├── utils.py
│   ├── employee.py
│   ├── department.py
│   ├── attendance.py
│   ├── reports.py
│   ├── menu.py
│   └── main.py
│
├── sql/
│   ├── schema.sql
│   └── sample_data.sql
│
├── .env
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

---


### Relationships

* One department can have many employees.
* Each employee belongs to a department.
* One employee can have many attendance records.
* An employee can have only one attendance record for a particular date.

---

##  SQL Concepts Demonstrated

The reporting module uses several important SQL concepts:

* `SELECT`
* `INSERT`
* `UPDATE`
* `DELETE`
* `JOIN`
* `LEFT JOIN`
* `GROUP BY`
* `HAVING`
* `ORDER BY`
* `LIMIT`
* `COUNT()`
* `AVG()`
* `SUM()`
* `MIN()`
* `MAX()`
* `ROUND()`
* `NULLIF()`
* PostgreSQL `FILTER`

Example:

```sql
SELECT
    d.department_name,
    COUNT(e.employee_id) AS total_employees
FROM departments d
LEFT JOIN employees e
    ON d.department_id = e.department_id
GROUP BY d.department_name
ORDER BY total_employees DESC;
```

This generates an employee count for every department while also displaying departments that currently have no employees.

---

# Validation & Error Handling

The application validates user input before sending it to PostgreSQL.

Examples include:

* Invalid numeric input
* Negative salary
* Empty required fields
* Invalid email
* Invalid date format
* Invalid attendance status

Database-level errors are also handled using PostgreSQL-specific exceptions.

Examples:

```text
UniqueViolation
ForeignKeyViolation
CheckViolation
NotNullViolation
```

This allows the application to display meaningful messages instead of exposing raw database errors to the user.

---

# Example Reports

The reporting module can generate information such as:

```text
Employee Count by Department

Department              Employees
----------------------------------
IT                      5
Finance                 3
Marketing               2
HR                      1
```

Attendance reports provide information such as:

```text
Employee              Present   Absent   Leave   Total
--------------------------------------------------------
Employee One             20        2       1      23
Employee Two             18        3       2      23
```

---

## 👩‍💻 Author

**Khushi Panchal**
