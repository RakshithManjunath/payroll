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
def just_test():
  # Access the data table
  cols = app_tables.transaction.list_columns()

  print(cols)
  
  # # Specify the field name you want to check for
  field_name_to_check = 'trans_date'

  for col in cols:
    if col["name"] == field_name_to_check:
      print(col["type"])
      print("exists")
    # else:
    #  # field_type = anvil.server.app_tables.transaction.TextColumnType()  # You can choose the appropriate column type (e.g., Text, Date, Number)
    #  # data_table.add_column(field_name, field_type)
  
  # # Get a list of all column names in the data table
  # all_column_names = data_table.get_columns()
  
  # # Check if the field name exists in the list of column names
  # if field_name_to_check in all_column_names:
  #     print(f"The field '{field_name_to_check}' exists in the data table.")
  # else:
  #     print(f"The field '{field_name_to_check}' does not exist in the data table.")
