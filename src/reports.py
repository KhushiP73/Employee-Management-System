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

def attendance_summary_by_employee():
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            """
            SELECT
                e.employee_id,
                e.first_name,
                e.last_name,
                COUNT(*) FILTER (
                    WHERE a.status = 'Present'
                ) AS present_days,
                COUNT(*) FILTER (
                    WHERE a.status = 'Absent'
                ) AS absent_days,
                COUNT(*) FILTER (
                    WHERE a.status = 'Leave'
                ) AS leave_days,
                COUNT(a.attendance_id) AS total_days
            FROM employees e
            LEFT JOIN attendance a
                ON e.employee_id = a.employee_id
            GROUP BY
                e.employee_id,
                e.first_name,
                e.last_name
            ORDER BY e.employee_id;
            """
        )

        rows = cur.fetchall()

        print("\n===== Attendance Summary by Employee =====\n")
        print(
            f"{'Employee':<25}"
            f"{'Present':<10}"
            f"{'Absent':<10}"
            f"{'Leave':<10}"
            f"{'Total':<10}"
        )
        print("-" * 65)

        for row in rows:
            name = (
                row["first_name"]
                + " "
                + row["last_name"]
            )
            print(
                f"{name:<25}"
                f"{row['present_days']:<10}"
                f"{row['absent_days']:<10}"
                f"{row['leave_days']:<10}"
                f"{row['total_days']:<10}"
            )

    except Exception as e:
        print("\nError:", e)

    finally:
        if "cur" in locals():
            cur.close()
        if "conn" in locals():
            conn.close()

def attendance_summary_by_status():
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            """
            SELECT
                status,
                COUNT(*) AS total_records
            FROM attendance
            GROUP BY status
            ORDER BY total_records DESC;
            """
        )
        rows = cur.fetchall()

        print("\n===== Attendance Summary =====\n")
        print(
            f"{'Status':<15}"
            f"{'Records':<10}"
        )
        print("-" * 30)
        for row in rows:
            print(
                f"{row['status']:<15}"
                f"{row['total_records']:<10}"
            )

    except Exception as e:
        print("\nError:", e)

    finally:
        if "cur" in locals():
            cur.close()
        if "conn" in locals():
            conn.close()

def department_salary_statistics():
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            """
            SELECT
                d.department_name,
                COUNT(e.employee_id) AS employee_count,
                ROUND(AVG(e.salary), 2) AS average_salary,
                MIN(e.salary) AS minimum_salary,
                MAX(e.salary) AS maximum_salary,
                SUM(e.salary) AS total_salary
            FROM departments d
            LEFT JOIN employees e
                ON d.department_id = e.department_id
            GROUP BY d.department_name
            ORDER BY average_salary DESC NULLS LAST;
            """
        )
        rows = cur.fetchall()
        print("\n===== Department Salary Statistics =====\n")
        print(
            f"{'Department':<20}"
            f"{'Employees':<10}"
            f"{'Average':<12}"
            f"{'Min':<12}"
            f"{'Max':<12}"
        )
        print("-" * 70)
        for row in rows:
            average = (
                row["average_salary"]
                if row["average_salary"] is not None
                else 0
            )
            minimum = (
                row["minimum_salary"]
                if row["minimum_salary"] is not None
                else 0
            )
            maximum = (
                row["maximum_salary"]
                if row["maximum_salary"] is not None
                else 0
            )
            print(
                f"{row['department_name']:<20}"
                f"{row['employee_count']:<10}"
                f"{average:<12}"
                f"{minimum:<12}"
                f"{maximum:<12}"
            )

    except Exception as e:
        print("\nError:", e)

    finally:
        if "cur" in locals():
            cur.close()
        if "conn" in locals():
            conn.close()

def employees_with_perfect_attendance():
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            """
            SELECT
                e.employee_id,
                e.first_name,
                e.last_name,
                COUNT(a.attendance_id) AS total_days
            FROM employees e
            JOIN attendance a
                ON e.employee_id = a.employee_id
            GROUP BY
                e.employee_id,
                e.first_name,
                e.last_name
            HAVING
                COUNT(a.attendance_id)
                =
                COUNT(*) FILTER (
                    WHERE a.status = 'Present'
                )
            ORDER BY total_days DESC;
            """
        )
        rows = cur.fetchall()
        print("\n===== Employees With Perfect Attendance =====\n")

        if not rows:
            print("No employees currently have perfect attendance.")
            return
        print(
            f"{'Employee':<25}"
            f"{'Present Days':<15}"
        )
        print("-" * 45)
        for row in rows:
            name = (
                row["first_name"]
                + " "
                + row["last_name"]
            )
            print(
                f"{name:<25}"
                f"{row['total_days']:<15}"
            )

    except Exception as e:
        print("\nError:", e)

    finally:
        if "cur" in locals():
            cur.close()

        if "conn" in locals():
            conn.close()

def employees_with_low_attendance():
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            """
            SELECT
                e.employee_id,
                e.first_name,
                e.last_name,
                COUNT(a.attendance_id) AS total_days,
                COUNT(*) FILTER (
                    WHERE a.status = 'Present'
                ) AS present_days,
                ROUND(
                    COUNT(*) FILTER (
                        WHERE a.status = 'Present'
                    ) * 100.0
                    / NULLIF(COUNT(a.attendance_id), 0),
                    2
                ) AS attendance_percentage
            FROM employees e
            JOIN attendance a
                ON e.employee_id = a.employee_id
            GROUP BY
                e.employee_id,
                e.first_name,
                e.last_name
            HAVING
                COUNT(*) FILTER (
                    WHERE a.status = 'Present'
                ) * 100.0
                / NULLIF(COUNT(a.attendance_id), 0) < 75
            ORDER BY attendance_percentage;
            """
        )
        rows = cur.fetchall()
        print("\n===== Low Attendance Report =====\n")
        if not rows:
            print("No employees have attendance below 75%.")
            return
        print(
            f"{'Employee':<25}"
            f"{'Total Days':<12}"
            f"{'Present':<10}"
            f"{'Attendance %':<15}"
        )
        print("-" * 65)

        for row in rows:
            name = (
                row["first_name"]
                + " "
                + row["last_name"]
            )
            print(
                f"{name:<25}"
                f"{row['total_days']:<12}"
                f"{row['present_days']:<10}"
                f"{row['attendance_percentage']:<15}"
            )

    except Exception as e:
        print("\nError:", e)

    finally:
        if "cur" in locals():
            cur.close()
        if "conn" in locals():
            conn.close()