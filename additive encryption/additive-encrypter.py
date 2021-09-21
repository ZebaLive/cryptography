def additive_encryption(text, shift):
    text = text.upper()
    encryption = ""
    for c in text:
        # find the position in 0-25
        c_u = ord(c)
        c_i = ord(c) - ord("A")
        # perform the shift
        new_i = (c_i + shift) % 26
        # convert to new character
        new_u = new_i + ord("A")
        new_c = chr(new_u)
        # append to encrypted string
        encryption += new_c
    return encryption

print("__Additive Cipher__")
print(" ")
print("__encryption__")
print(" ")
text = input("enter text to encrypt: ")
key = input("enter key value: ")
print("encrypting...")
print("encrypted text:", additive_encryption(str(text), int(key)))
input("press any key to exit...")
