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
def import_company_csv():
  with open(file_path.company_path, "r") as f:
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
    'comp_emp_pfrate': float, 
    'comp_empr_fpfrate': float, 
    'comp_pf_admin': float, 
    'comp_pf_edli': float, 
    'comp_mgmt_pf_lt': float, 
    'comp_mgmt_fpf_lt': float, 
    'comp_esi_sal_lt': float, 
    'comp_pts1_from': float, 
    'comp_pts1_to': float, 
    'comp_pts1_pt': float, 
    'comp_pts2_from': float, 
    'comp_pts2_to': float, 
    'comp_pts2_pt': float, 
    'comp_pts3_from': float, 
    'comp_pts3_to': float, 
    'comp_pts3_pt': float, 
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
    'comp_bonus_limit': float,
    'comp_bonus_pt_included': bool, 
    'comp_leave_head1': str,
    'comp_leave_head2': str,
    'comp_leave_head3': str,
    'comp_loan_head1': str,
    'comp_loan_head2': str
    }
    df = pd.read_csv(f, dtype=dtype_mapping,keep_default_na=False)
    df['comp_pay_date'] = pd.to_datetime(df['comp_pay_date']).dt.date
    key_to_ignore = 'ID'
    ignored_dict = {key: value for key, value in df.items() if key != key_to_ignore}
    ignored_dict = pd.DataFrame(ignored_dict)
    print(ignored_dict)
    # ignored_dict = {key: value for key, value in df.items() if key != key_to_ignore}
    ignored_dict = pd.DataFrame(ignored_dict)
    for d in ignored_dict.to_dict(orient="records"):
      print(d)
      app_tables.company.add_row(**d)