# Mini Project 1: Student database management system
# Simple in-memory student database with CRUD operations.

"""
Features:
1. Add a new student
2. View all students
3. Search for a student by name
4. Update a student's information (name, age, grade, marks, contact number, address, etc.)
"""

from typing import List, Optional


class Student:
    """Represents a student with essential attributes."""

    def __init__(
        self,
        student_id: int,
        name: str,
        age: int,
        grade: str,
        marks: dict,
        contact_number: str,
        address: str,
    ):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade
        self.marks = marks  # e.g., {"math": 90, "science": 85}
        self.contact_number = contact_number
        self.address = address

    def __repr__(self) -> str:
        return (
            f"Student(ID={self.student_id}, Name='{self.name}', Age={self.age}, "
            f"Grade='{self.grade}', Marks={self.marks}, Contact='{self.contact_number}', "
            f"Address='{self.address}')"
        )

    def to_dict(self) -> dict:
        """Convert student data to a dictionary for easy serialization."""
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "grade": self.grade,
            "marks": self.marks,
            "contact_number": self.contact_number,
            "address": self.address,
        }

    @staticmethod
    def from_dict(data: dict) -> "Student":
        """Create a Student instance from a dictionary."""
        return Student(
            student_id=data["student_id"],
            name=data["name"],
            age=data["age"],
            grade=data["grade"],
            marks=data["marks"],
            contact_number=data["contact_number"],
            address=data["address"],
        )


class StudentDatabase:
    """In-memory repository for managing Student objects."""

    def __init__(self):
        self._students: List[Student] = []
        self._next_id = 1  # Simple auto-incrementing ID generator

    def add_student(self, student: Student) -> None:
        """Add a new student to the database."""
        student.student_id = self._next_id
        self._students.append(student)
        self._next_id += 1

    def get_all_students(self) -> List[Student]:
        """Return a list of all students."""
        return self._students.copy()

    def find_student_by_name(self, name: str) -> List[Student]:
        """Return a list of students whose name matches the given query (case-insensitive)."""
        name_lower = name.lower()
        return [s for s in self._students if name_lower in s.name.lower()]

    def update_student(
        self,
        student_id: int,
        **updated_fields,
    ) -> Optional[Student]:
        """
        Update fields of a student identified by student_id.
        Returns the updated student or None if not found.
        """
        for student in self._students:
            if student.student_id == student_id:
                for key, value in updated_fields.items():
                    if hasattr(student, key):
                        setattr(student, key, value)
                return student
        return None

    def delete_student(self, student_id: int) -> bool:
        """Remove a student from the database by ID."""
        for i, student in enumerate(self._students):
            if student.student_id == student_id:
                del self._students[i]
                return True
        return False


# ---------------------------------------------------------------------------
# Simple command-line interface (CLI) for interacting with the database
# ---------------------------------------------------------------------------

def display_menu() -> None:
    """Print the available commands."""
    print("\n--- Student Database Management ---")
    print("1. Add a new student")
    print("2. View all students")
    print("3. Search student by name")
    print("4. Update student information")
    print("5. Exit")
    print("-----------------------------------")


def add_student_interactive(db: StudentDatabase) -> None:
    """Collect student details from the user and add them to the DB."""
    print("\n--- Add New Student ---")
    try:
        student_id = db._next_id  # will be set inside the constructor
        name = input("Enter student name: ").strip()
        age = int(input("Enter age: ").strip())
        grade = input("Enter grade (e.g., A, B+, etc.): ").strip()
        marks_input = input(
            "Enter marks as JSON (e.g., {\"math\": 90, \"science\": 85}): "
        ).strip()
        marks = eval(marks_input) if marks_input else {}
        contact_number = input("Enter contact number: ").strip()
        address = input("Enter address: ").strip()

        student = Student(
            student_id=student_id,
            name=name,
            age=age,
            grade=grade,
            marks=marks,
            contact_number=contact_number,
            address=address,
        )
        db.add_student(student)
        print("✅ Student added successfully!")
    except Exception as e:
        print(f"❌ Error adding student: {e}")


def view_all_students_interactive(db: StudentDatabase) -> None:
    """Display all students in the database."""
    print("\n--- All Students ---")
    students = db.get_all_students()
    if not students:
        print("No students found.")
        return
    for s in students:
        print(f"ID: {s.student_id} | {s}")


def search_student_interactive(db: StudentDatabase) -> None:
    """Search for students by name and display results."""
    print("\n--- Search Student ---")
    query = input("Enter name to search: ").strip()
    results = db.find_student_by_name(query)
    if not results:
        print("No matching students found.")
        return
    for s in results:
        print(f"ID: {s.student_id} | {s}")


def update_student_interactive(db: StudentDatabase) -> None:
    """Update fields of an existing student."""
    print("\n--- Update Student ---")
    try:
        student_id = int(input("Enter the ID of the student to update: ").strip())
        student = db.update_student(
            student_id,
            # The fields below will be populated from user input if provided
        )
        if not student:
            print("Student not found.")
            return

        print("Leave a field blank to keep the current value.")
        name = input(f"Current name ('{student.name}'): ").strip()
        if name:
            student.name = name

        age_input = input(f"Current age ({student.age}): ").strip()
        if age_input.isdigit():
            student.age = int(age_input)

        grade = input(f"Current grade ('{student.grade}'): ").strip()
        if grade:
            student.grade = grade

        marks_input = input(
            f"Current marks ('{student.marks}'): "
        ).strip()
        if marks_input:
            try:
                student.marks = eval(marks_input) if marks_input else {}
            except Exception:
                print("Invalid JSON for marks keeping current marks.")
        contact_number = input(f"Current contact number ('{student.contact_number}'): ").strip()
        if contact_number:
            student.contact_number = contact_number

        address = input(f"Current address ('{student.address}'): ").strip()
        if address:
            student.address = address

        print("Student information updated successfully!")
    except Exception as e:
        print(f"Error updating student: {e}")


def main() -> None:
    """Run the interactive CLI menu."""
    db = StudentDatabase()
    while True:
        display_menu()
        choice = input("Select an option (1-5): ").strip()
        if choice == "1":
            add_student_interactive(db)
        elif choice == "2":
            view_all_students_interactive(db)
        elif choice == "3":
            search_student_interactive(db)
        elif choice == "4":
            update_student_interactive(db)
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid option, please choose a number between 1 and 5.")


if __name__ == "__main__":
    main()