# 🔐 Password Security Research Lab

### A Controlled Study of Password Cracking, Hashing Algorithms, and Defensive Security Practices

![Security](https://img.shields.io/badge/Domain-Cybersecurity-red)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![Kali Linux](https://img.shields.io/badge/Environment-Kali%20Linux-black)
![License](https://img.shields.io/badge/Usage-Educational-green)

---

## 📌 Overview

This project is an ethical cybersecurity research lab designed to study:

- Password hashing algorithms
- Dictionary-based password attacks
- Password strength impact
- Defensive password storage strategies

All experiments were performed using **synthetic user data inside an isolated laboratory environment**.

No real credentials were used.

---

# 🎯 Research Question

> How effective are different password hashing algorithms against controlled password cracking attempts?

Algorithms evaluated:

| Algorithm | Purpose |
|-|-|
| MD5 | Legacy comparison |
| SHA-256 | Fast cryptographic hashing |
| bcrypt | Adaptive password hashing |
| Argon2id | Modern memory-hard hashing |

---

# 🧪 Experimental Workflow

Synthetic Dataset
|
↓
Password Hash Generation
|
↓
Dictionary Attack Simulation
|
↓
Recovery Analysis
|
↓
Security Recommendations


---

# 📊 Key Findings

## Password Recovery Results

| Algorithm | Accounts Recovered |
|---|---:|
| MD5 | 172 / 1000 |
| SHA-256 | 172 / 1000 |
| bcrypt | 65 / 1000 |
| Argon2id | 61 / 1000 |

### Main Observation

Fast hashing algorithms allow attackers to test password guesses extremely quickly.

Adaptive hashing algorithms significantly increase attack difficulty.

---

# 🔍 Security Insights

## ❌ Avoid

- MD5 password storage
- SHA-256 password storage
- Plaintext passwords
- Password reuse


## ✅ Recommended

- Argon2id
- bcrypt
- Multi-factor authentication
- Rate limiting
- Strong password policies

---

# 🛠️ Technology Stack

## Development

- Python
- uv package manager

## Security Tools

- Kali Linux
- John the Ripper

## Libraries

- argon2-cffi
- bcrypt
- zxcvbn
- Faker
- pandas
- matplotlib

---

# 📂 Project Structure
password-security-research-lab/

├── data/
│ └── synthetic_users.csv

├── exports/
│ └── generated password hashes

├── scripts/
│ ├── generate_dataset.py
│ ├── benchmark_hashing.py
│ └── analyze_cracking.py

├── results/
│ └── experiment outputs

├── reports/
│ └── security assessment report

└── README.md


---

# 📈 Results Visualization

(Add generated charts here)

Example:
results/reports/
├── recovery_comparison.png
└── success_rate.png


---

# 🚀 Future Improvements

- GPU-based password auditing using Hashcat
- Password manager security analysis
- Passphrase entropy experiments
- Automated security report generation
- Web dashboard for password risk analysis

---

# ⚠️ Ethical Disclaimer

This project was developed strictly for educational cybersecurity research.

Testing was performed only against synthetic datasets in a controlled environment.

---

# 👨💻 Author

Denyel Chokey Namgyal

BSc Computer Science  
AI & Data Science | Cybersecurity Enthusiast

