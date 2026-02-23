import sys

def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    # Ensure the shift stays within 0-25
    shift = shift if mode == 'encrypt' else -shift
    
    for char in text:
        if char.isalpha():
            # Calculate the starting point (ASCII 'A' or 'a')
            start = ord('A') if char.isupper() else ord('a')
            # Perform the shifting math: (Position + Shift) % 26
            new_pos = (ord(char) - start + shift) % 26
            result += chr(start + new_pos)
        else:
            # Keep spaces and punctuation as they are
            result += char
            
    return result

def main():
    print("--- Cryptography Tool: Caesar Cipher ---")
    
    while True:
        action = input("\nChoose: (E)ncrypt, (D)ecrypt, or (Q)uit: ").upper()
        if action == 'Q': break
        
        if action in ['E', 'D']:
            message = input("Enter your message: ")
            try:
                key = int(input("Enter shift key (1-25): "))
                mode = 'encrypt' if action == 'E' else 'decrypt'
                
                output = caesar_cipher(message, key, mode)
                print(f"\nResult: {output}")
            except ValueError:
                print("Invalid key. Please enter a number.")
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
