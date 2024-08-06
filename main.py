from db_operations import add_student, view_students, update_student, delete_student

def main():
    while True:
        print("\n--- Vaishnavi School Students Database ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            update_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()



def add_student():
    print("Inside add_student function")
    # Rest of the code...

def view_students():
    print("Inside view_students function")
    # Rest of the code...

def update_student():
    print("Inside update_student function")
    # Rest of the code...

def delete_student():
    print("Inside delete_student function")
    # Rest of the code...



try:
    choice = input("Enter your choice: ")
    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        update_student()
    elif choice == '4':
        delete_student()
    elif choice == '5':
        print("Exiting the application. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
except Exception as e:
    print(f"An error occurred: {e}")



def add_student():
    """
    Adds a new student to the database.
    Collects input data and saves it.
    """
    # existing code...
