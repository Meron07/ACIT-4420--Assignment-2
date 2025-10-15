# students_manager.py
import json
from typing import List, Dict

class StudentsManager:
    """Class to manage student data with JSON storage."""

    def __init__(self, file_path: str = "students.json"):
        self.file_path = file_path
        self.students: List[Dict[str, str]] = self.load_students()

    def load_students(self) -> List[Dict[str, str]]:
        """Load student data from a JSON file."""
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            return [
                {"name": "Abel", "email": "abel@example.com", "course": "Computer Science", "preferred_time": "08:00"},
                {"name": "Henok", "email": "henok@example.com", "course": "Mathematics", "preferred_time": "09:00"},
                {"name": "Charlie", "email": "charlie@example.com", "course": "Physics", "preferred_time": "07:30"},
            ]

    def add_student(self, name: str, email: str, course: str, preferred_time: str = "08:00") -> None:
        """Add a student and save to the JSON file."""
        student = {
            "name": name,
            "email": email,
            "course": course,
            "preferred_time": preferred_time,
        }
        self.students.append(student)
        self.save_students()

    def remove_student(self, name: str) -> None:
        """Remove a student by name and update the JSON file."""
        self.students = [s for s in self.students if s["name"] != name]
        self.save_students()

    def save_students(self) -> None:
        """Save student data to the JSON file."""
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(self.students, file, indent=4)

    def get_students(self):
        """Retrieve the list of students."""
        return self.students

    def list_students(self) -> None:
        """Print all students (for manual inspection)."""
        for student in self.students:
            print(f"Name: {student['name']}, Email: {student['email']}, Course: {student['course']}, Preferred Time: {student['preferred_time']}")
