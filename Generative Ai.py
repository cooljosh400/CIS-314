import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    while True:
        user_key = input("Please enter a key (no spaces allowed): ").strip()
        if ' ' in user_key:
            print("Invalid key. The key cannot contain spaces.")
        else:
            break
    
    length = random.randint(8, 16)
    password = generate_password(length)
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()