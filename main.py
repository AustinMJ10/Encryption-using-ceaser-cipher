# Define a function for encryption using the Caesar Cipher algorithm
def caesar_cipher_encrypt(text, shift):
    encrypted_text = ''
    # Iterate through each character in the input text
    for char in text:
        # Check if the character is an alphabet
        if char.isalpha():
            # Determine the shifted character's ASCII value and convert it back to a character
            shifted_char = chr((ord(char) - ord('a' if char.islower() else 'A') + shift) % 26 + ord('a' if char.islower() else 'A'))
            encrypted_text += shifted_char
        else:
            encrypted_text += char
    return encrypted_text

# Define a function for decryption using the Caesar Cipher algorithm
def caesar_cipher_decrypt(encrypted_text, shift):
    decrypted_text = ''
    for char in encrypted_text:
        # Check if the character is an alphabet
        if char.isalpha():
            # Determine the original character's ASCII value and convert it back to a character
            shifted_char = chr((ord(char) - ord('a' if char.islower() else 'A') - shift) % 26 + ord('a' if char.islower() else 'A'))
            # Append the original character to the decrypted text
            decrypted_text += shifted_char
        else:
            decrypted_text += char
    # Return the decrypted text
    return decrypted_text

# Define the main function to handle user input and execution of the encryption and decryption processes
def main():
    message = input("Enter your message: ")
    shift = int(input("Enter the shift value: "))

    # Encrypt the message using the Caesar Cipher algorithm
    encrypted_message = caesar_cipher_encrypt(message, shift)
    print("Encrypted message:", encrypted_message)

    # Decrypt the encrypted message using the Caesar Cipher algorithm
    decrypted_message = caesar_cipher_decrypt(encrypted_message, shift)
    print("Decrypted message:", decrypted_message)

if __name__ == "__main__":
    # Call the main function to start the execution of the program
    main()

#These comments explain each part of the code, from defining functions for encryption and decryption, to handling user input in the main function, and finally executing the program.
