from models import User

def add_user(system, user_detail):
    name, gender, age = user_detail.split(",")
    system.users[name.strip()] = User(name.strip(), gender.strip(), int(age.strip()))

def update_user_location(system, username, location):
    if username in system.users:
        system.users[username].update_location(location)
    else:
        print(f"User {username} not found!")
