#main application interface
import os, additive, multiplicative, autokey, keyed 

class ui:
    def __init__(self):
        self.cypher = {
            "additive" : additive.AdditiveCrypter(),
            "multiplicative" : multiplicative.MultiplicativeCrypter(),
            "autokey" : autokey.AdditiveCrypter()
        }

    def main_meniu(self):
        os.system('cls||clear')
        print("---Mian Meniu---")
        print ("""
        1.Additive Cypher
        2.Multiplicative Cypher
        3.Affine Cypher
        4.Autokey Cypher
        5.Keyed Transposition Cypher
        6.Exit
        """)
        
        selector = input("Selection: ") 
        if selector == "1":
            self.additive()
        elif selector == "2":
            self.multiplicative()
        elif selector == "3":
            self.affine()
        elif selector == "4":
            self.autokey()
        elif selector == "5":
            self.keyed()
        elif selector == "6":
            self.exit()
            return
        self.main_meniu()
        return

    def exit(self):
        os.system('cls||clear')
        print ("""
        Thank you for using my cypher program and have a good day!
        
        Copyright© 2021 Paulius Pluta
        """)

    def additive(self):
        os.system('cls||clear')
        print("---Additive Cypher---")
        print("""
        1. Encryption
        2. Decryption
        3. Exit
        """)
        selector = input("Selection: ") 
        if selector == "1":
            os.system('cls||clear')
            text = input("Input raw text: ")
            key = input("Input key (number): ")
            print("Encrypting text...")
            print("Encypted text:")
            print(self.cypher["additive"].encryption(text, key))
        elif selector == "2":
            os.system('cls||clear')
            text = input("Input encrypted text: ")
            key = input("Input key (number): ")
            print("Decrypting text...")
            print("Raw text:")
            print(self.cypher["additive"].decryption(text, key))
        elif selector == "3":
            return
        else:
            self.additive()
            return
        input("Press anything to go back to main meniu...")
        return
    
    def multiplicative(self):
        os.system('cls||clear')
        print("---Multiplicative Cypher---")
        print("""
        1. Encryption
        2. Decryption
        3. Exit
        """)
        selector = input("Selection: ") 
        if selector == "1":
            os.system('cls||clear')
            text = input("Input raw text: ")
            key = input("Input key (number): ")
            print("Encrypting text...")
            print("Encypted text:")
            print(self.cypher["multiplicative"].encryption(text, key))
        elif selector == "2":
            os.system('cls||clear')
            text = input("Input encrypted text: ")
            key = input("Input key (number): ")
            print("Decrypting text...")
            print("Raw text:")
            print(self.cypher["multiplicative"].decryption(text, key))
        elif selector == "3":
            return
        else:
            self.additive()
            return
        input("Press anything to go back to main meniu...")
        return

    def affine(self):
        os.system('cls||clear')
        print("---Multiplicative Cypher---")
        print("""
        1. Encryption
        2. Decryption
        3. Exit
        """)
        selector = input("Selection: ") 
        if selector == "1":
            os.system('cls||clear')
            text = input("Input raw text: ")
            key = input("Input key (number): ")
            print("Encrypting text...")
            print("Encypted text:")
            print(self.cypher["multiplicative"].encryption(text, key))
        elif selector == "2":
            os.system('cls||clear')
            text = input("Input encrypted text: ")
            key = input("Input key (number): ")
            print("Decrypting text...")
            print("Raw text:")
            print(self.cypher["multiplicative"].decryption(text, key))
        elif selector == "3":
            return
        else:
            self.additive()
            return
        input("Press anything to go back to main meniu...")
        return

    def autokey(self):
        pass

    def keyed(self):
        pass


user_interface = ui()   

user_interface.main_meniu()
"""
print("Additive encryption")
print("-------------------")
cypher_additive = additive.AdditiveCrypter()
cypher_multiplicative = multiplicative.MultiplicativeCrypter()
cypher_autokey = autokey.AdditiveCrypter()

print("Please select one")
selector = 0



while selector < 5:
    selector = int(input("[1] additive, [2] multiplicative, [3] affine, [4] autokey, [5] exit: "))

    #additive encryption
    if selector == 1:
        if int(input("[1] encryption, [2] decryption: ")) == 1:
            text = input("Input raw [text]: ")
            key = input("Input key [number]: ")
            print("Encrypting text...")
            print("Encypted text:")
            print(cypher_additive.encryption(text, key))
        else:
            text = input("Input encrypted [text]: ")
            key = input("Input key [number]: ")
            print("Decrypting text...")
            print("Raw text:")
            print(cypher_additive.decryption(text, key))

    #multiplicative encryption
    if selector == 2:
        if int(input("[1] encryption, [2] decryption: ")) == 1:
            text = input("Input raw [text]: ")
            key = input("Input key [number]: ")
            print("Encrypting text...")
            print("Encypted text:")
            print(cypher_multiplicative.encryption(text, key))
        else:
            text = input("Input encrypted [text]: ")
            key = input("Input key [number]: ")
            print("Decrypting text...")
            print("Raw text:")
            print(cypher_multiplicative.decryption(text, key))

    #affine encryption
    if selector == 3:
        if int(input("[1] encryption, [2] decryption: ")) == 1:
            text = input("Input raw [text]: ")
            key1 = input("Input key one [number]: ")
            key2 = input("Input key two [number]: ")
            print("Encrypting text...")
            print("Encypted text:")
            print(cypher_additive.encryption(cypher_multiplicative.encryption(text, key2), key1))
        else:
            text = input("Input encrypted [text]: ")
            key1 = input("Input key one [number]: ")
            key2 = input("Input key two [number]: ")
            print("Decrypting text...")
            print("Raw text:")
            print(cypher_multiplicative.decryption(cypher_additive.decryption(text, key1), key2))

    #autokey encryption
    if selector == 4:
        if int(input("[1] encryption, [2] decryption: ")) == 1:
            text = input("Input raw [text]: ")
            key = input("Input key [number]: ")
            print("Encrypting text...")
            print("Encypted text:")
            print(cypher_autokey.encryption(text, key))
        else:
            text = input("Input encrypted [text]: ")
            key = input("Input key [number]: ")
            print("Decrypting text...")
            print("Raw text:")
            print(cypher_autokey.decryption(text, key))
"""