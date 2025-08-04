password = input("Please enter your password: ")
score = 0

if len(password) >= 8:
    score += 1
    print("Your password has a minimum of 8 characters.")

if password.isdigit():
    score += 1
    print("Your password has at least 1 digit.")

if password.isupper():
    score += 1
    print("Your password has at least 1 uppercase.")

if password.islower():
    score += 1
    print("Your password has at least 1 lowercase.")
    
print(score)
