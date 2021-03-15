class DatabaseController:
    
    def __init__(self, database, cursor):
        self.connection = database
        self.c = cursor

    def createPasswordsTable(self):
        self.c.execute('''SELECT count(*) FROM sqlite_master WHERE type='table' AND name='passwords' ''')
        
        if self.c.fetchone()[0] == 0:
            print("Password table does not exists, creating now")
            self.connection.execute('''CREATE TABLE passwords (name text, password text, salt text)''')
        
        self.connection.commit()
        
    def showAllPasswords(self): 
        allrows = self.c.execute('''SELECT * FROM passwords''').fetchall()
        for row in allrows:
            print(row)
        self.connection.commit()
        return len(allrows)

    def insertPassword(self,account):
        query = ''' INSERT INTO passwords (name, password, salt) VALUES (?,?,?)'''
        self.c.execute(query, (account.name, account.password, account.salt))
        self.connection.commit()
        return self.c.lastrowid
