# students.py
from typing import List, Dict

class Students:
    """Class to manage a list of students' information."""

    def __init__(self):
        self.students: List[Dict[str, str]] = []

    def add_student(self, name: str, contact_info: str, course: str, preferred_time: str = "08:00") -> None:
        """Add a student with name, contact info, course, and preferred reminder time (HH:MM 24h)."""
        student = {
            "name": name,
            "contact_info": contact_info,
            "course": course,
            "preferred_time": preferred_time
        }
        self.students.append(student)

    def remove_student(self, name: str) -> None:
        """Remove a student by name."""
        self.students = [s for s in self.students if s["name"] != name]

    def get_students(self) -> List[Dict[str, str]]:
        """Retrieve the list of students."""
        return self.students
