#main application interface
import additive_crypter
import multiplicative_crypter

print("Additive encryption")
print("-------------------")
cypher_additive = additive_crypter.AdditiveCrypter()
cypher_multiplicative = multiplicative_crypter.MultiplicativeCrypter()

print("Please select one")
selector = 0
while selector < 4:
    selector = int(input("[1] additive, [2] multiplicative, [3] affine, [4] exit: "))

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
    
