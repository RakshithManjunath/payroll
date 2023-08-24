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
############### Add Bank ############
######### auto increment 'bank_id' column ###########
@anvil.server.callable
def bank_get_next_string_value():
  # Get the last row of the data table
  next_value = '0000000001'
  try:
    bank_id_list = [(r["bank_id"]) for r in app_tables.bank.search()]
    last_row = bank_id_list[-1]
    last_string_value = last_row
    next_value = str(int(last_string_value) + 1).zfill(10)
  except IndexError:
    next_value == '0000000001'
  return next_value

@anvil.server.callable
def next_bank_id_value():
  # Get the last row of the data table
  next_value = '001'
  try:
    bank_code_list = [(r["bank_code"]) for r in app_tables.bank.search()]
    last_row = bank_code_list[-1]
    last_string_value = last_row
    next_value = str(int(last_string_value) + 1).zfill(3)
  except IndexError:
    next_value == '001'
  return next_value

@anvil.server.callable
def bank_add(bank_id,bankcode,bankname,bankadd1,bankadd2,bankadd3,bankifsc):
  app_tables.bank.add_row(bank_id=bank_id,bank_code=bankcode,
                          bank_name=bankname,bank_addr1=bankadd1,bank_addr2=bankadd2,
                         bank_addr3=bankadd3,bank_ifsc=bankifsc)