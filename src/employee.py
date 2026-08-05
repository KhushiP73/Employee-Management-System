from database import get_connection

def add_employee():
    try:
        conn = get_connection()
        cur = conn.cursor()

        print("\n===== Add Employee =====")
        department_id = int(input("Department ID: "))
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        email = input("Email: ")
        phone = input("Phone: ")
        hire_date = input("Hire Date (YYYY-MM-DD): ")
        salary = float(input("Salary: "))

        query = """
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
        (%s, %s, %s, %s, %s, %s, %s)
        """

        cur.execute(
            query,
            (
                department_id,
                first_name,
                last_name,
                email,
                phone,
                hire_date,
                salary,
            ),
        )

        conn.commit()

        print("\nEmployee added successfully!")

    except Exception as e:
        print("\nError:", e)

    finally:
        if "cur" in locals():
            cur.close()

        if "conn" in locals():
            conn.close()

def view_employees():
    try:
        conn = get_connection()
        cur = conn.cursor()

        query = """
        SELECT
            e.employee_id,
            e.first_name,
            e.last_name,
            d.department_name,
            e.email,
            e.phone,
            e.hire_date,
            e.salary
        FROM employees e
        JOIN departments d
            ON e.department_id = d.department_id
        ORDER BY e.employee_id;
        """

        cur.execute(query)
        employees = cur.fetchall()

        if not employees:
            print("\nNo employees found.")
            return

        print("\n================ Employee List ================\n")
        print(
            f"{'ID':<5}"
            f"{'Name':<25}"
            f"{'Department':<20}"
            f"{'Salary':<12}"
        )
        print("-" * 65)
        for emp in employees:
            print(
                f"{emp[0]:<5}"
                f"{emp[1] + ' ' + emp[2]:<25}"
                f"{emp[3]:<20}"
                f"{emp[7]:<12}"
            )

    except Exception as e:
        print("Error:", e)

    finally:
        if "cur" in locals():
            cur.close()

        if "conn" in locals():
            conn.close()