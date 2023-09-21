import anvil.files
from anvil.files import data_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import pandas as pd

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
def emp_to_trans_transfer(id,trans_date,trans_empid,trans_empname,trans_father_husband,
                           trans_empsex,trans_empdob,trans_empdoj,trans_emptype,trans_deptcode,
                           trans_deptname,trans_desicode,trans_desiname,trans_emppfc,
                           trans_emppfno,trans_emp_pfuan,trans_empesic,trans_empesino,
                           trans_empdispensary,trans_empptc,trans_empitc,trans_emppan,
                           trans_phone_number,trans_alt_phone_number,trans_email_address,
                           trans_aadhar_number,trans_attn_bonus,
                           trans_earn1,trans_earn2,trans_earn3,trans_earn4,trans_earn5,
                           trans_earn6,trans_earn7,trans_earn8,trans_earn9,trans_earn10,
                           trans_mandays,trans_wo,trans_ph,trans_layoff,trans_absent,
                           trans_leave1,trans_leave2,trans_leave3,trans_othrs,trans_inchrs,
                           trans_ded1,trans_ded2,trans_ded3,trans_ded4,
                           trans_loan1,trans_loan2,
                           trans_adv,trans_tds,trans_pfvol,trans_lic,
                           trans_arr_esipt,trans_arr_pf):
  transaction = app_tables.transaction
  return transaction.add_row(
      id=id,
      trans_date=trans_date,
      trans_empid=trans_empid,
      trans_empname=trans_empname,
      trans_father_husband=trans_father_husband,
      trans_empsex = trans_empsex,
      trans_empdob = trans_empdob,
      trans_empdoj = trans_empdoj,
      trans_emptype = trans_emptype,
      trans_deptcode = trans_deptcode,
      trans_deptname = trans_deptname,
      trans_desicode = trans_desicode,
      trans_desiname = trans_desiname,
      trans_emppfc = trans_emppfc,
      trans_emppfno = trans_emppfno,
      trans_emp_pfuan = trans_emp_pfuan,
      trans_empesic = trans_empesic,
      trans_empesino = trans_empesino,
      trans_empdispensary = trans_empdispensary,
      trans_empptc = trans_empptc,
      trans_empitc = trans_empitc,
      trans_emppan = trans_emppan,
      trans_phone_number = trans_phone_number,
      trans_alt_phone_number = trans_alt_phone_number,
      trans_email_address = trans_email_address,
      trans_aadhar_number = trans_aadhar_number,
      trans_attn_bonus = trans_attn_bonus,
      trans_earn1 = trans_earn1,
      trans_earn2 = trans_earn2,
      trans_earn3 = trans_earn3,
      trans_earn4 = trans_earn4,
      trans_earn5 = trans_earn5,
      trans_earn6 = trans_earn6,
      trans_earn7 = trans_earn7,
      trans_earn8 = trans_earn8,
      trans_earn9 = trans_earn9,
      trans_earn10 = trans_earn10,
      trans_mandays=trans_mandays,
      trans_wo=trans_wo,
      trans_ph=trans_ph,
      trans_layoff=trans_layoff,
      trans_absent=trans_absent,
      trans_leave1=trans_leave1,
      trans_leave2=trans_leave2,
      trans_leave3=trans_leave3,
      trans_othrs=trans_othrs,
      trans_inchrs=trans_inchrs,
      trans_ded1=trans_ded1,
      trans_ded2=trans_ded2,
      trans_ded3=trans_ded3,
      trans_ded4=trans_ded4,
      trans_loan1=trans_loan1,
      trans_loan2=trans_loan2,
      trans_adv=trans_adv,
      trans_tds=trans_tds,
      trans_pfvol=trans_pfvol,
      trans_lic=trans_lic,
      trans_arr_esipt=trans_arr_esipt,
      trans_arr_pf=trans_arr_pf
      )
                             
def get_default_value_for_type(column_type):
  # Define default values based on column types (you can customize this)
  if column_type == 'text':
      return ''
  elif column_type == 'number':
      return 0
  elif column_type == 'date':
      return date(2000, 1, 1)  # Current UTC date and time
  elif column_type == 'true/false':
      return False
  return None
  

