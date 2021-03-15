import hashlib
import os

class Account():
    """Account that you will save in database model
    """
    
    def __init__(self, name, password): 
        self.name = name
        self.salt = os.urandom(32)
        self.password = self.hashedPassword(password, self.salt)
    
    def get_salt(self):
        """Returns generated salt on object initialization

        Returns:
            Bytes : Returns bytes generated randomly
        """
        return self.salt
    
    def get_password(self):
        return self.password
    
    def get_name(self):
        return self.name
    
    def hashedPassword(self,password, salt):
        """Function retruning hased password with salt

        Args:
            password (str): Password before hashing
            salt : Salt for the hassing algorthim

        Returns:
            str: Hashed password
        """
        key = hashlib.pbkdf2_hmac(
            'sha256',
            str.encode(password),
            salt,
            100000 # It is recommended to use at least 100,000 iterations of SHA-256
        )
        return key.hex()
    
    def verifyPassword(self, password, salt):
        """Password verification function

        Args:
            password (str): Password to hash and check
            salt : Salt for the hassing algorthim

        Returns:
            Bool : Returns if the passwords match
        """
        if self.hashedPassword(password, salt) == self.password:
            return True
        else:
            return False
        