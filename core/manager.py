class LMSManager:
    def __init__(self):
        self.users = {}

    def register_user(self, user):
        """Adds a user with basic error handling for duplicate IDs."""
        if user.user_id in self.users:
            raise ValueError(f"ID {user.user_id} already exists.")
        self.users[user.user_id] = user
        return True

    def get_user_count(self):
        return len(self.users)
