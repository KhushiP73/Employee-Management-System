from database import get_connection

def employee_count_by_department():
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            """
            SELECT
                d.department_name,
                COUNT(e.employee_id) AS total_employees
            FROM departments d
            LEFT JOIN employees e
                ON d.department_id = e.department_id
            GROUP BY d.department_name
            ORDER BY total_employees DESC;
            """
        )
        rows = cur.fetchall()
        print("\n===== Employee Count by Department =====\n")
        print(f"{'Department':<25}{'Employees':<10}")
        print("-" * 40)
        for row in rows:
            print(
                f"{row['department_name']:<25}"
                f"{row['total_employees']:<10}"
            )

    except Exception as e:
        print("\nError:", e)

    finally:
        if "cur" in locals():
            cur.close()
        if "conn" in locals():
            conn.close()

def average_salary_by_department():
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            """
            SELECT
                d.department_name,
                ROUND(AVG(e.salary), 2) AS average_salary
            FROM departments d
            LEFT JOIN employees e
                ON d.department_id = e.department_id
            GROUP BY d.department_name
            ORDER BY average_salary DESC NULLS LAST;
            """
        )
        rows = cur.fetchall()
        print("\n===== Average Salary by Department =====\n")
        print(f"{'Department':<25}{'Average Salary'}")
        print("-" * 45)

        for row in rows:
            print(
                f"{row['department_name']:<25}"
                f"{row['average_salary']}"
            )

    except Exception as e:
        print("\nError:", e)

    finally:
        if "cur" in locals():
            cur.close()
        if "conn" in locals():
            conn.close()

def highest_paid_employee():
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            """
            SELECT
                first_name,
                last_name,
                salary
            FROM employees
            ORDER BY salary DESC
            LIMIT 1;
            """
        )
        employee = cur.fetchone()
        if employee:
            print("\n===== Highest Paid Employee =====\n")
            print(
                f"{employee['first_name']} "
                f"{employee['last_name']}"
            )
            print(f"Salary: {employee['salary']}")

    except Exception as e:
        print("\nError:", e)

    finally:
        if "cur" in locals():
            cur.close()
        if "conn" in locals():
            conn.close()

def lowest_paid_employee():
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            """
            SELECT
                first_name,
                last_name,
                salary
            FROM employees
            ORDER BY salary ASC
            LIMIT 1;
            """
        )
        employee = cur.fetchone()
        if employee:
            print("\n===== Lowest Paid Employee =====\n")
            print(
                f"{employee['first_name']} "
                f"{employee['last_name']}"
            )
            print(f"Salary: {employee['salary']}")

    except Exception as e:
        print("\nError:", e)

    finally:
        if "cur" in locals():
            cur.close()
        if "conn" in locals():
            conn.close()