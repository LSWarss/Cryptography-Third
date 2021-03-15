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
        
    def showAllTables(self): 
        self.c.execute('''SELECT * FROM passwords''')
        for row in self.c:
            print(row)
        self.connection.commit()

    def insertPassword(self,account):
        query = ''' INSERT INTO passwords(name,password, salt) VALUES (?,?, ?)'''
    