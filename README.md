# 🔐 password-strength-checker

A simple and effective tool to assess the strength of passwords based on key security criteria such as length, presence of uppercase and lowercase letters, numbers, and special characters.

## 🚀 Features

- Checks password **length**
- Detects **uppercase** and **lowercase** letters
- Validates presence of **numbers**
- Validates presence of **special characters**
- Provides a **strength score** and **feedback**

## 📊 Password Strength Criteria

| Criteria                          | Points |
|----------------------------------|--------|
| Length (8+ characters)           | +1     |
| Contains lowercase letters       | +1     |
| Contains uppercase letters       | +1     |
| Contains numbers                 | +1     |
| Contains special characters      | +1     |

**Total Score: 0–5**

- 0–1: Very Weak  
- 2: Weak  
- 3: Moderate  
- 4: Strong  
- 5: Very Strong  

## 💻 Usage

You can use this tool as:

- A command-line utility
- A web-based form (optional if you build a frontend)
- A module in a larger authentication system

### Example (CLI)

```bash
$ python password_checker.py
Enter your password: My$ecur3Pass
Password strength: Very Strong (Score: 5/5)
