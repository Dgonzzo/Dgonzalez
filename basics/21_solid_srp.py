'''From class'''
class User:
    # Correct
    def __init__(self, username, email):
        self.username = username
        self.email = email
    
    # Incorrect

    # def save_to_database(self):
    #     print('Saving in database')
    
    # def send_email(self, message):
    #     print(f'The email was sent with the message: {message}')

class EmailInterface:
    def send_email(self, email, message):
        print(f'The email was sent with the message:{message}')

class Database_Interface:
    def save_to_database(self, user: User):
        pass

''' From copilot'''
class UserRepository:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def get_user(self, username):
        for user in self.users:
            if user.username == username:
                return user
        return None

class UserService:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def register_user(self, username, email):
        user = User(username, email)
        self.user_repository.add_user(user)

    def find_user(self, username):
        return self.user_repository.get_user(username)

# Example usage
if __name__ == "__main__":
    user_repo = UserRepository()
    user_service = UserService(user_repo)

    user_service.register_user("john_doe", "john@example.com")
    user = user_service.find_user("john_doe")
    print(f"Found user: {user.username}, {user.email}")