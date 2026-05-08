# Student Learning Management System (LMS)
import sys
from core.models import Student, Teacher
from core.manager import LMSManager

def main():
    lms = LMSManager()
    
    while True:
        print("\n--- STUDENT LEARNING MANAGEMENT SYSTEM ---")
        print("1. Add Student")
        print("2. Add Teacher")
        print("3. View All Users")
        print("4. Exit")
        
        choice = input("Select an option (1-4): ")
        
        if choice == '1':
            try:
                sid = int(input("Enter Student ID: "))
                name = input("Enter Name: ")
                email = input("Enter Email: ")
                student = Student(sid, name, email)
                lms.register_user(student)
                print(f" Student {name} added successfully!")
            except ValueError as e:
                print(f" Error: {e}")

        elif choice == '2':
            try:
                tid = int(input("Enter Teacher ID: "))
                name = input("Enter Name: ")
                email = input("Enter Email: ")
                dept = input("Enter Department: ")
                teacher = Teacher(tid, name, email, dept)
                lms.register_user(teacher)
                print(f"Teacher {name} added successfully!")
            except ValueError as e:
                print(f" Error: {e}")

        elif choice == '3':
            print("\n--- Registered Users ---")
            if lms.get_user_count() == 0:
                print("No users found.")
            else:
                for user_id, user in lms.users.items():
                    print(f"[{user.get_role()}] ID: {user_id} | Name: {user.name}")

        elif choice == '4':
            print(" Exiting system. Goodbye!")
            sys.exit()
            
        else:
            print(" Invalid choice, please try again.")

if __name__ == "__main__":
    main()
