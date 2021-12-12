#%%
import rsa
#%%
class simple_oracle():

    def __init__(self, mod_size=256, exponent=65537):
        super().__init__()
        self.pk, self.sk = rsa.newkeys(mod_size, exponent=exponent)
        self.queries = 0

    def get_pubkey(self):
        return self.pk.n, self.pk.e

    def get_ciphertext(self):
        ciphertext = rsa.encrypt(b"decrypt me, Eve", self.pk)
        return ciphertext

    def decrypt(self, ciphertext):
        plaintext = rsa.decrypt(ciphertext, self.sk)
        return plaintext

    def oracle(self, ciphertext):
        """Returns whether the ciphertext is PKCS conforming"""
        self.queries += 1
        try:
            plaintext = rsa.decrypt(ciphertext, self.sk)
        except rsa.pkcs1.DecryptionError:
            return False
        else:
            return True

    def number_of_queries(self):
        return self.queries
# %%
