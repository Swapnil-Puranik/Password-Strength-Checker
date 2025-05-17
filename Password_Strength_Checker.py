import string

#Step 1: Ask the user for a password
password = input("Enter a password: ")

#Step 2: Define the strength checks
errors = []
score = 0

# Length check
if len(password) >= 8:
    score += 2
else:
    errors.append("at least 8 characters")

# Uppercase check
flag=False
for c in password:
    if c.isupper() and flag==False:
        score += 2
        flag=True
        break
if flag==False:
    errors.append("at least one UpperCase letter")

# Lowercase check
flag=False
for c in password:
    if c.islower() and flag==False:
        score += 2
        flag=True
        break
if flag==False:
    errors.append("at least one lowercase letter")

# Digit check
if any(c.isdigit() for c in password):
    score += 2
else:
    errors.append("at least one digit")

# Special character check
special_chars = ["@","#","$","%","&","*","^","!"]
if any(c in special_chars for c in password):
    score += 2
else:
    errors.append("at least one special character (e.g. @, #, $)")

# Step 3: Output result
if not errors:
    print("Your password is strong!")
else:
    print("Your password needs:", ", ".join(errors) + ".")

#Bonus: Strength meter
print("Password Strength Score: ",score,"/10")
if score == 10:
    print("Excellent!")
elif score >= 6:
    print("Not bad, but could be stronger.")
else:
    print("Very weak. Consider improving your password.")
