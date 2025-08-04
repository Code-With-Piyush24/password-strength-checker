# 🔐 Simple Password Strength Checker
# This is a basic tool to check how strong a password is

def check_password_strength(password):
    """
    This function checks how strong a password is
    Returns a score from 0 to 5
    """
    
    score = 0
    feedback = []
    
    # ✅ Check 1: Length (at least 8 characters)
    if len(password) >= 8:
        score += 1
        feedback.append("✅ Good length 👍")
    else:
        feedback.append("❌ Should be at least 8 characters 📏")
    
    # 🔠 Check 2: Has uppercase letters
    has_upper = any(letter.isupper() for letter in password)
    if has_upper:
        score += 1
        feedback.append("✅ Has uppercase letters 🔠")
    else:
        feedback.append("❌ Add some uppercase letters 🔡 ➕")

    # 🔡 Check 3: Has lowercase letters
    has_lower = any(letter.islower() for letter in password)
    if has_lower:
        score += 1
        feedback.append("✅ Has lowercase letters 🔡")
    else:
        feedback.append("❌ Add some lowercase letters 🔠 ➕")
    
    # 🔢 Check 4: Has numbers
    has_number = any(letter.isdigit() for letter in password)
    if has_number:
        score += 1
        feedback.append("✅ Has numbers 🔢")
    else:
        feedback.append("❌ Add some numbers 0️⃣1️⃣2️⃣")
    
    # 🔣 Check 5: Has special characters
    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    has_special = any(letter in special_chars for letter in password)
    if has_special:
        score += 1
        feedback.append("✅ Has special characters 🔣")
    else:
        feedback.append("❌ Add some special characters like !@#$% ✨")
    
    return score, feedback

def get_strength_level(score):
    """Convert score to strength level"""
    if score <= 1:
        return "🔴 Very Weak"
    elif score == 2:
        return "🟠 Weak"
    elif score == 3:
        return "🟡 Medium"
    elif score == 4:
        return "🟢 Strong"
    else:
        return "💪 Very Strong"

# 🧪 Main program
if __name__ == "__main__":
    print("🔒 === Password Strength Checker ===")
    print("This tool checks how strong your password is 💡")
    print("It looks at length, uppercase, lowercase, numbers, and special characters 🔍")
    print()
    
    # Get password from user
    password = input("Enter your password: ")
    
    # Check the password
    score, feedback = check_password_strength(password)
    strength = get_strength_level(score)
    
    # Show results
    print("\n📊 === Results ===")
    print(f"Password: {'*' * len(password)}")  # Hide the actual password
    print(f"Score: {score}/5 🌟")
    print(f"Strength: {strength}")
    print("\n📝 Feedback:")
    
    for item in feedback:
        print(f"  {item}")
    
    # Give suggestions
    print("\n💡 === Suggestions ===")
    if score < 5:
        print("To make your password stronger 💪:")
        if len(password) < 8:
            print("- ➕ Make it longer (at least 8 characters)")
        if not any(c.isupper() for c in password):
            print("- ➕ Add uppercase letters (A-Z)")
        if not any(c.islower() for c in password):
            print("- ➕ Add lowercase letters (a-z)")
        if not any(c.isdigit() for c in password):
            print("- ➕ Add numbers (0-9)")
        if not any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password):
            print("- ➕ Add special characters (!@#$%^&*)")
    else:
        print("🎉 Great job! Your password is very strong.")
