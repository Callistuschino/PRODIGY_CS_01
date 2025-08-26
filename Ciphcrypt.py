#!/usr/bin/env python3
"""
CIPHCRYPT — Simple Caesar cipher CLI (encrypt/decrypt with a known shift).
- Keeps case (A↦D, a↦d).
- Leaves non-letters (spaces, punctuation, digits) unchanged.
- Accepts any integer shift (…,-27,-1,0,1,27, …); internally reduced mod 26.
"""

from typing import Literal

BANNER = r"""
╔══════════════════════════════════════╗
║         C I P H C R Y P T            ║
║        Caesar Cipher Utility         ║
╚══════════════════════════════════════╝
"""

def normalize_shift(shift: int) -> int:
    """Reduce any integer shift into the 0..25 range."""
    return shift % 26

def shift_char(ch: str, shift: int) -> str:
    """Shift a single ASCII letter by `shift`, preserving case."""
    if 'a' <= ch <= 'z':
        base = ord('a')
        return chr((ord(ch) - base + shift) % 26 + base)
    if 'A' <= ch <= 'Z':
        base = ord('A')
        return chr((ord(ch) - base + shift) % 26 + base)
    return ch  # punctuation, spaces, digits, emoji, etc.

def caesar(text: str, shift: int) -> str:
    """Core Caesar transform used by both encrypt and decrypt."""
    s = normalize_shift(shift)
    return ''.join(shift_char(c, s) for c in text)

def encrypt(plaintext: str, shift: int) -> str:
    """Encrypt by shifting forward."""
    return caesar(plaintext, shift)

def decrypt(ciphertext: str, shift: int) -> str:
    """Decrypt by shifting backward (equivalent to shifting by -shift)."""
    return caesar(ciphertext, -shift)

def ask_int(prompt: str) -> int:
    """Prompt until the user enters a valid integer."""
    while True:
        raw = input(prompt).strip()
        try:
            return int(raw)
        except ValueError:
            print("Enter a whole number (e.g., -13, 0, 7, 26).")

def main() -> None:
    print(BANNER)
    while True:
        print("Select an option:")
        print("  [1] Encrypt")
        print("  [2] Decrypt")
        print("  [3] Exit")
        choice = input("> ").strip().lower()

        if choice in {"1", "e", "enc", "encrypt"}:
            message = input("\nEnter plaintext: ")
            shift = ask_int("Enter shift (integer): ")
            result = encrypt(message, shift)
            print(f"\n[Encrypted with shift {normalize_shift(shift)}] => {result}\n")

        elif choice in {"2", "d", "dec", "decrypt"}:
            message = input("\nEnter ciphertext: ")
            shift = ask_int("Enter shift used to encrypt (integer): ")
            result = decrypt(message, shift)
            print(f"\n[Decrypted with shift {normalize_shift(shift)}] => {result}\n")

        elif choice in {"3", "x", "q", "quit", "exit"}:
            print("\nGoodbye from CIPHCRYPT!")
            break
        else:
            print("Invalid choice. Type 1, 2, or 3.\n")

if __name__ == "__main__":
    main()
