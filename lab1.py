# -------------------------------------------------------- #
# Lab 1: Getting Started with Python
# CIS 103: Introduction to Programming
# Instructor: Md Ali
# Student Name: Annie Yung
# Date: 9/6/2024


# Description:
# This script prints a greeting message to the user.
# --------------------------------------------------------
# The following line of code prints a greeting message #

print("Hello, welcome to CIS 103!")

# This script prints a personalized greeting message
# and demonstrates the use of variables and basic data types. 
# --------------------------------------------------------

# Get the user's name (string) and age (integer)

name = input("Enter your name:")
age = int(input("Enter your age:"))

# Calculate the year the user was born #
current_year=2024
birth_year=current_year - age

#Print a personalized greeting message #
print(f"Hello, {name}! You were born in {birth_year}.")

