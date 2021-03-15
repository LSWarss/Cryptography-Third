class DatabaseController:
    """General passwords data base controller
    """
    
    def __init__(self, database, cursor):
        self.connection = database
        self.c = cursor

    def createPasswordsTable(self):
        """Check if the passwords table exists and if not it creats it
        """
        self.c.execute('''SELECT count(*) FROM sqlite_master WHERE type='table' AND name='passwords' ''')
        
        if self.c.fetchone()[0] == 0:
            print("Password table does not exists, creating now")
            self.connection.execute('''CREATE TABLE passwords (name text, password text, salt text)''')
        
        self.connection.commit()
        
    def showAllPasswords(self): 
        """Prints all passwords saved in passwords table to the screen, and returns number of passwords

        Returns:
            int : Number of rows in Passwords table
        """
        allrows = self.c.execute('''SELECT * FROM passwords''').fetchall()
        for row in allrows:
            print(row)
        self.connection.commit()
        return len(allrows)

    def insertPassword(self,account):
        """Insert new password to the database 

        Args:
            account (Account): Account model with name, password and salt

        Returns:
            id : Created password id in table
        """
        query = ''' INSERT INTO passwords (name, password, salt) VALUES (?,?,?)'''
        self.c.execute(query, (account.name, account.password, account.salt))
        self.connection.commit()
        return self.c.lastrowid
