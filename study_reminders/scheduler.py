# scheduler.py
from typing import Callable
from functools import partial
import time

try:
    import schedule
except ImportError:
    schedule = None

def schedule_reminders(students_manager, reminder_generator: Callable, reminder_sender: Callable, logger: Callable, run_forever: bool = True):
    """
    Schedule reminder delivery for each student at their preferred time.
    If run_forever is False, it will run pending tasks once (useful for testing).
    """
    if schedule is None:
        raise RuntimeError("The 'schedule' package is required. Install it with 'pip install schedule'.")

    for student in students_manager.get_students():
        reminder = reminder_generator(student["name"], student["course"])
        job_fn = partial(_deliver, student, reminder, reminder_sender, logger)
        schedule.every().day.at(student["preferred_time"]).do(job_fn)

    if not run_forever:
        schedule.run_pending()
        return

    while True:
        schedule.run_pending()
        time.sleep(60)

def _deliver(student, reminder, sender, logger):
    status = sender(student.get("email") or student.get("contact_info"), reminder)
    logger(student, reminder, status=status)
