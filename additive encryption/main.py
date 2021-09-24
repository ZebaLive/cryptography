#main application interface
import additive_crypter

print("Additive encryption")
print("-------------------")
cypher = additive_crypter.AdditiveCrypter()

print("Please select one")
i = 0
while i < 3:
    i = int(input("[1] encryption, [2] decryption, [3] exit: "))
    if i == 1:
        text = input("Input raw [text]: ")
        key = input("Input key [number]: ")
        print("Encrypting text...")
        print("Encypted text:")
        print(cypher.encryption(text, key))

    if i == 2 :
        text = input("Input encrypted [text]: ")
        key = input("Input key [number]: ")
        print("Decrypting text...")
        print("Raw text:")
        print(cypher.decryption(text, key))

    
