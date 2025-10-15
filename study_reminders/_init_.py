"""
study_reminders package

A modular toolkit for generating and (simulated) sending of personalized study reminders.
"""
from .students import Students
from .students_manager import StudentsManager
from .reminder_generator import generate_reminder
from .reminder_sender import send_reminder
from .logger import log_reminder
from .scheduler import schedule_reminders
