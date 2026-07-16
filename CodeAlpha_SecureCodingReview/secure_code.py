"""
CodeAlpha Cyber Security Internship
Task 3: Secure Coding Review
Author: Abdullah Saeed
Secure Login System
"""
import bcrypt
print("=" * 60)
print("        Secure Login System")
print("=" * 60)
# Secure username
USERNAME = "admin"

# Password hashing
stored_password = bcrypt.hashpw(
    "admin123".encode(),
    bcrypt.gensalt()
)

username = input("Enter Username: ")
password = input("Enter Password: ")

# Secure verification
if (
    username == USERNAME and
    bcrypt.checkpw(password.encode(), stored_password)
):
    print("\nLogin Successful!")
    print("Welcome Administrator.")
else:
    print("\nLogin Failed!")
    print("Invalid Username or Password.")
print("\nProgram Finished.")