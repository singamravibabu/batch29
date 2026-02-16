import random

lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = lowercase.upper()
deci_chars = "0123456789"
special_chars = "!@#$%^&*()-_=+[]{}|;':,./<>?"

all_chars = lowercase + uppercase + deci_chars + special_chars

def generate_password(length=12):

	if length < 6:
		return "Password must contain at least 6 characters"

	password = random.choice(lowercase)
	password += random.choice(uppercase)
	password += random.choice(deci_chars)
	password += random.choice(special_chars)

	for _ in range(length - 4):
		password += random.choice(all_chars)

	password_list = list(password)
	random.shuffle(password_list)

	password = "".join(password_list)
	return password

length = int(input("Enter password length (minimum 6 characters): "))
print("Password:", generate_password(length))