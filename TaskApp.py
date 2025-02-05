import json
import os
from User import User
from TaskManager import TaskManager
from Task import Task

class TaskApp:
    @staticmethod
    def main_menu():
        while True:
            print("\nTask Manager")
            print("1. Register")
            print("2. Login")
            print("3. Exit")
            choice = input("Enter choice: ")
            
            if choice == "1":
                username = input("Enter username: ")
                password = input("Enter password: ")
                user = User(username, password)
                user.register()
            elif choice == "2":
                username = input("Enter username: ")
                password = input("Enter password: ")
                user = User(username, password)
                if user.login():
                    task_manager = TaskManager(username)
                    TaskApp.task_menu(task_manager)
            elif choice == "3":
                break
            else:
                print("Invalid choice!")
    
    @staticmethod
    def task_menu(task_manager):
        while True:
            print("\nTask Menu")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Mark Task Completed")
            print("4. Delete Task")
            print("5. Logout")
            choice = input("Enter choice: ")
            
            if choice == "1":
                description = input("Enter task description: ")
                task_manager.add_task(description)
            elif choice == "2":
                task_manager.view_tasks()
            elif choice == "3":
                task_id = int(input("Enter task ID to mark completed: "))
                task_manager.mark_completed(task_id)
            elif choice == "4":
                task_id = int(input("Enter task ID to delete: "))
                task_manager.delete_task(task_id)
            elif choice == "5":
                break
            else:
                print("Invalid choice!")

if __name__ == "__main__":
    TaskApp.main_menu()