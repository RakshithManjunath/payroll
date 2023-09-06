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

  #print(cols)
  
  # # Specify the field name you want to check for
  field_name = 'xxxx'
  field_type = 'bool'

  for col in cols:
    if ((col["name"] == field_name) and (col["type"] == field_type)):
      print(col["name"])
      print(col["type"])
    else:
    #      print("fail")
    
    # 'type': 'number' for numeric
    # 'type': 'string' for text
    # 'type': 'bool' for logical
    # 'type': 'date' for date

    #  # field_type = anvil.server.app_tables.transaction.TextColumnType()  # You can choose the appropriate column type (e.g., Text, Date, Number)
      data_table.add_column(field_name, field_type)
  
    # Get a list of all column names in the data table
      # all_column_names = data_table.get_columns()
      all_column_names = cols(0)
  
