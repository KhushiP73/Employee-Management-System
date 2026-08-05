-- Departments Table
CREATE TABLE departments (
    department_id SERIAL PRIMARY KEY,
    department_name VARCHAR(100) NOT NULL UNIQUE,
    location VARCHAR(100)
);

-- Employees Table
CREATE TABLE employees (
    employee_id SERIAL PRIMARY KEY,
    department_id INTEGER NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    hire_date DATE NOT NULL,
    salary NUMERIC(10,2) NOT NULL CHECK (salary >= 0),
    CONSTRAINT fk_department
        FOREIGN KEY (department_id)
        REFERENCES departments(department_id)
        ON DELETE RESTRICT
);

-- Attendance Table
CREATE TABLE attendance (
    attendance_id SERIAL PRIMARY KEY,
    employee_id INTEGER NOT NULL,
    attendance_date DATE NOT NULL,
    status VARCHAR(15) NOT NULL
        CHECK (status IN ('Present','Absent','Leave')),
    CONSTRAINT fk_employee
        FOREIGN KEY (employee_id)
        REFERENCES employees(employee_id)
        ON DELETE CASCADE,
    UNIQUE(employee_id, attendance_date)
);