import json
import os

class User:
    USERS_FILE = "users.txt"
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def register(self):
        users = self.load_users()
        if self.username in users:
            print("Username already exists!")
            return False
        users[self.username] = self.password
        self.save_users(users)
        print("Registration successful!")
        return True
    
    def login(self):
        users = self.load_users()
        if users.get(self.username) == self.password:
            print("Login successful!")
            return True
        print("Invalid username or password!")
        return False
    
    @staticmethod
    def load_users():
        if not os.path.exists(User.USERS_FILE):
            return {}
        with open(User.USERS_FILE, "r") as file:
            return json.load(file)
    
    @staticmethod
    def save_users(users):
        with open(User.USERS_FILE, "w") as file:
            json.dump(users, file)