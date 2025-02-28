import secrets
import string
import random

def generate_seed(key):

    return sum(ord(char)for char in key) #Generates a seed based on ASCII values

def generate_password(key):
# Generates a password using imput from the user and having a random length password from 12-24
    user_seed = generate_seed(key)
    secrets_gen = secrets.SystemRandom(user_seed)

    length = random.randint(12,24) #picks a number between 12 and 24 for the length of the password
    alphabet = string.ascii_letters + string.digits + string.punctuation # all the these types of characters can be apart of the password

    #makes sure it has at least one of each type of character ex. A 1 and $

    while True:
        password = ''.join(secrets_gen.choice(alphabet)for _ in range(length))
        if (any(c.islower() for c in password) and
            any(c.isupper() for c in password) and
            any(c.isdigit() for c in password) and
            any(c in string.punctuation for c in password)):
            break  # Ensure it meets set rules above


    return password

def main():
    while True:
        key = input("Enter a key to generate your password: ").replace(" ","") #removes spaces from key

        if not key: #checks if input is empty
            print ("Error: please input a valid key to generate a unique password")
            continue # asks for the input again

        password = generate_password(key) # creates a password using the method
        print ("Generated Password: " + password)

    
        while True:
            decision = input("Do you want this password? yes or no? ").replace(" ", "").lower() # checks if the user wants this password or to make a different password

                    # Check if the decision is valid
            if decision not in ('yes', 'no'):
                print("Please type 'yes' or 'no'.")
                continue  # Re-run the prompt if input is invalid

                # Check the user's decision
            if decision == 'yes':
                print("Password saved!")
                break  # Exit the loop when 'yes' is entered
            if decision == 'no':    
                print("Generating a new password...\n")
                break

        if decision == 'yes':     # should only run if decision is 'yes'    
            while True: 
                review = input("Do you want to see the password again? yes or no: ").replace(" ", "").lower() #asks if the user wants to look at the password again
                if review == 'yes':
                    print("Saved password: " + password)
                    return
                elif review == 'no':
                    print("Exiting Program.")
                    return #Exits the program
                else:
                    print("Invalid input please type 'yes' or 'no'.")
                    continue #makes sure only yes and no can be the input

if __name__ == "__main__":
    main() #makes code more modular helps with running order