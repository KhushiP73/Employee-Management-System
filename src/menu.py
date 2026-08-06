from employee import (
    add_employee,
    view_employees,
    search_employee,
    update_employee,
    delete_employee,
)
from department import (
    add_department,
    view_departments,
)

def display_menu():
    while True:
        print("\n" + "=" * 45)
        print(" Employee Management System ")
        print("=" * 45)
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Search Employee")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Department Management")
        print("7. Attendance Management")
        print("8. Reports")
        print("9. Exit")

        choice = input("\nEnter your choice: ")
        if choice == "1":
            add_employee()

        elif choice == "2":
            view_employees()

        elif choice == "3":
            search_employee()

        elif choice == "4":
            update_employee()

        elif choice == "5":
            delete_employee()

        elif choice == "6":
            while True:
                print("\n===== Department Management =====")
                print("1. Add Department")
                print("2. View Departments")
                print("3. Back")

                department_choice = input("Enter your choice: ")

                if department_choice == "1":
                    add_department()

                elif department_choice == "2":
                    view_departments()

                elif department_choice == "3":
                    break

                else:
                    print("\nInvalid choice.")

        elif choice == "7":
            print("\nAttendance")

        elif choice == "8":
            print("\nReports")

        elif choice == "9":
            print("\nThank you for using the Employee Management System.")
            break

        else:
            print("\nInvalid choice! Please try again.")