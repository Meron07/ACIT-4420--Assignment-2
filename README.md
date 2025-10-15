# ACIT-4420--Assignment-2
# study_reminders

A modular Python package that automates generating and (simulated) sending personalized study reminders.
The project demonstrates practical automation, modular programming and files handling techniques by using python.

## Overview
    The study_reminders package performs five automated tasks:   
        -Manage student information (name, email, course, preferred time).    
        -Generate personalized study reminders for each student.    
        -Simulate sending reminders (printed to console).    
        -Log every reminder sent with timestamps.    
        -Schedule daily reminders automatically based on each student’s preferred time.
    It shows how task automation and logging can enhance time management in academic or professional environments.
    
## Package structure
    study_reminders/
    │
    ├── study_reminders/
    │   ├── __init__.py
    │   ├── students.py
    │   ├── reminder_generator.py
    │   ├── reminder_sender.py
    │   ├── logger.py
    │   ├── students_manager.py
    │   └── scheduler.py
    │
    ├── students.json
    ├── main.py
    ├── setup.py
    ├── README.md
    │
    ├── tests/
    │   ├── test_students.py
    │   └── test_modules.py
    └── test.py

## Features
    ✅ Manage students dynamically (JSON-based data).
    ✅ Generate personalized course reminders.
    ✅ Simulate delivery with console output.
    ✅ Log all activity with timestamps in reminder_log.txt.
    ✅ Schedule daily reminders using the schedule library.
    ✅ Modular design — reusable and independently testable components.

## Usage
```bash
pip install -e .
python main.py --run-once

## To test follow this 
-pwd   "dobbel check where is the folder located"
-install this liibriers 
    pip schedule                 "You must have the schedule library for the planning to work"
    pip install -e .             "run this in the project folder"
    python test.py               "to test for everything working well"
    python main.py --run-once    "to send all at the same time"
    python main.py --list        "to list all students"
    python main.py               "to activate daily"
    cat reminder_log.txt         "After you run the script, and then you ll see all times and who received which reminders."
```



