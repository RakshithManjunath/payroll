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


#### Transaction ###############
####### concatenating emp name and code #########
@anvil.server.callable
def trans_empcode_name():
  emp_details = []
  for r in app_tables.employee.search(tables.order_by("emp_code")):
    emp_details.append(r['emp_code'] + " | "  +r['emp_name'])
  return emp_details

@anvil.server.callable
def trans_get_next_string_value():
  # Get the last row of the data table
  next_value = '0000000001'
  try:
    id_list = [(r["id"]) for r in app_tables.transaction.search()]
    last_row = id_list[-1]
    last_string_value = last_row
    next_value = str(int(last_string_value) + 1).zfill(10)
  except IndexError:
    next_value == '0000000001'
  return next_value

@anvil.server.callable
def test_dynamic_col_create(id,trans_date,trans_empid,trans_empname,trans_father_husband,
                           trans_empsex):
  transaction = app_tables.transaction
  transaction.add_row(
      id=id,
      trans_date=trans_date,
      trans_empid=trans_empid,
      trans_empname=trans_empname,
      trans_father_husband=trans_father_husband,
      trans_empsex = trans_empsex
  )