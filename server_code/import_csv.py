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
#

@anvil.server.callable
def csv_company_upload():
  with open(data_files["company.csv"], "r") as f:
    dtype_mapping = {
    'comp_id': str,  
    'comp_code': str,
    'comp_name': str,
    'comp_addr1':str,  
    'comp_addr2':str,  
    'comp_addr3':str,
    'comp_pf_number': str,
    'comp_esi_number': str,
    'comp_pto_circle': str, 
    'comp_emp_pfrate': int, 
    'comp_empr_fpfrate': int, 
    'comp_pf_admin': int, 
    'comp_pf_edli': int, 
    'comp_mgmt_pf_lt': int, 
    'comp_mgmt_fpf_lt': int, 
    'comp_esi_sal_lt': int, 
    'comp_pts1_from': int, 
    'comp_pts1_to': int, 
    'comp_pts1_pt': int, 
    'comp_pts2_from': int, 
    'comp_pts2_to': int, 
    'comp_pts2_pt': int, 
    'comp_pts3_from': int, 
    'comp_pts3_to': int, 
    'comp_pts3_pt': int, 
    'comp_ded1': str, 
    'comp_ded2': str,
    'comp_ded3': str, 
    'comp_ded4': str,
    'comp_earn_head1': str, 
    'comp_earnhead1_pf': bool,
    'comp_earnhead1_esi': bool,
    'comp_earnhead1_pt': bool, 
    'comp_earnhead1_it': bool, 
    'comp_earnhead1_ot': bool, 
    'comp_earnhead1_bonus': bool, 
    'comp_earn_head2': str, 
    'comp_earnhead2_pf': bool, 
    'comp_earnhead2_esi': bool, 
    'comp_earnhead2_pt': bool, 
    'comp_earnhead2_it': bool, 
    'comp_earnhead2_ot': bool, 
    'comp_earnhead2_bonus': bool, 
    'comp_earn_head3': str, 
    'comp_earnhead3_pf': bool,
    'comp_earnhead3_esi': bool, 
    'comp_earnhead3_pt': bool, 
    'comp_earnhead3_it': bool, 
    'comp_earnhead3_ot': bool, 
    'comp_earnhead3_bonus': bool, 
    'comp_earn_head4': str, 
    'comp_earnhead4_pf': bool, 
    'comp_earnhead4_esi': bool, 
    'comp_earnhead4_pt': bool, 
    'comp_earnhead4_it': bool, 
    'comp_earnhead4_ot': bool, 
    'comp_earnhead4_bonus': bool, 
    'comp_earn_head5': str, 
    'comp_earnhead5_pf': bool,
    'comp_earnhead5_esi': bool,
    'comp_earnhead5_pt': bool, 
    'comp_earnhead5_it': bool, 
    'comp_earnhead5_ot': bool, 
    'comp_earnhead5_bonus': bool, 
    'comp_earn_head6': str, 
    'comp_earnhead6_pf': bool, 
    'comp_earnhead6_esi': bool, 
    'comp_earnhead6_pt': bool, 
    'comp_earnhead6_it': bool, 
    'comp_earnhead6_ot': bool, 
    'comp_earnhead6_bonus': bool, 
    'comp_earn_head7': str, 
    'comp_earnhead7_pf': bool,
    'comp_earnhead7_esi': bool,
    'comp_earnhead7_pt': bool, 
    'comp_earnhead7_it': bool, 
    'comp_earnhead7_ot': bool, 
    'comp_earnhead7_bonus': bool, 
    'comp_earn_head8': str, 
    'comp_earnhead8_pf': bool, 
    'comp_earnhead8_esi': bool, 
    'comp_earnhead8_pt': bool, 
    'comp_earnhead8_it': bool, 
    'comp_earnhead8_ot': bool, 
    'comp_earnhead8_bonus': bool,
    'comp_earn_head9': str, 
    'comp_earnhead9_pf': bool, 
    'comp_earnhead9_esi': bool, 
    'comp_earnhead9_pt': bool, 
    'comp_earnhead9_it': bool, 
    'comp_earnhead9_ot': bool, 
    'comp_earnhead9_bonus': bool, 
    'comp_earn_head10': str, 
    'comp_earnhead10_pf': bool, 
    'comp_earnhead10_esi': bool, 
    'comp_earnhead10_pt': bool, 
    'comp_earnhead10_it': bool, 
    'comp_earnhead10_ot': bool, 
    'comp_earnhead10_bonus': bool,
    'comp_bonus_from': str, 
    'comp_bonus_to': str, 
    'comp_bonus_percentage': float,
    'comp_bonus_limit': int,
    'comp_bonus_pt_included': bool, 
    'comp_leave_head1': str,
    'comp_leave_head2': str,
    'comp_leave_head3': str,
    'comp_loan_head1': str,
    'comp_loan_head2': str
    }
    df = pd.read_csv(f, dtype=dtype_mapping,keep_default_na=False)
    df['comp_pay_date'] = pd.to_datetime(df['comp_pay_date']).dt.date
    # key_to_ignore = 'ID'
    columns_to_ignore = ['ID','comp_emp_pfrate','comp_empr_fpfrate', 'comp_pf_admin','comp_pf_edli']
    ignored_dict = df.drop(columns=columns_to_ignore)
    print(ignored_dict)
    # ignored_dict = {key: value for key, value in df.items() if key != key_to_ignore}
    ignored_dict = pd.DataFrame(ignored_dict)
    for d in ignored_dict.to_dict(orient="records"):
      print(d)
      app_tables.company.add_row(**d)

