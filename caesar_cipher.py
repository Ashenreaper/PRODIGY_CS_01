def caesar_cipher(text, shift, mode):
    """
    Encrypts or decrypts text using the Caesar cipher.

    Args:
        text: The text to encrypt or decrypt.
        shift: The shift value (positive for encryption, negative for decryption).
        mode: 'encrypt' or 'decrypt'.

    Returns:
        The encrypted or decrypted text.
    """

    result = ''
    for char in text:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            shifted_char = chr((ord(char) - start + shift) % 26 + start)
        else:
            shifted_char = char  # Keep non-alphabetic characters as they are
        result += shifted_char
    return result

def main():
    while True:
        mode = input("Enter 'encrypt' or 'decrypt' (or 'exit'): ").lower()

        if mode == 'exit':
            break

        if mode not in ('encrypt', 'decrypt'):
            print("Invalid mode. Please enter 'encrypt' or 'decrypt'.")
            continue

        text = input("Enter the text: ")
        try:
            shift = int(input("Enter the shift value: "))
        except ValueError:
            print("Invalid shift value. Please enter an integer.")
            continue

        if mode == 'decrypt':
          shift = -shift

        result = caesar_cipher(text, shift, mode)
        print("Result:", result)

if __name__ == "__main__":
    main()s					