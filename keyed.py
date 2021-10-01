#Keyed Transpostion crypter class
import math

class KeyedTranspositionCrypter:
    #encryption function
    def encryption(self, text, key):
        text = text.upper()
        text = text.ljust(math.ceil(len(text) / key) * key, '*') 
        encrypted_text = ""
        for i in range(key):
            encrypted_text += text[i::key]
        return encrypted_text
    #decryption function
    def decryption(self, text, key):
        text = text.upper()
        plain_text = ""
        key = math.ceil(len(text) / key)
        for i in range(key):
            plain_text += text[i::key]
        return plain_text.replace('*','')
