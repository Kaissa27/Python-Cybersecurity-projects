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