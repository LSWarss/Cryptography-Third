from account_model import Account

def testModelCreation(): 
    account = Account("google.com", "qwerty123")
    assert account
    
def testModelSaltGetter(): 
    account = Account("google.com", "qwerty123")
    assert account.get_salt() != None
    
def testPasswordHashing():
    account = Account("google.com", "qwerty123")
    assert account.get_password() != "qwerty123"

def testPasswordVerification(): 
    account = Account("google.com", "qwerty123")
    assert account.verifyPassword("qwerty123", account.get_salt())
    assert account.verifyPassword("qwertuch123", account.get_salt()) == False

