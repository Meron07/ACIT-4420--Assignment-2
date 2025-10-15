from setuptools import setup, find_packages

setup(
    name="study_reminders",
    version="0.1.0",
    description="Automate generating and (simulated) sending personalized study reminders",
    author="Your Name",
    packages=find_packages(),
    install_requires=[
        "schedule>=1.2.0",
    ],
    python_requires=">=3.8",
)
