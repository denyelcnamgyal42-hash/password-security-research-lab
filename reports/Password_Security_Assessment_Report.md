# Password Security Assessment Report

## Executive Summary

This report documents a controlled password security assessment performed using synthetic user data.

The objective was to evaluate the security impact of different password storage algorithms and demonstrate the importance of secure password hashing practices.

The assessment compared:

- MD5
- SHA-256
- bcrypt
- Argon2id

Dictionary-based password recovery attacks were performed using John the Ripper in an isolated laboratory environment.

---

# 1. Objectives

The objectives of this research were:

- Generate realistic synthetic password datasets
- Evaluate different password hashing algorithms
- Measure resistance against dictionary attacks
- Analyze password policy effectiveness
- Recommend secure password storage practices

---

# 2. Laboratory Environment

## Operating System

Kali Linux

## Tools

- John the Ripper
- Python
- uv package manager

## Dataset

Synthetic dataset:

- 1000 user accounts
- No real credentials used

Password categories:

- Weak passwords
- Medium passwords
- Strong passwords
- Passphrases
- Random passwords

---

# 3. Hashing Algorithms Tested

## MD5

Legacy hashing algorithm.

Characteristics:

- Extremely fast
- Not suitable for password storage
- Vulnerable to high-speed guessing attacks

---

## SHA-256

Cryptographic hash function.

Although secure for integrity checking, it is unsuitable for password storage because it is too fast.

---

## bcrypt

Adaptive password hashing algorithm.

Features:

- Configurable cost factor
- Salted hashes
- Designed for password storage

---

## Argon2id

Modern password hashing recommendation.

Features:

- Memory hardness
- Configurable computational cost
- Resistance against GPU attacks

---

# 4. Attack Methodology

A dictionary attack was performed using common password lists.

Workflow:

Password Candidates
|
↓
Hash Generation
|
↓
Hash Comparison
|
↓
Recovered Credentials


Only synthetic credentials were used.

---

# 5. Results

| Algorithm | Recovered Accounts |
|------------|-------------------|
| MD5 | 172 |
| SHA-256 | 172 |
| bcrypt | 65 |
| Argon2id | 61 |

---

# 6. Analysis

Fast hashing algorithms showed poor resistance because attackers can test large numbers of guesses quickly.

MD5 and SHA-256 allowed recovery of many weak passwords.

bcrypt and Argon2id significantly reduced attack effectiveness due to intentional computational cost.

However, weak passwords remained vulnerable regardless of hashing algorithm.

---

# 7. Recommendations

## Password Storage

Recommended:

- Argon2id
- bcrypt

Avoid:

- MD5
- SHA-256
- Plaintext storage


## Password Policies

Recommended:

- Minimum length of 12 characters
- Support passphrases
- Block commonly breached passwords
- Avoid password reuse


## Additional Security Controls

Implement:

- Multi-factor authentication
- Rate limiting
- Account lockout protection
- Login monitoring

---

# 8. Conclusion

This experiment demonstrates that secure password storage requires both:

1. Strong password hashing algorithms
2. Strong user password practices

Modern systems should use memory-hard algorithms such as Argon2id combined with effective authentication controls.
