from scripts.hash_generator import (
    hash_md5,
    hash_sha256,
    hash_bcrypt,
    hash_argon2id,
)

password = "password123"

print("Password:", password)
print()

print("MD5:")
print(hash_md5(password))
print()

print("SHA256:")
print(hash_sha256(password))
print()

print("bcrypt:")
print(hash_bcrypt(password))
print()

print("Argon2id:")
print(hash_argon2id(password))