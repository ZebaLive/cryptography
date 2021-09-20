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


eq = additive_encryption("HelloWorld", 4)
print(eq)
pt = additive_decryption(eq, 4)
print(pt)