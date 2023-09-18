import hashlib

str = "064799"

result = hashlib.sha256(str.encode())
print(result.hexdigest().upper())