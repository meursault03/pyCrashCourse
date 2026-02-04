from pathlib import Path
import json

def get_stored_username(path):
    """Obtém o nome de usuário armazenado, se disponível."""
    if path.exists():
        contents = path.read_text()
        user_info = json.loads(contents)
        return user_info
    return None


def get_new_username(path):
    """Solicita um novo nome de usuário e o armazena."""

    username = input("What is your name? ")
    city = input("Where do you live ")
    favorite_game = input("What is your favorite game? ")
    user_info = {"username": username, 'city': city, 'favorite game': favorite_game}
    contents = json.dumps(user_info)
    path.write_text(contents)
    return user_info


def greet_user():
    """Sauda o usuário pelo nome."""
    path = Path('user_info.json')
    user_info = get_stored_username(path)
    if path.exists():
        check = input(f"Is your username correct? {user_info['username'].title()} y/n ")

        if check == "n":
            user_info = get_new_username(path)
            print(f"We'll remember you when you come back, {user_info['username'].title()}")
        else:
            print("Welcome back, your information is: ")
            for key, value in user_info.items():
                print(f"{key.title()}: {value.title()}")
    else:
        user_info = get_new_username(path)
        print(f"{user_info['username'].title()} your data was stored in our database.")



greet_user()