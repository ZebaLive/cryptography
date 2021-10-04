#Affine crypter class
import math, additive, multiplicative

class AffineCrypter:

    def __init__(self):
        self.cypher = {
            "additive" : additive.AdditiveCrypter(),
            "multiplicative" : multiplicative.MultiplicativeCrypter()
        }

    def encryption(self, text, key):
        return self.cypher["additive"].encryption(self.cypher["multiplicative"].encryption(text, key["B"]), key["A"])

    def decryption(self, text, key):
        return self.cypher["multiplicative"].decryption(self.cypher["additive"].decryption(text, key["A"]), key["B"])