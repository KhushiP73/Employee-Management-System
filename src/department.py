from database import get_connection
from utils import (
    get_integer,
    get_required_text,
)

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
        department_name = get_required_text("Department Name: ")
        location = get_required_text("Location: ")

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

def update_department():
    try:
        conn = get_connection()
        cur = conn.cursor()
        department_id = get_integer("\nEnter Department ID to update: ")
        department_name = get_required_text("New Department Name: ")
        location = get_required_text("New Location: ")

        cur.execute(
            """
            SELECT
                department_id,
                department_name,
                location
            FROM departments
            WHERE department_id = %s
            """,
            (department_id,),
        )
        department = cur.fetchone()

        if department is None:
            print("\nDepartment not found.")
            return

        print("\nCurrent Details")
        print("-------------------------")
        print(f"Name : {department['department_name']}")
        print(f"Location : {department['location']}")

        department_name = input("New Department Name: ").strip()
        location = input("New Location: ").strip()

        cur.execute(
            """
            UPDATE departments
            SET
                department_name = %s,
                location = %s
            WHERE department_id = %s
            """,
            (
                department_name,
                location,
                department_id,
            ),
        )

        conn.commit()
        print("\nDepartment updated successfully!")

    except Exception as e:
        if "conn" in locals():
            conn.rollback()
        print("\nError:", e)

    finally:
        if "cur" in locals():
            cur.close()

        if "conn" in locals():
            conn.close()

def delete_department():
    try:
        conn = get_connection()
        cur = conn.cursor()
        department_id = get_integer("\nEnter Department ID to delete: ")
        cur.execute(
            """
            SELECT
                department_id,
                department_name
            FROM departments
            WHERE department_id = %s
            """,
            (department_id,),
        )

        department = cur.fetchone()

        if department is None:
            print("\nDepartment not found.")
            return

        print("\nDepartment Found")
        print("-------------------------")
        print(f"ID   : {department['department_id']}")
        print(f"Name : {department['department_name']}")

        confirm = input("\nDelete this department? (y/n): ").strip().lower()
        if confirm != "y":
            print("\nDeletion cancelled.")
            return

        cur.execute(
            """
            DELETE FROM departments
            WHERE department_id = %s
            """,
            (department_id,),
        )

        conn.commit()
        print("\nDepartment deleted successfully!")

    except Exception as e:
        if "conn" in locals():
            conn.rollback()

        error_message = str(e).lower()
        if "foreign key" in error_message:
            print(
                "\nCannot delete department because employees are assigned to it."
            )
            print("Move or delete those employees first.")
        else:
            print("\nError:", e)

    finally:
        if "cur" in locals():
            cur.close()

        if "conn" in locals():
            conn.close()