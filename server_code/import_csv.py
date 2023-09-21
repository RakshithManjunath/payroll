import anvil.files
from anvil.files import data_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import pandas as pd
import file_path

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
def import_transaction_csv():
  with open(file_path.transaction_path, "r") as f:
    dtype_mapping = {
      'id': str,
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


def import_department_csv():
  with open(file_path.department_path, "r") as f:
    dtype_mapping = {
      'dept_id': str,  
    'dept_code': str,
    'dept_name': str,
    }
    df = pd.read_csv(f, dtype=dtype_mapping,keep_default_na=False)
    key_to_ignore = 'ID'
    ignored_dict = {key: value for key, value in df.items() if key != key_to_ignore}
    ignored_dict = pd.DataFrame(ignored_dict)
    for d in ignored_dict.to_dict(orient="records"):
      print(d)
      app_tables.department.add_row(**d)

def import_desi_csv():
  with open(file_path.desi_path, "r") as f:
    dtype_mapping = {
      'desi_id': str,  
    'desi_code': str,
    'desi_name': str,
    }
    df = pd.read_csv(f, dtype=dtype_mapping,keep_default_na=False)
    key_to_ignore = 'ID'
    ignored_dict = {key: value for key, value in df.items() if key != key_to_ignore}
    ignored_dict = pd.DataFrame(ignored_dict)
    for d in ignored_dict.to_dict(orient="records"):
      print(d)
      app_tables.designation.add_row(**d)

def import_bank_csv():
  with open(file_path.bank_path, "r") as f:
    dtype_mapping = {
      'bank_id': str,  
    'bank_code': str,
    'bank_name': str,
    'bank_addr1': str,
    'bank_addr2': str,
    'bank_addr3': str,
    'bank_ifsc': str
    }
    df = pd.read_csv(f, dtype=dtype_mapping,keep_default_na=False)
    key_to_ignore = 'ID'
    ignored_dict = {key: value for key, value in df.items() if key != key_to_ignore}
    ignored_dict = pd.DataFrame(ignored_dict)
    for d in ignored_dict.to_dict(orient="records"):
      print(d)
      app_tables.bank.add_row(**d)

def import_password_csv():
  with open(file_path.password_path, "r") as f:
    dtype_mapping = {
      'username': str,  
    'password': str
    }
    df = pd.read_csv(f, dtype=dtype_mapping,keep_default_na=False)
    key_to_ignore = 'ID'
    ignored_dict = {key: value for key, value in df.items() if key != key_to_ignore}
    ignored_dict = pd.DataFrame(ignored_dict)
    for d in ignored_dict.to_dict(orient="records"):
      print(d)
      app_tables.password.add_row(**d)

def import_trans_date_csv():
  with open(file_path.trans_date_path, "r") as f:
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


def import_employee_csv():
  with open(file_path.employee_path, "r") as f:
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

@anvil.server.callable
def import_all_csv():
  import_department_csv()
  import_desi_csv()
  import_bank_csv()
  import_password_csv()
  import_trans_date_csv()
  import_company_csv()
  import_employee_csv()
  import_transaction_csv()