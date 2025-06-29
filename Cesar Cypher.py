

 #encryption
try:
    def caesar_encrypt(message,shiftno):
        new_string=""
        for char in message:
        #if char is a number then ignore
            if char.isdigit():
                continue
        #if char is a space then ignore
            elif char.isspace():
                continue
        #if char is a special character then ignore
            elif not char.isalnum():
                continue
        #if char is a letter then encrypt
            else:
                if char.isupper():
            # range of upper is 65-90
                    new_char = (ord(char) - 65 + shiftno) % 26 + 65
                    #ord changes the character to its ASCII value
                    new_string += chr(new_char)
                    #chr changes the ASCII value to its character
                elif char.islower():
            # range of lower is 97-122
                    new_char = (ord(char) - 97 + shiftno) % 26 + 97
                    new_string += chr(new_char)
        return new_string
    def caesar_decrypt(message,shiftno):
        new_string=""
        for char in message:
        #if char is a number then ignore
            if char.isdigit():
                continue
        #if char is a space then ignore
            elif char.isspace():
                continue
        #if char is a special character then ignore
            elif not char.isalnum():
                continue
        #if char is a letter then encrypt
            else:
                if char.isupper():
            # range of upper is 65-90
                    new_char = (ord(char) - 65 - shiftno) % 26 + 65
                    #ord changes the character to its ASCII value
                    new_string += chr(new_char)
                    #chr changes the ASCII value to its character
                elif char.islower():
            # range of lower is 97-122
                    new_char = (ord(char) - 97 - shiftno) % 26 + 97
                    new_string += chr(new_char)
        return new_string
    choice = input("Do you want to encrypt or decrypt a message? (e/d): ").lower()
    while choice in ('e', 'd'):
        if choice == 'e':
            message = input("Enter the message to encrypt: ")
            shiftno = int(input("Enter the shift number (1-25): "))
            encrypted_message = caesar_encrypt(message, shiftno)
            print(f"Encrypted message: {encrypted_message}")
        elif choice == 'd':
            message = input("Enter the message to decrypt: ")
            shiftno = int(input("Enter the shift number (1-25): "))
            decrypted_message = caesar_decrypt(message, shiftno)
            print(f"Decrypted message: {decrypted_message}")
        else:
            print("Invalid choice. Please enter 'e' to encrypt or 'd' to decrypt.")
        
        # Ask if the user wants to continue
        cont = input("Do you want to continue? (yes/no): ").lower()
        if cont != 'yes':
            break
        choice = input("Do you want to encrypt or decrypt a message? (e/d): ").lower()
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("Exit")
