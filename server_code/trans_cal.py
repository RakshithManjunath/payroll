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
def earn_cal(trans_comp_code,trans_empid):
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
def update_earn(trans_comp_code,trans_empid,trans_earn_earn1,trans_earn_earn2,trans_earn_earn3,
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

  ##############################################################################
  ################################ PF Calculation Start #######################
  ##############################################################################
@anvil.server.callable
def pf_calculaton(comp_code,trans_empid):
  row = app_tables.company.get(comp_code=comp_code,)
  eh1_pf = row['comp_earnhead1_pf']
  eh2_pf = row['comp_earnhead2_pf']
  eh3_pf = row['comp_earnhead3_pf']
  eh4_pf = row['comp_earnhead4_pf']
  eh5_pf = row['comp_earnhead5_pf']
  eh6_pf = row['comp_earnhead6_pf']
  eh7_pf = row['comp_earnhead7_pf']
  eh8_pf = row['comp_earnhead8_pf']
  eh9_pf = row['comp_earnhead9_pf']
  eh10_pf = row['comp_earnhead10_pf']
  row = app_tables.transaction.search(trans_comp_code=comp_code,trans_empid=trans_empid)[0]
  if row['trans_emppfc'] == True:
    pfsal = 0
    fxd_pfsal = 0
    if eh1_pf == True:
      pfsal = row['trans_earn_earn1']
      fxd_pfsal  = row['trans_earn1']
    if eh2_pf == True:
      pfsal = pfsal + row['trans_earn_earn2']
      fxd_pfsal  = fxd_pfsal + row['trans_earn2']
    if eh3_pf == True:
      pfsal = pfsal + row['trans_earn_earn3']
      fxd_pfsal  = fxd_pfsal + row['trans_earn3']
    if eh4_pf == True:
      pfsal = pfsal + row['trans_earn_earn4']
      fxd_pfsal  = fxd_pfsal + row['trans_earn4']
    if eh5_pf == True:
      pfsal = pfsal + row['trans_earn_earn5']
      fxd_pfsal  = fxd_pfsal + row['trans_earn5']
    if eh6_pf == True:
      pfsal = pfsal + row['trans_earn_earn6']
      fxd_pfsal  = fxd_pfsal + row['trans_earn6']
    if eh7_pf == True:
      pfsal = pfsal + row['trans_earn_earn7']
      fxd_pfsal  = fxd_pfsal + row['trans_earn7']
    if eh8_pf == True:
      pfsal = pfsal + row['trans_earn_earn8']
      fxd_pfsal  = fxd_pfsal + row['trans_earn8']
    if eh9_pf == True:
      pfsal = pfsal + row['trans_earn_earn9']
      fxd_pfsal  = fxd_pfsal + row['trans_earn9']
    if eh10_pf == True:
      pfsal = pfsal + row['trans_earn_earn10']
      fxd_pfsal  = fxd_pfsal + row['trans_earn10']
  else:
    pfsal = 0
    
  return pfsal

@anvil.server.callable
def update_pfsalary(trans_comp_code,trans_empid,earn_pf_salary):
  row = app_tables.transaction.search(trans_comp_code=trans_comp_code,trans_empid=trans_empid)[0]
  row.update(earn_pf_salary = earn_pf_salary)
  ##############################################################################
  ################################ PF Calculation End    #######################
  ##############################################################################


  ##############################################################################
  ################################ ESI Calculation Start #######################
  ##############################################################################
@anvil.server.callable
def esi_calculaton(comp_code,trans_empid):
  row = app_tables.company.get(comp_code=comp_code,)
  eh1_esi = row['comp_earnhead1_esi']
  eh2_esi = row['comp_earnhead2_esi']
  eh3_esi = row['comp_earnhead3_esi']
  eh4_esi = row['comp_earnhead4_esi']
  eh5_esi = row['comp_earnhead5_esi']
  eh6_esi = row['comp_earnhead6_esi']
  eh7_esi = row['comp_earnhead7_esi']
  eh8_esi = row['comp_earnhead8_esi']
  eh9_esi = row['comp_earnhead9_esi']
  eh10_esi = row['comp_earnhead10_esi']
  row = app_tables.transaction.search(trans_comp_code=comp_code,trans_empid=trans_empid)[0]
  esisal = 0
  if eh1_esi == True:
    esisal = row['trans_earn_earn1']
  if eh2_esi == True:
    esisal = esisal + row['trans_earn_earn2']
  if eh3_esi == True:
    esisal = esisal + row['trans_earn_earn3']
  if eh4_esi == True:
    esisal = esisal + row['trans_earn_earn4']
  if eh5_esi == True:
    esisal = esisal + row['trans_earn_earn5']    
  if eh6_esi == True:
    esisal = esisal + row['trans_earn_earn6']
  if eh7_esi == True:
    esisal = esisal + row['trans_earn_earn7']
  if eh8_esi == True:
    esisal = esisal + row['trans_earn_earn8']
  if eh9_esi == True:
    esisal = esisal + row['trans_earn_earn9']
  if eh10_esi == True:
    esisal = esisal + row['trans_earn_earn10']    

  return esisal

@anvil.server.callable
def update_esisalary(trans_comp_code,trans_empid,earn_esi_salary):
  row = app_tables.transaction.search(trans_comp_code=trans_comp_code,trans_empid=trans_empid)[0]
  row.update(earn_esi_salary = earn_esi_salary)
  ##############################################################################
  ################################ ESI Calculation End    #######################
  ##############################################################################