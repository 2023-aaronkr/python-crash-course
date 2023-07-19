# 8.1_functions.py
def greet_user():
    """Display a simple greeting."""
    print("Hello!")


greet_user()

# Arguments and parameters / 인수와 매개변수


def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")


greet_user('jesse')
