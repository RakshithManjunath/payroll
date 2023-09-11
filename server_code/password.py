import anvil.files
from anvil.files import data_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#

@anvil.server.callable
def check_username_and_password(username, password):
  row = app_tables.password.get(username=username)
  if row:
    print(f"User {username} exists")
    if row['password'] == password:
      print(f"Correct password for {username}")
    else:
      print(f"Incorrect password for {username}")
  else:
    print(f"User {username} doesn't exist")
  # password_table = app_tables.password.search()
  # db_username, db_password = password[username], password_table[password]

@anvil.server.callable
def check_password_and_confirm_password(username, password):
  pass