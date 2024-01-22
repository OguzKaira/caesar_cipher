def caesar_cipher(text, shift, direction):
    result = ""
    for char in text:
        if char.isalpha():
            if direction == 'e':
                result += chr((ord(char) + shift - ord('a')) % 26 + ord('a')) if char.islower() else chr((ord(char) + shift - ord('A')) % 26 + ord('A'))
            elif direction == 'd':
                result += chr((ord(char) - shift - ord('a')) % 26 + ord('a')) if char.islower() else chr((ord(char) - shift - ord('A')) % 26 + ord('A'))
        else:
            result += char
    return result

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Caesar Cipher Encryption/Decryption")
    parser.add_argument("-e", "--encrypt", action="store_true", help="Encrypt the text")
    parser.add_argument("-d", "--decrypt", action="store_true", help="Decrypt the text")

    args = parser.parse_args()
  
    direction = 'e' if args.encrypt else 'd'
    result = caesar_cipher(args.text, args.shift, direction)
    print(f"Result: {result}")
