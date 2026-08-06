from database import get_connection

def display_attendance(records):
    if not records:
        print("\nNo attendance records found.")
        return

    print("\n" + "=" * 90)
    print("Attendance Records")
    print("=" * 90)

    print(
        f"{'ID':<5}"
        f"{'Employee':<25}"
        f"{'Date':<15}"
        f"{'Status':<15}"
    )
    print("-" * 90)

    for record in records:
        full_name = (
            record["first_name"]
            + " "
            + record["last_name"]
        )
        print(
            f"{record['attendance_id']:<5}"
            f"{full_name:<25}"
            f"{str(record['attendance_date']):<15}"
            f"{record['status']:<15}"
        )

def mark_attendance():
    try:
        conn = get_connection()
        cur = conn.cursor()

        print("\n===== Mark Attendance =====")
        employee_id = int(input("Employee ID: "))
        attendance_date = input("Date (YYYY-MM-DD): ")
        status = input(
            "Status (Present/Absent/Leave): "
        ).capitalize()

        if status not in ["Present", "Absent", "Leave"]:
            print("\nInvalid attendance status.")
            return

        cur.execute(
            """
            INSERT INTO attendance
            (
                employee_id,
                attendance_date,
                status
            )
            VALUES
            (%s, %s, %s)
            """,
            (
                employee_id,
                attendance_date,
                status,
            ),
        )
        conn.commit()
        print("\nAttendance marked successfully!")

    except Exception as e:
        if "conn" in locals():
            conn.rollback()
        message = str(e).lower()

        if "unique" in message:
            print(
                "\nAttendance already exists for this employee on this date."
            )

        elif "foreign key" in message:
            print("\nEmployee ID does not exist.")

        else:
            print("\nError:", e)

    finally:
        if "cur" in locals():
            cur.close()

        if "conn" in locals():
            conn.close()

def view_attendance():
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            """
            SELECT
                a.attendance_id,
                e.first_name,
                e.last_name,
                a.attendance_date,
                a.status
            FROM attendance a
            JOIN employees e
            ON a.employee_id = e.employee_id
            ORDER BY
                attendance_date DESC,
                first_name
            """
        )
        records = cur.fetchall()
        display_attendance(records)

    except Exception as e:
        print("\nError:", e)

    finally:
        if "cur" in locals():
            cur.close()

        if "conn" in locals():
            conn.close()