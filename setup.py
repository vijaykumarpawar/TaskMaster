from setuptools import setup, find_packages

setup(
    name="first_project",
    version="0.1",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "first_project_run = TaskApp:TaskApp.main_menu"
        ]
    }
)
