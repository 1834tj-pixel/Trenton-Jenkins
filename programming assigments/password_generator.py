import random
import string
import os


def main():
    print("Welcome to the Incredible Password Generator!")

    try:
        num_passwords = int(input("How many random passwords would you like to generate? "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    passwords = []

    for i in range(num_passwords):
        print(f"\n--- Generating password #{i + 1} ---")
        try:
            length = int(input("How many characters would you like in your password? "))
        except ValueError:
            print("Invalid input. Skipping this password.")
            continue

        # Character options
        lower = input("Include lowercase letters? (Yes or No): ").strip().lower()
        upper = input("Include uppercase letters? (Yes or No): ").strip().lower()
        numbers = input("Include numbers? (Yes or No): ").strip().lower()
        special = input("Include special characters? (Yes or No): ").strip().lower()

        chars = ""
        if lower in ["", "yes", "y"]:
            chars += string.ascii_lowercase
        if upper in ["", "yes", "y"]:
            chars += string.ascii_uppercase
        if numbers in ["", "yes", "y"]:
            chars += string.digits
        if special in ["", "yes", "y"]:
            chars += string.punctuation

        if not chars:
            print("No character sets selected. Skipping this password.")
            continue

        password = ''.join(random.choice(chars) for _ in range(length))
        passwords.append(password)
        print(f"Your new password is: {password}")

    save = input("\nWould you like to save all passwords to a file? (Yes or No): ").strip().lower()
    if save in ["", "yes", "y"]:

        os.makedirs("text_files", exist_ok=True)
        with open("text_files/random_passwords.txt", "w") as file:
            for pwd in passwords:
                file.write(pwd + "\n")
        print("Passwords saved to text_files/random_passwords.txt")

    print("\nThis password generator app will close...")


if __name__ == "__main__":
    main()
