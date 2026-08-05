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