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
  paid_days = row['trans_paid_days']
  row_trans_date = app_tables.trans_date.search()[0]
  no_of_days_in_month = row_trans_date['tr_days']
  
  earning1 = row['trans_earn1'] 
  ee1 = round(((earning1 / no_of_days_in_month) * paid_days),2)
  earning2 = row['trans_earn2'] 
  ee2 = round(((earning2 / no_of_days_in_month) * paid_days),2)
  earning3 = row['trans_earn3'] 
  ee3 = round(((earning3 / no_of_days_in_month) * paid_days),2) 
  earning4 = row['trans_earn4'] 
  ee4 = round(((earning4 / no_of_days_in_month) * paid_days),2) 
  earning5 = row['trans_earn5'] 
  ee5 = round(((earning5 / no_of_days_in_month) * paid_days),2) 
  earning6 = row['trans_earn6'] 
  ee6 = round(((earning6 / no_of_days_in_month) * paid_days),2)
  earning7 = row['trans_earn7'] 
  ee7 = round(((earning7 / no_of_days_in_month) * paid_days),2)
  earning8 = row['trans_earn8'] 
  ee8 = round(((earning8 / no_of_days_in_month) * paid_days),2) 
  earning9 = row['trans_earn9'] 
  ee9 = round(((earning9 / no_of_days_in_month) * paid_days),2) 
  earning10 = row['trans_earn10'] 
  ee10 = round(((earning10 / no_of_days_in_month) * paid_days),2) 

  return ee1,ee2,ee3,ee4,ee5,ee6,ee7,ee8,ee9,ee10

@anvil.server.callable
def update_earn1(trans_comp_code,trans_empid,trans_earn_earn1,trans_earn_earn2,trans_earn_earn3,
                trans_earn_earn4,trans_earn_earn5,trans_earn_earn6,trans_earn_earn7,trans_earn_earn8,
                trans_earn_earn9,trans_earn_earn10):
  row = app_tables.transaction.search(trans_comp_code=trans_comp_code,trans_empid=trans_empid)[0]
  row.update(trans_earn_earn1=trans_earn_earn1)
  row.update(trans_earn_earn2=trans_earn_earn2)
  row.update(trans_earn_earn3=trans_earn_earn3)
  row.update(trans_earn_earn4=trans_earn_earn4)
  row.update(trans_earn_earn5=trans_earn_earn5)
  row.update(trans_earn_earn6=trans_earn_earn6)
  row.update(trans_earn_earn7=trans_earn_earn7)
  row.update(trans_earn_earn8=trans_earn_earn8)
  row.update(trans_earn_earn9=trans_earn_earn9)
  row.update(trans_earn_earn10=trans_earn_earn10)

  ##############################################################################
  ################################ Start Attendeance Bonus #####################
  ##############################################################################
@anvil.server.callable
def attn_bonus(trans_comp_code,trans_empid):
  row = app_tables.transaction.search(trans_comp_code=trans_comp_code,trans_empid=trans_empid)[0]
  fxd_attn_bonus = row['trans_attn_bonus']
  mandays = row['trans_mandays']

  weekly_off = row['trans_wo']
  paid_holiday = row['trans_ph']
  layoff = row['trans_layoff']
  absent = row['trans_absent']
  leave1 = row['trans_leave1']
  leave2 = row['trans_leave2']
  leave3 = row['trans_leave3']

  row_trans_date = app_tables.trans_date.search()[0]
  no_of_days_in_month = row_trans_date['tr_days']
  sundays = row_trans_date['tr_sundays']
  
  if (mandays + paid_holiday) >= (no_of_days_in_month - weekly_off) :
    ebonus = fxd_attn_bonus
  else:
    ebonus = 0

  if ((leave1 + leave2 + leave3) > 0) : ## applied leave
    ebonus = 0 

  if (absent) : ## absent days are there
    ebonus = 0 
  
  return ebonus

@anvil.server.callable
def update_earn_att_bonus(trans_comp_code,trans_empid,trans_earn_attn_bonus):
  row = app_tables.transaction.search(trans_comp_code=trans_comp_code,trans_empid=trans_empid)[0]
  row.update(trans_earn_attn_bonus=trans_earn_attn_bonus)
  ##############################################################################
  ################################ End Attendeance Bonus #######################
  ##############################################################################