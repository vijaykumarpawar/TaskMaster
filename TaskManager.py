import json
import os

class TaskManager:
    def __init__(self, username):
        self.filename = f"{username}_tasks.json"
        self.tasks = self.load_tasks()
    
    def load_tasks(self):
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, "r") as file:
            return [Task.from_dict(task) for task in json.load(file)]
    
    def save_tasks(self):
        with open(self.filename, "w") as file:
            json.dump([task.to_dict() for task in self.tasks], file)
    
    def add_task(self, description):
        task_id = len(self.tasks) + 1
        self.tasks.append(Task(task_id, description))
        self.save_tasks()
        print("Task added successfully!")
    
    def view_tasks(self):
        if not self.tasks:
            print("No tasks available!")
            return
        for task in self.tasks:
            status = "Completed" if task.is_completed else "Pending"
            print(f"[{task.task_id}] {task.description} - {status}")
    
    def mark_completed(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                task.is_completed = True
                self.save_tasks()
                print("Task marked as completed!")
                return
        print("Task not found!")
    
    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task.task_id != task_id]
        self.save_tasks()
        print("Task deleted successfully!")