@anvil.server.callable
def trans_default_values(row):
  columns_and_types = {
  'trans_mandays': 'number',
  'trans_wo': 'number',
  'trans_ph': 'number',
  'trans_layoff': 'number',
  'trans_absent': 'number',
  'trans_leave1': 'number',
  'trans_leave2': 'number',
  'trans_leave3': 'number',
  'trans_othrs': 'number',
  'trans_inchrs': 'number',
  'trans_ded1': 'number',
  'trans_ded2': 'number',  
  'trans_ded3': 'number', 
  'trans_ded4': 'number',
  'trans_loan1': 'number',
  'trans_loan2': 'number',
  'trans_adv': 'number',
  'trans_tds': 'number',
  'trans_pfvol': 'number',
  'trans_lic': 'number',
  'trans_arr_esipt': 'number',
  'trans_arr_pf': 'number',
  'trans_earn_earn1': 'number', 
  'trans_earn_earn2': 'number', 
  'trans_earn_earn3': 'number', 
  'trans_earn_earn4': 'number', 
  'trans_earn_earn5': 'number', 
  'trans_earn_earn6': 'number', 
  'trans_earn_earn7': 'number', 
  'trans_earn_earn8': 'number', 
  'trans_earn_earn9': 'number', 
  'trans_earn_earn10': 'number',
  'Fxd_earn_gross': 'number',
  'earn_pf_salary': 'number',
  'earn_fpf_salary': 'number',
  'earn_esi_salary': 'number',
  'earn_pt_salary': 'number', 
  'earn_ot_salary': 'number',
  'earn_it_salary': 'number', 
  'earn_bonus_salary': 'number',      
  'pf_amt': 'number',
  'fpf_amt': 'number',
  'esi_amt': 'number',
  'pt_amt': 'number',
  'ot_amt': 'number',
  'it_or_tds_amt': 'number',
  'bonus_amt': 'number'    
  }
  
  for column_name, column_type in columns_and_types.items():
    print(column_name, column_type)
    if row[column_name] is None:
      print(row[column_name])
      default_value = get_default_value_for_type(column_type)
      row[column_name] = default_value  

@anvil.server.callable
def trans_change_update(trans_empid,trans_mandays,trans_wo,trans_ph,trans_layoff,trans_absent,
                        trans_leave1,trans_leave2,trans_leave3,trans_othrs,trans_inchrs,
                        trans_ded1,trans_ded2,trans_ded3,trans_ded4,
                        trans_loan1,trans_loan2,
                        trans_adv,trans_tds,trans_pfvol,trans_lic,
                        trans_arr_esipt,trans_arr_pf):
  row = app_tables.transaction.get(trans_empid=trans_empid)
  row.update(trans_mandays=trans_mandays,
            trans_wo=trans_wo,
            trans_ph=trans_ph,
            trans_layoff=trans_layoff,
            trans_absent=trans_absent,
            trans_leave1=trans_leave1,
            trans_leave2=trans_leave2,
            trans_leave3=trans_leave3,
            trans_othrs=trans_othrs,
            trans_inchrs=trans_inchrs,
            trans_ded1=trans_ded1,
            trans_ded2=trans_ded2,
            trans_ded3=trans_ded3,
            trans_ded4=trans_ded4,
            trans_loan1=trans_loan1,
            trans_loan2=trans_loan2,
            trans_adv=trans_adv,
            trans_tds=trans_tds,
            trans_pfvol=trans_pfvol,
            trans_lic=trans_lic,
            trans_arr_esipt=trans_arr_esipt,
            trans_arr_pf=trans_arr_pf
            )

############ trans change #############
@anvil.server.callable
def trans_emp_name_and_code():
  emp_details = []
  for r in app_tables.transaction.search(tables.order_by("trans_empid")):
    emp_details.append(r['trans_empid'] + " | "  +r['trans_empname'])
  return emp_details

@anvil.server.callable
def trans_emp_get_details(trans_empid):
  row = app_tables.transaction.get(trans_empid=trans_empid)
  return row

@anvil.server.callable
def trans_emp_delete_row(trans_empid):
  row = app_tables.transaction.get(trans_empid=trans_empid)
  row.delete()

