# reminder_sender.py
def send_reminder(email: str, reminder: str) -> str:
    """
    Simulate sending a reminder to the specified email.
    Returns a short delivery status string for logging/tests.
    """
    if not email:
        raise ValueError("Email address is missing")
    message = f"Sending reminder to {email}: {reminder}"
    print(message)
    return "SENT"
