import json
import os

class Task:
    def __init__(self, task_id, description, is_completed=False):
        self.task_id = task_id
        self.description = description
        self.is_completed = is_completed
    
    def to_dict(self):
        return {"task_id": self.task_id, "description": self.description, "is_completed": self.is_completed}
    
    @staticmethod
    def from_dict(data):
        return Task(data["task_id"], data["description"], data["is_completed"])