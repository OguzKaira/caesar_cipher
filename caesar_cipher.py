import getpass

def caesar_cipher(text, shift, direction):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) + shift - base) % 26 + base) if direction == 'e' else chr((ord(char) - shift - base) % 26 + base)
        else:
            result += char
    return result

def main():
    print("Welcome to the Caesar Cipher Encryption/Decryption tool")
    text = getpass.getpass("Enter the text to be encrypted/decrypted: ")

    while True:
        direction = input("Do you want to encrypt or decrypt? (e/d): ").lower()
        if direction in ['e', 'd']:
            break
        else:
            print("Invalid input. Please enter 'e' for encryption or 'd' for decryption.")

    while True:
        try:
            shift = int(input("Enter the shift value for the Caesar cipher: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer for the shift value.")

    result = caesar_cipher(text, shift, direction)
    print("Result: {}".format(result))

if __name__ == "__main__":
    main()
