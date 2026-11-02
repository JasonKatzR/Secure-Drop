import sys
from accCreation import userExist, createUser

def main():
    if not userExist():
        print("No users are registered with this client.")
        choice = input("Do you want to register a new user (y/n)? ").strip().lower()

        if (choice == "y"):
            if not createUser():
                sys.exit(1)
        else:
            print("Exiting SecureDrop.")
            sys.exit(0)


if __name__ == "__main__":
    main()