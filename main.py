# Febry Afriansyah
# 09011382126166

# Define the encrypted text and alphabet
encrypted_text = "XRPCTCRGNEI"
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Function to decrypt with a given shift
def caesar_decrypt(ciphertext, shift, alphabet):
    decrypted_text = ""
    for char in ciphertext:
        if char in alphabet:
            index = (alphabet.index(char) - shift) % len(alphabet)
            decrypted_text += alphabet[index]
        else:
            decrypted_text += char
    return decrypted_text

# Try all possible shifts
for shift in range(1, 26):
    
    decrypted = caesar_decrypt(encrypted_text, shift, alphabet)
    print(f"Shift {shift}: {decrypted}")

