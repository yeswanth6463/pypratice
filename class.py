import re

def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) + shift - shift_amount) % 26 + shift_amount)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

def is_valid_password(password):
    if (len(password) >= 8 and
        re.search(r'[A-Z]', password) and
        re.search(r'[0-9]', password) and
        re.search(r'[\W_]', password)):
        return True
    return False

def main():
    username = input("Enter username: ")
    while True:
        password = input("Enter password: ")
        if is_valid_password(password):
            break
        else:
            print("Password must be at least 8 characters long and contain at least one uppercase letter, one number, and one special character.")

    shift = 3  # You can change the shift value as needed

    encrypted_password = caesar_cipher_encrypt(password, shift)
    print(f"Encrypted Password: {encrypted_password}")

    entered_password = input("Re-enter password to verify: ")
    decrypted_password = caesar_cipher_decrypt(encrypted_password, shift)

    if entered_password == decrypted_password:
        print("Password verified successfully!")
    else:
        print("Password verification failed!")

if __name__ == "__main__":
    main()
