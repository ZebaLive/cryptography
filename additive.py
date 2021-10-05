#Aditive crypter class
class AdditiveCrypter:
    #encryption function
    def encryption(self, text, key):
        text = text.upper()
        key = int(key)
        encrypted_text = ""
        for c in text:
            # find the position in 0-25
            c_u = ord(c)
            c_i = ord(c) - ord("A")
            # perform the shift
            new_i = (c_i + key) % 26
            # convert to new character
            new_u = new_i + ord("A")
            new_c = chr(new_u)
            # append to encrypted string
            encrypted_text += new_c
        return encrypted_text
    #decryption function
    def decryption(self, text, key):
        plain_text = ""
        i = 0
        while i < len(text):
            plain_text += __vig( ciphertext[i], key[i % len(key)], True )
            key += cleartext[-1]
            i += 1
        return plain_text