INSERT INTO departments (department_name, location)
VALUES
('Human Resources', 'Ahmedabad'),
('Finance', 'Mumbai'),
('IT', 'Bangalore'),
('Sales', 'Delhi'),
('Marketing', 'Pune');

SELECT * FROM departments;

INSERT INTO employees
(
department_id,
first_name,
last_name,
email,
phone,
hire_date,
salary
)
VALUES
(3,'Rahul','Sharma','rahul.sharma@example.com','9876543210','2022-01-15',65000.00),
(2,'Priya','Patel','priya.patel@example.com','9876543211','2021-07-10',72000.00),
(1,'Amit','Verma','amit.verma@example.com','9876543212','2023-03-01',50000.00),
(4,'Sneha','Gupta','sneha.gupta@example.com','9876543213','2020-11-20',58000.00),
(5,'Karan','Mehta','karan.mehta@example.com','9876543214','2024-02-05',47000.00);

SELECT * FROM employees;

INSERT INTO attendance
(
employee_id,
attendance_date,
status
)
VALUES
(1,'2026-08-01','Present'),
(2,'2026-08-01','Present'),
(3,'2026-08-01','Absent'),
(4,'2026-08-01','Leave'),
(5,'2026-08-01','Present');

SELECT * FROM attendance;

SELECT
e.employee_id,
e.first_name,
e.last_name,
d.department_name
FROM employees e
JOIN departments d
ON e.department_id = d.department_id;

SELECT
d.department_name,
AVG(e.salary) AS average_salary
FROM employees e
JOIN departments d
ON e.department_id = d.department_id
GROUP BY d.department_name;