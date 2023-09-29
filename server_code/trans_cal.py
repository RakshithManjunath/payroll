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
def earn1_cal(trans_comp_code,trans_empid):
  row = app_tables.transaction.search(trans_comp_code=trans_comp_code,trans_empid=trans_empid)[0]
  fixed_earning = row['trans_earn1'] 
  paid_days = row['trans_paid_days']
  row_trans_date = app_tables.trans_date.search()[0]
  no_of_days_in_month = row_trans_date['tr_days']
  return (fixed_earning / no_of_days_in_month) * paid_days

@anvil.server.callable
def update_earn1(trans_comp_code,trans_empid,trans_earn_earn1):
  row = app_tables.transaction.search(trans_comp_code=trans_comp_code,trans_empid=trans_empid)[0]
  row.update(trans_earn_earn1=trans_earn_earn1)