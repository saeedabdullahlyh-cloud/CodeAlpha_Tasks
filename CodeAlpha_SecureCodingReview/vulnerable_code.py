"""
CodeAlpha Cyber Security Internship
Task 3: Secure Coding Review

Author: Abdullah Saeed

Vulnerable Login System
(For Educational Purposes Only)
"""

# Hardcoded credentials (Vulnerability)
USERNAME = "admin"
PASSWORD = "admin123"

print("=" * 60)
print("      Vulnerable Login System")
print("=" * 60)

username = input("Enter Username: ")
password = input("Enter Password: ")

# Plain text password comparison (Vulnerability)
if username == USERNAME and password == PASSWORD:
    print("\nLogin Successful!")
    print("Welcome Administrator.")
else:
    print("\nLogin Failed!")
    print("Username or Password is Incorrect.")

print("\nProgram Finished.")