
import sys
# Welcome message to encoder
print("Welcome to the Caesar Cipher Encoder")
def caesar_cipher(text, shift):
    encoded_text = ""
# Change to Uppercase, shift
    for char in text.upper():
        if char.isalpha():
            shifted = ord(char) - shift % 26
            if shifted > ord('Z'):
                shifted -= 26
            encoded_text += chr(shifted)
        else:
            continue

    return encoded_text

def format_output(encoded_text):
    formatted_text = ""
    block_count = 0
# Format per 5 characters, 10 blocks
    for i in range(0, len(encoded_text), 5):
        formatted_text += encoded_text[i:i+5] + " "
        block_count += 1
        if block_count % 10 == 0:
            formatted_text += "\n"

    return formatted_text.strip()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 caesar_cipher.py <shift>")
        sys.exit(1)
# Get input, encode and provide output 
    shift = int(sys.argv[1])
    message = input("Enter a message to encode: ")
    encoded_text = caesar_cipher(message, shift)
    formatted_text = format_output(encoded_text)

    print("\nEncoded message:")
    print(formatted_text)

if __name__ == "__main__":
    main()

