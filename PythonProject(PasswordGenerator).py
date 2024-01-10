# Name:        module1
#
# Author:      Sourav Dutta
#
# Created:     02-12-2023
#------------------------------------------------------------------------------
# password Generator

# Import random module
import random

# Input statement
password_len = int(input("Enter Password length. "))

# Symbol & Character for Generate Password
password_data = "QWERTYUIOPASDFGHJKLZXCVBNM1234567890@$&%"

Password = "".join(random.sample(password_data,password_len))

print(f"Your Password is {Password} ")
