# MD5 Dictionary Attack Results

## Experiment Setup

Algorithm:
MD5

Attack Type:
Dictionary Attack

Tool:
John the Ripper

Dataset:
1000 synthetic user passwords

Wordlist:
RockYou

---

## Results

Total Users:
1000

Recovered Passwords:
172

Remaining:
828

Success Rate:
17.2%

---

## Observations

The recovered passwords were primarily weak passwords:

- password
- password123
- admin123
- qwerty123
- 123456

The experiment demonstrates that unsalted fast hashing algorithms
such as MD5 provide insufficient protection against offline
password attacks.

Password reuse was also observed because identical passwords
generated identical hashes.
