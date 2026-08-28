def caesar_decode(text, shift):
    result = ""
    for char in text:
        if 'A' <= char <= 'Z':
            # Dekodierung für Großbuchstaben (Shift nach links)
            base = ord('A')
            new_char = chr((ord(char) - base - shift) % 26 + base)
            result += new_char
        elif 'a' <= char <= 'z':
            # Dekodierung für Kleinbuchstaben (Shift nach links)
            base = ord('a')
            new_char = chr((ord(char) - base - shift) % 26 + base)
            result += new_char
        else:
            # Nicht-Buchstaben unverändert lassen
            result += char
    return result

# ----------------------------------------------------------
# USER-INPUT: Hier geben Sie den Text ein
input_text = input("Geben Sie den Text ein: ")

# Die gewünschte Verschiebung (3 nach links)
SHIFT_AMOUNT = 3

# Dekodierung durchführen und Ergebnis ausgeben
decoded_text = caesar_decode(input_text, SHIFT_AMOUNT)

print("\nDekodiert (Shift um 3 nach links):")
print(decoded_text)
