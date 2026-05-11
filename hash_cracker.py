import hashlib

with open("dictionary.txt", "r", encoding="utf-8") as f:
    pos_pw_list = [line.strip() for line in f]

with open("hash.bin", "rb") as f:
    target = f.read()

for pw in pos_pw_list:
    h = hashlib.md5(pw.encode()).digest()

    if h == target:
        print("Password:", pw)
        break
else:
    print("Password not found!")
