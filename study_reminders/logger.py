# logger.py
import datetime
from typing import Dict

LOG_FILE = "reminder_log.txt"

def log_reminder(student: Dict[str, str], reminder: str, status: str = "SENT") -> None:
    """Log a sent reminder with a timestamp to a file."""
    timestamp = datetime.datetime.now().isoformat(timespec="seconds")
    line = f"{timestamp} - Sent to {student['name']} <{student.get('email', student.get('contact_info', ''))}> [{status}]: {reminder}\n"
    with open(LOG_FILE, "a", encoding="utf-8") as log_file:
        log_file.write(line)
