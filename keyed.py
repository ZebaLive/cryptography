#Keyed Transpostion crypter class
import math

class KeyedTranspositionCrypter:
    #encryption function
    def encryption(self, text, key):
        encrypted_text = [''] * key

        for col in range(key):
            position = col
            while position < len(text):
                encrypted_text[col] += text[position]
                position += key
        return ''.join(encrypted_text) #Cipher text

    #decryption function
    def decryption(self, text, key):
        num_of_columns = math.ceil(len(text) / key)
        num_of_rows = key
        num_of_shaded_boxes = (num_of_columns * num_of_rows) - len(text)
        plaintext = [''] * num_of_columns
        col = 0
        row = 0

        #place letters in a column format and later combined or concatenate them together
        for symbol in text:
            plaintext[col] += symbol
            col += 1
            if (col == num_of_columns) or (col == num_of_columns - 1 and row >= num_of_rows - num_of_shaded_boxes):
                col = 0 
                row += 1 
        return ''.join(plaintext)