@anvil.server.callable
def csv_trans_date_upload():
  with open(data_files["trans_date.csv"], "r") as f:
    dtype_mapping = {
      'tr_days': int,
      'tr_sundays': int,
      'tr_id': int
    }
    df = pd.read_csv(f, dtype=dtype_mapping,keep_default_na=False)
    df['tr_date'] = pd.to_datetime(df['tr_date']).dt.date
    df['tr_end_date'] = pd.to_datetime(df['tr_end_date']).dt.date
    key_to_ignore = 'ID'
    ignored_dict = {key: value for key, value in df.items() if key != key_to_ignore}
    ignored_dict = pd.DataFrame(ignored_dict)
    for d in ignored_dict.to_dict(orient="records"):
      print(d)
      app_tables.trans_date.add_row(**d)

@anvil.server.callable
def csv_transaction_upload():
  with open(data_files["transaction.csv"], "r") as f:
    dtype_mapping = {
      'id ': str, 
      'trans_empid': str, 
      'trans_empname': str, 
      'trans_father_husband': str, 
      'trans_empsex': str, 
      'trans_emptype': str, 
      'trans_deptcode': str, 
      'trans_deptname': str, 
      'trans_desicode': str, 
      'trans_desiname': str,
      'trans_emppfc': bool, 
      'trans_emppfno': int,
      'trans_emp_pfuan': str,
      'trans_empesic': bool,
      'trans_empesino': int,
      'trans_empdispensary': str,
      'trans_empptc': bool,
      'trans_empitc': bool,
      'trans_emppan': str,
      'trans_mandays': int,
      'trans_wo': int,
      'trans_ph': int,
      'trans_layoff': int,
      'trans_absent': int,
      'trans_leave1': int,
      'trans_leave2': int,
      'trans_leave3': int,
      'trans_othrs': int,
      'trans_inchrs': int,
      'trans_ded1': int,
      'trans_ded2': int,
      'trans_ded3': int,
      'trans_ded4': int,
      'trans_loan1': int,
      'trans_loan2': int,
      'trans_adv': int,
      'trans_tds': int,
      'trans_pfvol': int,
      'trans_lic': int,
      'trans_arr_esipt': int,
      'trans_arr_pf': int,
      'trans_earn1': int,
      'trans_earn2': int,
      'trans_earn3': int,
      'trans_earn4': int,
      'trans_earn5': int,
      'trans_earn6': int,
      'trans_earn7': int,
      'trans_earn8': int,
      'trans_earn9': int,
      'trans_earn10': int,
      'trans_earn_earn1': int,
      'trans_earn_earn2': int,
      'trans_earn_earn3': int,
      'trans_earn_earn4': int,
      'trans_earn_earn5': int,
      'trans_earn_earn6': int,
      'trans_earn_earn7': int,
      'trans_earn_earn8': int,
      'trans_earn_earn9': int,
      'trans_earn_earn10': int,
      'trans_phone_number': int,
      'trans_alt_phone_number': int,
      'trans_email_address': str,
      'trans_aadhar_number': int,
      'trans_attn_bonus': int,
      'fxd_earn_gross': int,
      'earn_pf_salary': int,
      'earn_fpf_salary': int,
      'earn_esi_salary': int,
      'earn_pt_salary': int,
      'earn_ot_salary': int,
      'earn_it_salary': int,
      'earn_bonus_salary': int,
      'pf_amt': int,
      'fpf_amt': int,
      'esi_amt': int,
      'pt_amt': int,
      'it_or_tds_amt': int,
      'bonus_amt': int
   }
    df = pd.read_csv(f, dtype=dtype_mapping,keep_default_na=False)
    df['trans_empdob'] = pd.to_datetime(df['trans_empdob']).dt.date
    df['trans_empdoj'] = pd.to_datetime(df['trans_empdoj']).dt.date
    df['trans_date'] = pd.to_datetime(df['trans_date']).dt.date
    columns_to_ignore = ['ID']
    key_to_ignore = 'ID'
    ignored_dict = {key: value for key, value in df.items() if key != key_to_ignore}
    ignored_dict = pd.DataFrame(ignored_dict)
    for d in ignored_dict.to_dict(orient="records"):
      print(d)
      app_tables.transaction.add_row(**d)

@anvil.server.callable
def csv_employee_upload():
  with open(data_files["employee.csv"], "r") as f:
    dtype_mapping = {
      'id': str,
      'emp_code': str,
      'emp_name': str,
      'emp_hus_name': str,
      'emp_sex': str,
      'emp_type': str,
      'emp_pf_contribution': bool,
      'emp_pf_number': int,
      'emp_pf_uan': str,
      'emp_esi_contribution': bool,
      'emp_esi_number': int,
      'emp_esi_dispensary': str,
      'emp_pt_contribution': bool,
      'emp_dept_code': str,
      'emp_dept_name': str,
      'emp_desi_code': str,
      'emp_desi_name': str,
      'emp_it_contribution': bool,
      'emp_pan_number': str,
      'earn1': int,
      'earn2': int,
      'earn3': int,
      'earn4': int,
      'earn5': int,
      'earn6': int,
      'earn7': int,
      'earn8': int,
      'earn9': int,
      'earn10': int,
      'phone_number': int,
      'alt_phone_number': int,
      'email_address': str,
      'aadhar_number': int,
      'attn_bonus': int
    }
    df = pd.read_csv(f, dtype=dtype_mapping,keep_default_na=False)
    df['emp_dob'] = pd.to_datetime(df['emp_dob']).dt.date
    df['emp_doj'] = pd.to_datetime(df['emp_doj']).dt.date
    key_to_ignore = 'ID'
    ignored_dict = {key: value for key, value in df.items() if key != key_to_ignore}
    ignored_dict = pd.DataFrame(ignored_dict)
    for d in ignored_dict.to_dict(orient="records"):
      print(d)
      app_tables.employee.add_row(**d)