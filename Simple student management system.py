# Single Responsibility Principle (SRP)
class Student:
    """
    Represents a student with ID, name, age, and major.
    """
    def __init__(self, id, name, age, major):
        self.id = id
        self.name = name
        self.age = age
        self.major = major

    def display(self):
        """
        Displays the student's information.
        """
        print(f"ID: {self.id}, Name: {self.name}, Age: {self.age}, Major: {self.major}")

class StudentDatabase:
    """
    Manages the collection of students.
    """
    def __init__(self):
        self.students = []

    def add_student(self, student):
        """
        Adds a student to the database.
        """
        self.students.append(student)

    def remove_student(self, student_id):
        """
        Removes a student from the database based on their ID.
        """
        for student in self.students:
            if student.id == student_id:
                self.students.remove(student)
                break

    def display_all_students(self):
        """
        Displays the information of all students in the database.
        """
        for student in self.students:
            student.display()

# Open/Closed Principle (OCP)
class StudentUpdateService:
    """
    Provides functionality to update a student's information.
    """
    def update_student(self, student, name=None, age=None, major=None):
        """
        Updates the specified fields of the given student.
        """
        if name:
            student.name = name
        if age:
            student.age = age
        if major:
            student.major = major
        return student

# Dependency Inversion Principle (DIP)
class StudentManagementSystem:
    """
    Manages the student management system, including adding, deleting, and updating students.
    """
    def __init__(self, database, update_service):
        self.database = database
        self.update_service = update_service

    def add_new_student(self, id, name, age, major):
        """
        Adds a new student to the database.
        """
        student = Student(id, name, age, major)
        self.database.add_student(student)

    def delete_student(self, student_id):
        """
        Deletes a student from the database.
        """
        self.database.remove_student(student_id)

    def update_student_info(self, student_id, name=None, age=None, major=None):
        """
        Updates the information of a student in the database.
        """
        for student in self.database.students:
            if student.id == student_id:
                updated_student = self.update_service.update_student(student, name, age, major)
                self.database.students[self.database.students.index(student)] = updated_student

    def show_all_students(self):
        """
        Displays the information of all students in the database.
        """
        self.database.display_all_students()

# Example Usage
def main():
    database = StudentDatabase()
    update_service = StudentUpdateService()
    system = StudentManagementSystem(database, update_service)

    while True:
        print("\nStudent Management System")
        print("1. Add New Student")
        print("2. Update Student Information")
        print("3. Delete Student")
        print("4. Display All Students")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            id = int(input("Enter student ID: "))
            name = input("Enter student name: ")
            age = int(input("Enter student age: "))
            major = input("Enter student major: ")
            system.add_new_student(id, name, age, major)
            print("Student added successfully!")
        elif choice == "2":
            student_id = int(input("Enter student ID to update: "))
            name = input("Enter new name (or leave blank to skip): ")
            age = input("Enter new age (or leave blank to skip): ")
            major = input("Enter new major (or leave blank to skip): ")
            system.update_student_info(student_id, name, age, major)
            print("Student information updated successfully!")
        elif choice == "3":
            student_id = int(input("Enter student ID to delete: "))
            system.delete_student(student_id)
            print("Student deleted successfully!")
        elif choice == "4":
            system.show_all_students()
        elif choice == "5":
            print("Exiting Student Management System...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
