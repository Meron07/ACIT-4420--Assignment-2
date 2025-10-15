# main.py
"""
Entry point that integrates all modules to perform the automation:
- manage student data
- generate personalized reminders
- simulate sending
- log operations
- schedule daily execution
"""
import argparse
from study_reminders.students_manager import StudentsManager
from study_reminders.reminder_generator import generate_reminder
from study_reminders.reminder_sender import send_reminder
from study_reminders.logger import log_reminder
from study_reminders.scheduler import schedule_reminders

def main():
    parser = argparse.ArgumentParser(description="Automate personalized study reminders.")
    parser.add_argument("--students", default="students.json", help="Path to students JSON file")
    parser.add_argument("--list", action="store_true", help="List students and exit")
    parser.add_argument("--run-once", action="store_true", help="Trigger reminders immediately (for testing)")
    args = parser.parse_args()

    sm = StudentsManager(args.students)

    if args.list:
        sm.list_students()
        return

    if args.run_once:
        for student in sm.get_students():
            reminder = generate_reminder(student["name"], student["course"])
            status = send_reminder(student["email"], reminder)
            log_reminder(student, reminder, status=status)
        print("Run-once delivery completed.")
        return

    print("Scheduling daily reminders... (Ctrl+C to stop)")
    schedule_reminders(sm, generate_reminder, send_reminder, log_reminder, run_forever=True)
if __name__ == "__main__":
    try:
        main()  
    except KeyboardInterrupt:
        print("\nScheduler stopped manually by user. See ya")



