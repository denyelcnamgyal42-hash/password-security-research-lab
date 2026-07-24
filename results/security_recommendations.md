# Password Security Recommendations


## Hashing Algorithm

Avoid:

- MD5
- SHA-256 for password storage


Recommended:

- Argon2id
- bcrypt


## Password Policy

Recommended minimum:

- 12+ characters
- Allow passphrases
- Block common passwords
- Avoid forced periodic password changes


## Authentication Controls

Implement:

- MFA
- Account lockout
- Rate limiting
- Login monitoring


## Storage Practices

Passwords should:

- Never be stored plaintext
- Use unique salts
- Use adaptive hashing algorithms
- Use appropriate work factors
