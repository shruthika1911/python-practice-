# file_encryption.py

# Step 1: Take input
text = input("Enter text: ")
shift = 3

# Step 2: Encrypt
encrypted = ""

for char in text:
    encrypted += chr(ord(char) + shift)

print("Encrypted text:", encrypted)

# Step 3: Decrypt
decrypted = ""

for char in encrypted:
    decrypted += chr(ord(char) - shift)

print("Decrypted text:", decrypted)
