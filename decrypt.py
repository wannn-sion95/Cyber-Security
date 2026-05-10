import base64
from cryptography.fernet import Fernet

password = "720b6ad346f84cd483c60c7464dd95d4"

key = base64.b64encode(password.encode())

cipher = Fernet(key)

with open("flag.txt.en", "rb") as f:
    encrypted = f.read()

decrypted = cipher.decrypt(encrypted)

print(decrypted.decode())

# Or you can just: python3 ende.py -d flag.txt.en "your password(720b6ad346f84cd483c60c7464dd95d4)" for the passsword make without ""
