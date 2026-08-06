from database import get_connection

def display_departments(departments):
    if not departments:
        print("\nNo departments found.")
        return

    print("\n" + "=" * 55)
    print("Departments")
    print("=" * 55)
    print(
        f"{'ID':<5}"
        f"{'Department':<25}"
        f"{'Location':<20}"
    )
    print("-" * 55)

    for department in departments:
        print(
            f"{department['department_id']:<5}"
            f"{department['department_name']:<25}"
            f"{department['location']:<20}"
        )

def add_department():
    try:
        conn = get_connection()
        cur = conn.cursor()

        print("\n===== Add Department =====")

        department_name = input("Department Name: ").strip()
        location = input("Location: ").strip()

        cur.execute(
            """
            INSERT INTO departments
            (
                department_name,
                location
            )
            VALUES
            (%s, %s)
            """,
            (
                department_name,
                location,
            ),
        )
        conn.commit()
        print("\nDepartment added successfully!")

    except Exception as e:
        if "conn" in locals():
            conn.rollback()
        print("\nError:", e)

    finally:
        if "cur" in locals():
            cur.close()

        if "conn" in locals():
            conn.close()

def view_departments():
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            """
            SELECT
                department_id,
                department_name,
                location
            FROM departments
            ORDER BY department_id
            """
        )
        departments = cur.fetchall()
        display_departments(departments)

    except Exception as e:
        print("\nError:", e)

    finally:
        if "cur" in locals():
            cur.close()

        if "conn" in locals():
            conn.close()

