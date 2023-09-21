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
  
  for row in data_table:
    csv_row = ["[496577,781197072]",row["comp_id"], row["comp_code"], row["comp_name"], row["comp_addr1"],
              row["comp_addr2"], row["comp_pf_number"], row["comp_addr3"],row["comp_esi_number"],row["comp_pto_circle"],
              row["comp_emp_pfrate"],row["comp_empr_fpfrate"],row["comp_pf_admin"],row["comp_pf_edli"],
              row["comp_mgmt_pf_lt"],row["comp_mgmt_fpf_lt"],row["comp_esi_sal_lt"],row["comp_pts1_from"],
              row["comp_pts1_to"],row["comp_pts1_pt"],row["comp_pts2_from"],row["comp_pts2_to"],row["comp_pts2_pt"],
              row["comp_pts3_from"],row["comp_pts3_to"],row["comp_pts3_pt"],row["comp_ded1"],row["comp_ded2"],
              row["comp_ded3"],row["comp_ded4"],row["comp_earn_head1"],row["comp_earnhead1_pf"],row["comp_earnhead1_pt"],
              row["comp_earnhead1_it"],row["comp_earnhead1_ot"],row["comp_earnhead1_bonus"],row["comp_earn_head2"],
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
              row["comp_earnhead10_it"],row["comp_earnhead10_bonus"],row["comp_earnhead1_esi"],row["comp_bonus_from"],
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


