import sqlite3
from dbController import DatabaseController
from account_model import Account

mockConnection = sqlite3.connect('mock.db')
cursor = mockConnection.cursor()

def testPasswordTableCreation():
    db = DatabaseController(mockConnection, cursor)
    db.createPasswordsTable()
    
    cursor.execute('''SELECT count(*) FROM sqlite_master WHERE type='table' AND name='passwords' ''')
    assert cursor.fetchone()[0] == 1
    
def testPasswordInsert():
    db = DatabaseController(mockConnection, cursor)
    account = Account("google.com", "qwerty123")
    db.insertPassword(account)
    assert db.showAllPasswords() != 0
    