def additive_decryption(text, shift):
    text = text.upper()
    p_text = ""
    for c in text:
        # find the position in 0-25
        c_u = ord(c)
        c_i = ord(c) - ord("A")
        # perform the negative shift
        new_i = (c_i - shift) % 26
        # convert to new character
        new_u = new_i + ord("A")
        new_c = chr(new_u)
        # append to plain string
        p_text += new_c
    return p_text


print("__Additive Cipher__")
print(" ")
print("__decryption__")
print(" ")
text = input("enter tencrypted text: ")
key = input("enter key value: ")
print("decrypting...")
print("plain text:", additive_decryption(str(text), int(key)))
input("press any key to exit...")

