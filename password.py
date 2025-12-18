import secrets
import string

def generate_password(length=12):
    """Generates a secure random password."""
    if length < 8:
        length = 8
    
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return password

if __name__ == "__main__":
    print(f"Generated Password: {generate_password()}")