import os, json, hashlib

DATA_DIR = "data"
USERS_FILE = os.path.join(DATA_DIR, "users.json")
USER_DATA_DIR = os.path.join(DATA_DIR, "user_data")

os.makedirs(USER_DATA_DIR, exist_ok=True)

class User:
    def __init__(self, username, password_hash):
        self.username = username
        self.password_hash = password_hash

    def check_password(self, password):
        return self.password_hash == hashlib.sha256(password.encode()).hexdigest()

class UserManager:
    def __init__(self):
        self.users = self.load_users()

    def load_users(self):
        if not os.path.exists(USERS_FILE):
            return []
        with open(USERS_FILE, "r") as f:
            data = json.load(f)
            return [User(u["username"], u["password_hash"]) for u in data]

    def save_users(self):
        with open(USERS_FILE, "w") as f:
            json.dump([{"username": u.username, "password_hash": u.password_hash} for u in self.users], f, indent=4)

    def add_user(self, username, password):
        if any(u.username == username for u in self.users):
            return False
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        self.users.append(User(username, password_hash))
        self.save_users()

        # Create empty data file for user
        with open(os.path.join(USER_DATA_DIR, f"{username}.json"), "w") as f:
            json.dump({"companies": [], "invoices": []}, f, indent=4)

        return True

    def get_user(self, username):
        for user in self.users:
            if user.username == username:
                return user
        return None
