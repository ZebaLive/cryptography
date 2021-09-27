import math
import inverse

#multiplicative encrypter
class MultiplicativeCrypter:

    def encryption(self, text, key):
        text = text.upper()
        key = int(key)
        if math.gcd(key, 26) != 1:
            return "ERROR: key is invalid!" 
        encryption = ""
        for c in text:
            # find the position in 0-25
            c_u = ord(c)
            c_i = ord(c) - ord("A")
            # perform the shift
            new_i = (c_i * key) % 26
            # convert to new character
            new_u = new_i + ord("A")
            new_c = chr(new_u)
            # append to encrypted string
            encryption += new_c
        return encryption

    def decryption(self, text, key):
        text = text.upper()
        key = int(key)
        if math.gcd(key, 26) != 1:
            return "ERROR: key is invalid!" 
        key = inverse.modInverse(int(key), 26)
        p_text = ""
        for c in text:
            # find the position in 0-25
            c_u = ord(c)
            c_i = ord(c) - ord("A")
            # perform the negative shift
            new_i = (c_i * key) % 26
            # convert to new character
            new_u = new_i + ord("A")
            new_c = chr(new_u)
            # append to plain string
            p_text += new_c
        return p_text
