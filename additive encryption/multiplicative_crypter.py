import math

#multiplicative encrypter
class MultiplicativeCrypter:

    def modInverse(self, a, m) :
        a = a % m
        for x in range(1, m) :
            if ((a * x) % m == 1) :
                return x
        return 1

    def encryption(self, text, key):
        text = text.upper()
        key = int(key)
        if math.gcd(key, 26) != 1:
            return "ERROR: uncompatable key!" 
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
        key = self.modInverse(int(key), 26)
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
