import unittest
from study_reminders.reminder_generator import generate_reminder
from study_reminders.reminder_sender import send_reminder
from study_reminders.logger import log_reminder
from study_reminders.students_manager import StudentsManager
import os

class TestModules(unittest.TestCase):
    def test_generate_reminder(self):
        r = generate_reminder("Abel", "Python")
        self.assertIn("Abel", r)
        self.assertIn("Python", r)

    def test_send_and_log(self):
        student = {"name": "Abel", "email": "Abel@example.com", "course": "Python", "preferred_time": "08:00"}
        reminder = generate_reminder(student["name"], student["course"])
        status = send_reminder(student["email"], reminder)
        self.assertEqual(status, "SENT")
        log_reminder(student, reminder, status=status)
        self.assertTrue(os.path.exists("reminder_log.txt"))

    def test_students_manager_load(self):
        sm = StudentsManager(file_path="students.json")
        students = sm.get_students()
        self.assertGreaterEqual(len(students), 1)
        self.assertIn("name", students[0])
        self.assertIn("email", students[0])

if __name__ == "__main__":
    unittest.main()