@anvil.server.callable
def trans_get_all_details():
  return app_tables.transaction.search(tables.order_by("trans_empid"))

@anvil.server.callable
def get_all_companies():
  return app_tables.company.search()

@anvil.server.callable
def get_all_password():
  return app_tables.password.search()

@anvil.server.callable
def get_all_companies_download():
  data_table = app_tables.company.search()
  csv_rows = []
  
  earnhead1_pf = None
  earnhead1_esi = None
  earnhead1_pt = None
  earnhead1_it = None
  earnhead1_ot = None
  earnhead1_bonus = None

  earnhead2_pf = None
  earnhead2_esi = None
  earnhead2_pt = None
  earnhead2_it = None
  earnhead2_ot = None
  earnhead2_bonus = None

  earnhead3_pf = None
  earnhead3_esi = None
  earnhead3_pt = None
  earnhead3_it = None
  earnhead3_ot = None
  earnhead3_bonus = None

  earnhead4_pf = None
  earnhead4_esi = None
  earnhead4_pt = None
  earnhead4_it = None
  earnhead4_ot = None
  earnhead4_bonus = None

  earnhead5_pf = None
  earnhead5_esi = None
  earnhead5_pt = None
  earnhead5_it = None
  earnhead5_ot = None
  earnhead5_bonus = None

  earnhead6_pf = None
  earnhead6_esi = None
  earnhead6_pt = None
  earnhead6_it = None
  earnhead6_ot = None
  earnhead6_bonus = None

  earnhead7_pf = None
  earnhead7_esi = None
  earnhead7_pt = None
  earnhead7_it = None
  earnhead7_ot = None
  earnhead7_bonus = None

  earnhead8_pf = None
  earnhead8_esi = None
  earnhead8_pt = None
  earnhead8_it = None
  earnhead8_ot = None
  earnhead8_bonus = None

  earnhead9_pf = None
  earnhead9_esi = None
  earnhead9_pt = None
  earnhead9_it = None
  earnhead9_ot = None
  earnhead9_bonus = None

  earnhead10_pf = None
  earnhead10_esi = None
  earnhead10_pt = None
  earnhead10_it = None
  earnhead10_ot = None
  earnhead10_bonus = None
  
  bonus_pt_included = None
 
  for row in data_table:
    if row['comp_earnhead1_pf'] == False:
      ehead1_pf = 0
    elif row['comp_earnhead1_pf'] == True:
      ehead1_pf = 1
    elif row['comp_earnhead1_pf'] == None:
      ehead1_pf = 0
      
    if row['comp_earnhead1_esi'] == False:
      ehead1_esi = 0
    elif row['comp_earnhead1_esi'] == True:
      ehead1_esi = 1
    elif row['comp_earnhead1_esi'] == None:
      ehead1_esi = 0  

    if row['comp_earnhead1_pt'] == False:
      ehead1_pt = 0
    elif row['comp_earnhead1_pt'] == True:
      ehead1_pt = 1
    elif row['comp_earnhead1_pt'] == None:
      ehead1_pt = 0 
      
    if row['comp_earnhead1_it'] == False:
      ehead1_it = 0
    elif row['comp_earnhead1_it'] == True:
      ehead1_it = 1
    elif row['comp_earnhead1_it'] == None:
      ehead1_it = 0

    if row['comp_earnhead1_ot'] == False:
      ehead1_ot = 0
    elif row['comp_earnhead1_ot'] == True:
      ehead1_ot = 1
    elif row['comp_earnhead1_ot'] == None:
      ehead1_ot = 0   

    if row['comp_earnhead1_bonus'] == False:
      ehead1_bonus = 0
    elif row['comp_earnhead1_bonus'] == True:
      ehead1_bonus = 1
    elif row['comp_earnhead1_bonus'] == None:
      ehead1_bonus = 0    


    if row['comp_earnhead2_pf'] == False:
      ehead2_pf = 0
    elif row['comp_earnhead2_pf'] == True:
      ehead2_pf = 1
    elif row['comp_earnhead2_pf'] == None:
      ehead2_pf = 0
      
    if row['comp_earnhead2_esi'] == False:
      ehead2_esi = 0
    elif row['comp_earnhead2_esi'] == True:
      ehead2_esi = 1
    elif row['comp_earnhead2_esi'] == None:
      ehead2_esi = 0  

    if row['comp_earnhead2_pt'] == False:
      ehead2_pt = 0
    elif row['comp_earnhead2_pt'] == True:
      ehead2_pt = 1
    elif row['comp_earnhead2_pt'] == None:
      ehead2_pt = 0 
      
    if row['comp_earnhead2_it'] == False:
      ehead2_it = 0
    elif row['comp_earnhead2_it'] == True:
      ehead2_it = 1
    elif row['comp_earnhead2_it'] == None:
      ehead2_it = 0

    if row['comp_earnhead2_ot'] == False:
      ehead2_ot = 0
    elif row['comp_earnhead2_ot'] == True:
      ehead2_ot = 1
    elif row['comp_earnhead2_ot'] == None:
      ehead2_ot = 0   

    if row['comp_earnhead2_bonus'] == False:
      ehead2_bonus = 0
    elif row['comp_earnhead2_bonus'] == True:
      ehead2_bonus = 1
    elif row['comp_earnhead2_bonus'] == None:
      ehead2_bonus = 0    


    if row['comp_earnhead3_pf'] == False:
      ehead3_pf = 0
    elif row['comp_earnhead3_pf'] == True:
      ehead3_pf = 1
    elif row['comp_earnhead3_pf'] == None:
      ehead3_pf = 0
      
    if row['comp_earnhead3_esi'] == False:
      ehead3_esi = 0
    elif row['comp_earnhead3_esi'] == True:
      ehead3_esi = 1
    elif row['comp_earnhead3_esi'] == None:
      ehead3_esi = 0  

    if row['comp_earnhead3_pt'] == False:
      ehead3_pt = 0
    elif row['comp_earnhead3_pt'] == True:
      ehead3_pt = 1
    elif row['comp_earnhead3_pt'] == None:
      ehead3_pt = 0 
      
    if row['comp_earnhead3_it'] == False:
      ehead3_it = 0
    elif row['comp_earnhead3_it'] == True:
      ehead3_it = 1
    elif row['comp_earnhead3_it'] == None:
      ehead3_it = 0

    if row['comp_earnhead3_ot'] == False:
      ehead3_ot = 0
    elif row['comp_earnhead3_ot'] == True:
      ehead3_ot = 1
    elif row['comp_earnhead3_ot'] == None:
      ehead3_ot = 0   

    if row['comp_earnhead3_bonus'] == False:
      ehead3_bonus = 0
    elif row['comp_earnhead3_bonus'] == True:
      ehead3_bonus = 1
    elif row['comp_earnhead3_bonus'] == None:
      ehead3_bonus = 0    


    if row['comp_earnhead4_pf'] == False:
      ehead4_pf = 0
    elif row['comp_earnhead4_pf'] == True:
      ehead4_pf = 1
    elif row['comp_earnhead4_pf'] == None:
      ehead4_pf = 0
      
    if row['comp_earnhead4_esi'] == False:
      ehead4_esi = 0
    elif row['comp_earnhead4_esi'] == True:
      ehead4_esi = 1
    elif row['comp_earnhead4_esi'] == None:
      ehead4_esi = 0  

    if row['comp_earnhead4_pt'] == False:
      ehead4_pt = 0
    elif row['comp_earnhead4_pt'] == True:
      ehead4_pt = 1
    elif row['comp_earnhead4_pt'] == None:
      ehead4_pt = 0 
      
    if row['comp_earnhead4_it'] == False:
      ehead4_it = 0
    elif row['comp_earnhead4_it'] == True:
      ehead4_it = 1
    elif row['comp_earnhead4_it'] == None:
      ehead4_it = 0

    if row['comp_earnhead4_ot'] == False:
      ehead4_ot = 0
    elif row['comp_earnhead4_ot'] == True:
      ehead4_ot = 1
    elif row['comp_earnhead4_ot'] == None:
      ehead4_ot = 0   

    if row['comp_earnhead4_bonus'] == False:
      ehead4_bonus = 0
    elif row['comp_earnhead4_bonus'] == True:
      ehead4_bonus = 1
    elif row['comp_earnhead4_bonus'] == None:
      ehead4_bonus = 0    

    if row['comp_earnhead5_pf'] == False:
      ehead5_pf = 0
    elif row['comp_earnhead5_pf'] == True:
      ehead5_pf = 1
    elif row['comp_earnhead5_pf'] == None:
      ehead5_pf = 0
      
    if row['comp_earnhead5_esi'] == False:
      ehead5_esi = 0
    elif row['comp_earnhead5_esi'] == True:
      ehead5_esi = 1
    elif row['comp_earnhead5_esi'] == None:
      ehead5_esi = 0  

    if row['comp_earnhead5_pt'] == False:
      ehead5_pt = 0
    elif row['comp_earnhead5_pt'] == True:
      ehead5_pt = 1
    elif row['comp_earnhead5_pt'] == None:
      ehead5_pt = 0 
      
    if row['comp_earnhead5_it'] == False:
      ehead5_it = 0
    elif row['comp_earnhead5_it'] == True:
      ehead5_it = 1
    elif row['comp_earnhead5_it'] == None:
      ehead5_it = 0

    if row['comp_earnhead5_ot'] == False:
      ehead5_ot = 0
    elif row['comp_earnhead5_ot'] == True:
      ehead5_ot = 1
    elif row['comp_earnhead5_ot'] == None:
      ehead5_ot = 0   

    if row['comp_earnhead5_bonus'] == False:
      ehead5_bonus = 0
    elif row['comp_earnhead5_bonus'] == True:
      ehead5_bonus = 1
    elif row['comp_earnhead5_bonus'] == None:
      ehead5_bonus = 0    


    if row['comp_earnhead6_pf'] == False:
      ehead6_pf = 0
    elif row['comp_earnhead6_pf'] == True:
      ehead6_pf = 1
    elif row['comp_earnhead6_pf'] == None:
      ehead6_pf = 0
      
    if row['comp_earnhead6_esi'] == False:
      ehead6_esi = 0
    elif row['comp_earnhead6_esi'] == True:
      ehead6_esi = 1
    elif row['comp_earnhead6_esi'] == None:
      ehead6_esi = 0  

    if row['comp_earnhead6_pt'] == False:
      ehead6_pt = 0
    elif row['comp_earnhead6_pt'] == True:
      ehead6_pt = 1
    elif row['comp_earnhead6_pt'] == None:
      ehead6_pt = 0 
      
    if row['comp_earnhead6_it'] == False:
      ehead6_it = 0
    elif row['comp_earnhead6_it'] == True:
      ehead6_it = 1
    elif row['comp_earnhead6_it'] == None:
      ehead6_it = 0

    if row['comp_earnhead6_ot'] == False:
      ehead6_ot = 0
    elif row['comp_earnhead6_ot'] == True:
      ehead6_ot = 1
    elif row['comp_earnhead6_ot'] == None:
      ehead6_ot = 0   

    if row['comp_earnhead6_bonus'] == False:
      ehead6_bonus = 0
    elif row['comp_earnhead6_bonus'] == True:
      ehead6_bonus = 1
    elif row['comp_earnhead6_bonus'] == None:
      ehead6_bonus = 0    

    if row['comp_earnhead7_pf'] == False:
      ehead7_pf = 0
    elif row['comp_earnhead7_pf'] == True:
      ehead7_pf = 1
    elif row['comp_earnhead7_pf'] == None:
      ehead7_pf = 0
      
    if row['comp_earnhead7_esi'] == False:
      ehead7_esi = 0
    elif row['comp_earnhead7_esi'] == True:
      ehead7_esi = 1
    elif row['comp_earnhead7_esi'] == None:
      ehead7_esi = 0  

    if row['comp_earnhead7_pt'] == False:
      ehead7_pt = 0
    elif row['comp_earnhead7_pt'] == True:
      ehead7_pt = 1
    elif row['comp_earnhead7_pt'] == None:
      ehead7_pt = 0 
      
    if row['comp_earnhead7_it'] == False:
      ehead7_it = 0
    elif row['comp_earnhead7_it'] == True:
      ehead7_it = 1
    elif row['comp_earnhead7_it'] == None:
      ehead7_it = 0

    if row['comp_earnhead7_ot'] == False:
      ehead7_ot = 0
    elif row['comp_earnhead7_ot'] == True:
      ehead7_ot = 1
    elif row['comp_earnhead7_ot'] == None:
      ehead7_ot = 0   

    if row['comp_earnhead7_bonus'] == False:
      ehead7_bonus = 0
    elif row['comp_earnhead7_bonus'] == True:
      ehead7_bonus = 1
    elif row['comp_earnhead7_bonus'] == None:
      ehead7_bonus = 0 

    if row['comp_earnhead8_pf'] == False:
      ehead8_pf = 0
    elif row['comp_earnhead8_pf'] == True:
      ehead8_pf = 1
    elif row['comp_earnhead8_pf'] == None:
      ehead8_pf = 0
      
    if row['comp_earnhead8_esi'] == False:
      ehead8_esi = 0
    elif row['comp_earnhead8_esi'] == True:
      ehead8_esi = 1
    elif row['comp_earnhead8_esi'] == None:
      ehead8_esi = 0  

    if row['comp_earnhead8_pt'] == False:
      ehead8_pt = 0
    elif row['comp_earnhead8_pt'] == True:
      ehead8_pt = 1
    elif row['comp_earnhead8_pt'] == None:
      ehead8_pt = 0 
      
    if row['comp_earnhead8_it'] == False:
      ehead8_it = 0
    elif row['comp_earnhead8_it'] == True:
      ehead8_it = 1
    elif row['comp_earnhead8_it'] == None:
      ehead8_it = 0

    if row['comp_earnhead8_ot'] == False:
      ehead8_ot = 0
    elif row['comp_earnhead8_ot'] == True:
      ehead8_ot = 1
    elif row['comp_earnhead8_ot'] == None:
      ehead8_ot = 0   

    if row['comp_earnhead8_bonus'] == False:
      ehead8_bonus = 0
    elif row['comp_earnhead8_bonus'] == True:
      ehead8_bonus = 1
    elif row['comp_earnhead8_bonus'] == None:
      ehead8_bonus = 0 

    if row['comp_earnhead9_pf'] == False:
      ehead9_pf = 0
    elif row['comp_earnhead9_pf'] == True:
      ehead9_pf = 1
    elif row['comp_earnhead9_pf'] == None:
      ehead9_pf = 0
      
    if row['comp_earnhead9_esi'] == False:
      ehead9_esi = 0
    elif row['comp_earnhead9_esi'] == True:
      ehead9_esi = 1
    elif row['comp_earnhead9_esi'] == None:
      ehead9_esi = 0  

    if row['comp_earnhead9_pt'] == False:
      ehead9_pt = 0
    elif row['comp_earnhead9_pt'] == True:
      ehead9_pt = 1
    elif row['comp_earnhead9_pt'] == None:
      ehead9_pt = 0 
      
    if row['comp_earnhead9_it'] == False:
      ehead9_it = 0
    elif row['comp_earnhead9_it'] == True:
      ehead9_it = 1
    elif row['comp_earnhead9_it'] == None:
      ehead9_it = 0

    if row['comp_earnhead9_ot'] == False:
      ehead9_ot = 0
    elif row['comp_earnhead9_ot'] == True:
      ehead9_ot = 1
    elif row['comp_earnhead9_ot'] == None:
      ehead9_ot = 0   

    if row['comp_earnhead9_bonus'] == False:
      ehead9_bonus = 0
    elif row['comp_earnhead9_bonus'] == True:
      ehead9_bonus = 1
    elif row['comp_earnhead9_bonus'] == None:
      ehead9_bonus = 0 

    if row['comp_earnhead10_pf'] == False:
      ehead10_pf = 0
    elif row['comp_earnhead10_pf'] == True:
      ehead10_pf = 1
    elif row['comp_earnhead10_pf'] == None:
      ehead10_pf = 0
      
    if row['comp_earnhead10_esi'] == False:
      ehead10_esi = 0
    elif row['comp_earnhead10_esi'] == True:
      ehead10_esi = 1
    elif row['comp_earnhead10_esi'] == None:
      ehead10_esi = 0  

    if row['comp_earnhead10_pt'] == False:
      ehead10_pt = 0
    elif row['comp_earnhead10_pt'] == True:
      ehead10_pt = 1
    elif row['comp_earnhead10_pt'] == None:
      ehead10_pt = 0 
      
    if row['comp_earnhead10_it'] == False:
      ehead10_it = 0
    elif row['comp_earnhead10_it'] == True:
      ehead10_it = 1
    elif row['comp_earnhead10_it'] == None:
      ehead10_it = 0

    if row['comp_earnhead10_ot'] == False:
      ehead10_ot = 0
    elif row['comp_earnhead10_ot'] == True:
      ehead10_ot = 1
    elif row['comp_earnhead10_ot'] == None:
      ehead10_ot = 0   

    if row['comp_earnhead10_bonus'] == False:
      ehead10_bonus = 0
    elif row['comp_earnhead10_bonus'] == True:
      ehead10_bonus = 1
    elif row['comp_earnhead10_bonus'] == None:
      ehead10_bonus = 0
    
    csv_row = ["[496577,781197072]",row["comp_id"], row["comp_code"], row["comp_name"], row["comp_addr1"],
              row["comp_addr2"], row["comp_pf_number"], row["comp_addr3"],row["comp_esi_number"],row["comp_pto_circle"],
              row["comp_emp_pfrate"],row["comp_empr_fpfrate"],row["comp_pf_admin"],row["comp_pf_edli"],
              row["comp_mgmt_pf_lt"],row["comp_mgmt_fpf_lt"],row["comp_esi_sal_lt"],row["comp_pts1_from"],
              row["comp_pts1_to"],row["comp_pts1_pt"],row["comp_pts2_from"],row["comp_pts2_to"],row["comp_pts2_pt"],
              row["comp_pts3_from"],row["comp_pts3_to"],row["comp_pts3_pt"],row["comp_ded1"],row["comp_ded2"],
              row["comp_ded3"],row["comp_ded4"],row["comp_earn_head1"],ehead1_pf,ehead1_pt,
              ehead1_it,ehead1_ot,ehead1_bonus,row["comp_earn_head2"],
              row["comp_earnhead2_pf"],row["comp_earnhead2_esi"],row["comp_earnhead2_pt"],row["comp_earnhead2_it"],
              row["comp_earnhead2_ot"],row["comp_earnhead2_bonus"],row["comp_earn_head3"],row["comp_earnhead3_pf"],
              row["comp_earnhead3_esi"],row["comp_earnhead3_pt"],row["comp_earnhead3_it"],row["comp_earnhead3_ot"],
              row["comp_earnhead3_bonus"],row["comp_earn_head4"],row["comp_earnhead4_pf"],row["comp_earnhead4_esi"],
              row["comp_earnhead4_pt"],row["comp_earnhead4_it"],row["comp_earnhead4_ot"],row["comp_earnhead4_bonus"],
              row["comp_earn_head5"],row["comp_earnhead5_pf"],row["comp_earnhead5_esi"],row["comp_earnhead5_pt"],
              row["comp_earnhead5_it"],row["comp_earnhead5_ot"],row["comp_earnhead5_bonus"],row["comp_earn_head6"],
              row["comp_earnhead6_pf"],row["comp_earnhead6_esi"],row["comp_earnhead6_pt"],row["comp_earnhead6_it"],
              row["comp_earnhead6_ot"],row["comp_earnhead6_bonus"],row["comp_earn_head7"],row["comp_earnhead7_pf"],
              row["comp_earnhead7_esi"],row["comp_earnhead7_pt"],row["comp_earnhead7_it"],row["comp_earnhead7_ot"],
              row["comp_earnhead7_bonus"],row["comp_earn_head8"],row["comp_earnhead8_pf"],row["comp_earnhead8_esi"],
              row["comp_earnhead8_pt"],row["comp_earnhead8_it"],row["comp_earnhead8_ot"],row["comp_earnhead8_bonus"],
              row["comp_earn_head9"],row["comp_earnhead9_pf"],row["comp_earnhead9_esi"],row["comp_earnhead9_pt"],
              row["comp_earnhead9_it"],row["comp_earnhead9_ot"],row["comp_earnhead9_bonus"],row["comp_earn_head10"],
              row["comp_earnhead10_pf"],row["comp_earnhead10_esi"],row["comp_earnhead10_pt"],row["comp_earnhead10_ot"],
              row["comp_earnhead10_it"],row["comp_earnhead10_bonus"],ehead1_esi,row["comp_bonus_from"],
              row["comp_bonus_to"],row["comp_bonus_percentage"],row["comp_bonus_limit"],row["comp_bonus_pt_included"],
              row["comp_leave_head1"],row["comp_leave_head2"],row["comp_leave_head3"],row["comp_loan_head1"],
              row["comp_loan_head2"],row["comp_pay_date"]]  
    csv_rows.append(csv_row)

  df = pd.DataFrame(csv_rows, columns=["ID","comp_id","comp_code","comp_name","comp_addr1","comp_addr2",
            "comp_pf_number","comp_addr3","comp_esi_number","comp_pto_circle",
            "comp_emp_pfrate","comp_empr_fpfrate","comp_pf_admin","comp_pf_edli",
            "comp_mgmt_pf_lt","comp_mgmt_fpf_lt","comp_esi_sal_lt","comp_pts1_from",
            "comp_pts1_to","comp_pts1_pt","comp_pts2_from","comp_pts2_to","comp_pts2_pt",
            "comp_pts3_from","comp_pts3_to","comp_pts3_pt","comp_ded1","comp_ded2",
            "comp_ded3","comp_ded4","comp_earn_head1","comp_earnhead1_pf","comp_earnhead1_pt",
            "comp_earnhead1_it","comp_earnhead1_ot","comp_earnhead1_bonus","comp_earn_head2",
            "comp_earnhead2_pf","comp_earnhead2_esi","comp_earnhead2_pt","comp_earnhead2_it",
            "comp_earnhead2_ot","comp_earnhead2_bonus","comp_earn_head3","comp_earnhead3_pf",
            "comp_earnhead3_esi","comp_earnhead3_pt","comp_earnhead3_it","comp_earnhead3_ot",
            "comp_earnhead3_bonus","comp_earn_head4","comp_earnhead4_pf","comp_earnhead4_esi",
            "comp_earnhead4_pt","comp_earnhead4_it","comp_earnhead4_ot","comp_earnhead4_bonus",
            "comp_earn_head5","comp_earnhead5_pf","comp_earnhead5_esi","comp_earnhead5_pt",
            "comp_earnhead5_it","comp_earnhead5_ot","comp_earnhead5_bonus","comp_earn_head6",
            "comp_earnhead6_pf","comp_earnhead6_esi","comp_earnhead6_pt","comp_earnhead6_it",
            "comp_earnhead6_ot","comp_earnhead6_bonus","comp_earn_head7","comp_earnhead7_pf",
            "comp_earnhead7_esi","comp_earnhead7_pt","comp_earnhead7_it","comp_earnhead7_ot",
            "comp_earnhead7_bonus","comp_earn_head8","comp_earnhead8_pf","comp_earnhead8_esi",
            "comp_earnhead8_pt","comp_earnhead8_it","comp_earnhead8_ot","comp_earnhead8_bonus",
            "comp_earn_head9","comp_earnhead9_pf","comp_earnhead9_esi","comp_earnhead9_pt",
            "comp_earnhead9_it","comp_earnhead9_ot","comp_earnhead9_bonus","comp_earn_head10",
            "comp_earnhead10_pf","comp_earnhead10_esi","comp_earnhead10_pt","comp_earnhead10_ot",
            "comp_earnhead10_it","comp_earnhead10_bonus","comp_earnhead1_esi","comp_bonus_from",
            "comp_bonus_to","comp_bonus_percentage","comp_bonus_limit","comp_bonus_pt_included",
            "comp_leave_head1","comp_leave_head2","comp_leave_head3","comp_loan_head1",
            "comp_loan_head2","comp_pay_date"])
  df.to_csv('/tmp/company.csv',index=False)
  df_media = anvil.media.from_file('/tmp/company.csv', 'csv', 'company.csv')
  return df_media


