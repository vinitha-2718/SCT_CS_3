import re


def assess_password_strength(password):
    """
    Assesses the strength of a password and provides feedback.

    Args:
        password (str): The password to be assessed.

    Returns:
        dict: A dictionary containing the score, strength rating, and feedback.
    """
    score = 0
    feedback = []

    # Criteria Checks
    length_min = 8
    has_uppercase = bool(re.search(r'[A-Z]', password))
    has_lowercase = bool(re.search(r'[a-z]', password))
    has_number = bool(re.search(r'\d', password))
    has_special_char = bool(re.search(r'[\W_]', password))

    # Scoring Logic
    if len(password) >= length_min:
        score += 1
    else:
        feedback.append(
            f"Password must be at least {length_min} characters long.")

    if has_uppercase:
        score += 1
    else:
        feedback.append("Include at least one uppercase letter.")

    if has_lowercase:
        score += 1
    else:
        feedback.append("Include at least one lowercase letter.")

    if has_number:
        score += 1
    else:
        feedback.append("Include at least one number.")

    if has_special_char:
        score += 1
    else:
        feedback.append("Include at least one special character.")

    # Determine Strength Rating
    if score == 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Medium"
    else:
        strength = "Weak"

    return {
        "score": score,
        "strength": strength,
        "feedback": feedback
    }


# Main function to run the tool
if __name__ == "__main__":
    user_password = input("Enter a password to assess its strength: ")
    result = assess_password_strength(user_password)

    print("\n--- Password Strength Assessment ---")
    print(f"Strength: {result['strength']}")
    print(f"Score: {result['score']}/5")

    if result['feedback']:
        print("\nSuggestions for improvement:")
        for suggestion in result['feedback']:
            print(f"- {suggestion}")
    else:
        print("\nThis password is very strong! 👍")
