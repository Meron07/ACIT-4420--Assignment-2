import unittest
from study_reminders.students import Students

class TestStudents(unittest.TestCase):
    def test_add_and_remove(self):
        s = Students()
        s.add_student("Abel", "abel@example.com", "Python", "08:00")
        s.add_student("Henok", "henok@example.com", "Networks", "09:00")
        self.assertEqual(len(s.get_students()), 2)
        s.remove_student("Abel")
        self.assertEqual(len(s.get_students()), 1)
        self.assertEqual(s.get_students()[0]["name"], "Henok")

if __name__ == "__main__":
    unittest.main()
