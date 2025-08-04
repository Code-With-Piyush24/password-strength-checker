# 🔐 password-strength-checker

![Python](https://img.shields.io/badge/Python-3.x-blue)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

A simple and effective tool to assess the strength of passwords based on key security criteria such as length, character variety, and complexity. Great for users, developers, and educators looking to promote better password practices.

---

## 🚀 Features

- ✅ Checks password **length**
- ✅ Verifies **lowercase** and **uppercase** letters
- ✅ Detects **numbers** and **special characters**
- ✅ Provides a clear **strength score** and **recommendation**
- ✅ Customizable scoring logic
- ✅ Lightweight and fast
- 🛡️ Promotes secure password habits

---

## 📊 Password Strength Criteria

| Criteria                          | Points |
|----------------------------------|--------|
| Length (8+ characters)           | +1     |
| Contains lowercase letters       | +1     |
| Contains uppercase letters       | +1     |
| Contains numbers                 | +1     |
| Contains special characters      | +1     |

**Total Score: 0–5**

- **0–1**: 🔴 Very Weak  
- **2**: 🟠 Weak  
- **3**: 🟡 Moderate  
- **4**: 🟢 Strong  
- **5**: 🟢🟢 Very Strong  

---

## 💻 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/password-strength-checker.git
cd password-strength-checker

🖥️ Example Output
$ python password_checker.py
Enter your password: My$ecur3Pass
Password strength: Very Strong (Score: 5/5)


🗂️ Project Structure
password-strength-checker/
│
├── password_checker.py       # Main script for checking password strength
├── README.md                 # Project documentation
├── requirements.txt          # Dependencies (if any)
├── assets/                   # Screenshots or other assets
└── tests/                    # Unit tests (optional)
