#main application interface
import os, additive, multiplicative, autokey, keyed, affine 

class ui:
    def __init__(self):
        self.cypher = {
            "additive" : additive.AdditiveCrypter(),
            "multiplicative" : multiplicative.MultiplicativeCrypter(),
            "autokey" : autokey.AdditiveCrypter(),
            "affine" : affine.AffineCrypter()
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
            self.multiplicative()
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
            key = {
                "A" : input("Input first key (number): "),
                "B" : input("Input second key (number): ")
            }
            print("Encrypting text...")
            print("Encypted text:")
            print(self.cypher["affine"].encryption(text, key))
        elif selector == "2":
            os.system('cls||clear')
            text = input("Input encrypted text: ")
            key = {
                "A" : input("Input first key (number): "),
                "B" : input("Input second key (number): ")
            }
            print("Decrypting text...")
            print("Raw text:")
            print(self.cypher["affine"].decryption(text, key))
        elif selector == "3":
            return
        else:
            self.affine()
            return
        input("Press anything to go back to main meniu...")
        return

    def autokey(self):
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
            print(self.cypher["autokey"].encryption(text, key))
        elif selector == "2":
            os.system('cls||clear')
            text = input("Input encrypted text: ")
            key = input("Input key (number): ")
            print("Decrypting text...")
            print("Raw text:")
            print(self.cypher["autokey"].decryption(text, key))
        elif selector == "3":
            return
        else:
            self.autokey()
            return
        input("Press anything to go back to main meniu...")
        return

    def keyed(self):
        pass

def main(): 
    user_interface = ui()   
    user_interface.main_meniu()

if __name__ == '__main__':
    main()