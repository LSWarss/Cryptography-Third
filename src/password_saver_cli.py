import click
from sty import fg
import sqlite3
from dbController import DatabaseController
from account_model import Account

connector = sqlite3.connect('assignment.db')
cursor = connector.cursor()
db = DatabaseController(connector, cursor)
db.createPasswordsTable()

@click.group()
def cli():
    pass

@cli.command()
def hello():
    """ Welcomes you :) 
    """
    click.echo("Hello, this is password saver CLI 🛡")

@cli.command()
@click.argument('name')
def savePassword(name):
    """Saves new password for specified name
    """
    password = input(f"Pass password you want to save for {name}: ")
    account = Account(name, password)
    password_verificator = input(f"Pass password again for verification: ")
    matching_passwords = account.verifyPassword(password_verificator, account.get_salt())
    while matching_passwords == False:
        click.echo("Wrong password ❌")
        password_verificator = input(fg.red + f"Pass password again for verification: " + fg.rs)
        matching_passwords = account.verifyPassword(password_verificator, account.get_salt())
    click.echo("Password was saved ✅")
    db.insertPassword(account)

@cli.command()
def getPasswords():
    """ Return all passwords you have saved up in the database
    """
    db.showAllPasswords()

if __name__ == '__main__':
    cli()