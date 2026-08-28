def caesar_kodieren(text, verschiebung=3):
    ergebnis = ""

    for zeichen in text:
        if "a" <= zeichen <= "z":
            ergebnis += chr((ord(zeichen) - ord("a") + verschiebung) % 26 + ord("a"))
        elif "A" <= zeichen <= "Z":
            ergebnis += chr((ord(zeichen) - ord("A") + verschiebung) % 26 + ord("A"))
        else:
            ergebnis += zeichen

    return ergebnis


eingabe = input("Text zum Kodieren eingeben: ")
kodierter_text = caesar_kodieren(eingabe)
print("Kodierter Text:", kodierter_text)
