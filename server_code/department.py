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
############### Add department ############
@anvil.server.callable
def dept_get_next_string_value():
  # Get the last row of the data table
  next_value = '001'
  try:
    dept_code_list = [(r["dept_code"]) for r in app_tables.department.search()]
    last_row = dept_code_list[-1]
    last_string_value = last_row
    next_value = str(int(last_string_value) + 1).zfill(3)
  except IndexError:
    next_value == '001'
  return next_value

@anvil.server.callable
def dept_add(deptcode,deptname):
  app_tables.department.add_row(dept_code=deptcode,
                          dept_name=deptname)








@anvil.server.callable
def get_dept_names():
  return [(r["dept_name"]) for r in app_tables.department.search()]