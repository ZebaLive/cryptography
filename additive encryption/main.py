#main application interface
import additive_crypter
import multiplicative_crypter

print("Additive encryption")
print("-------------------")
cypher = additive_crypter.AdditiveCrypter()

print("Please select one")
selector = 0
while selector < 3:
    selector = int(input("[1] additive encryption, [2] multiplicative encryption, [3] exit: "))
    if selector == 1:
        cypher = additive_crypter.AdditiveCrypter()
        if int(input("[1] encryption, [2] decryption: ")) == 1:
            text = input("Input raw [text]: ")
            key = input("Input key [number]: ")
            print("Encrypting text...")
            print("Encypted text:")
            print(cypher.encryption(text, key))
        else:
            text = input("Input encrypted [text]: ")
            key = input("Input key [number]: ")
            print("Decrypting text...")
            print("Raw text:")
            print(cypher.decryption(text, key))

    if selector == 2 :
        cypher = multiplicative_crypter.MultiplicativeCrypter()
        if int(input("[1] encryption, [2] decryption: ")) == 1:
            text = input("Input raw [text]: ")
            key = input("Input key [number]: ")
            print("Encrypting text...")
            print("Encypted text:")
            print(cypher.encryption(text, key))
        else:
            text = input("Input encrypted [text]: ")
            key = input("Input key [number]: ")
            print("Decrypting text...")
            print("Raw text:")
            print(cypher.decryption(text, key))

    
