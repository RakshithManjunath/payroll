import anvil.files
from anvil.files import data_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from datetime import date

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


######### auto increment 'id' column ###########
@anvil.server.callable
def emp_get_next_id_value():
  # Get the last row of the data table
  next_value = '0000000001'
  try:
    trans_code_list = [(r["id"]) for r in app_tables.employee.search()]
    last_row = trans_code_list[-1]
    last_string_value = last_row
    next_value = str(int(last_string_value) + 1).zfill(10)
  except IndexError:
    next_value == '0000000001'
  return next_value


######## add employee #########
@anvil.server.callable
def emp_add(id,emp_code,emp_name,emp_hus_name,emp_dob,emp_doj,
            emp_sex,emp_type,emp_pf_contribution,emp_pf_number,
            emp_pf_uan,emp_esi_contribution,emp_esi_number, 
            emp_esi_dispensary,emp_pt_contribution,emp_it_contribution,
            emp_pan_number,emp_dept_code,emp_dept_name,emp_desi_code,
            emp_desi_name,photo,emp_comp_code):
  return app_tables.employee.add_row(id=id,
                              emp_code=emp_code,
                              emp_name=emp_name,
                              emp_hus_name=emp_hus_name,
                              emp_dob=emp_dob,
                              emp_doj=emp_doj,
                              emp_sex=emp_sex,
                              emp_type=emp_type,
                              emp_pf_contribution=emp_pf_contribution,
                              emp_pf_number=emp_pf_number,
                              emp_pf_uan=emp_pf_uan,
                              emp_esi_contribution=emp_esi_contribution,
                              emp_esi_number=emp_esi_number,
                              emp_esi_dispensary=emp_esi_dispensary,
                              emp_pt_contribution=emp_pt_contribution,
                              emp_it_contribution=emp_it_contribution,
                              emp_pan_number=emp_pan_number,
                              emp_dept_code=emp_dept_code,
                              emp_dept_name=emp_dept_name,
                              emp_desi_code=emp_desi_code,
                              emp_desi_name=emp_desi_name,
                              emp_photo=photo,
                              emp_comp_code=emp_comp_code)

@anvil.server.callable
def emp_default_values(row):
  columns_and_types = {
    'emp_hus_name': 'text', 
    'emp_dob': 'date',
    'emp_doj' : 'date',
    'emp_sex': 'text',
    'emp_type': 'text',
    'emp_pf_contribution': 'true/false',
    'emp_pf_number': 'number',
    'emp_pf_uan': 'text',
    'emp_esi_contribution': 'true/false',
    'emp_esi_number': 'number',
    'emp_esi_dispensary': 'text',
    'emp_pt_contribution': 'true/false',
    'emp_dept_code': 'text',
    'emp_dept_name': 'text',
    'emp_desi_code': 'text',
    'emp_desi_name': 'text',
    'emp_it_contribution': 'true/false',
    'emp_pan_number': 'text',
    'earn1': 'number',
    'earn2': 'number',
    'earn3': 'number',
    'earn4': 'number',
    'earn5': 'number',
    'earn6': 'number',
    'earn7': 'number',
    'earn8': 'number',
    'earn9': 'number',
    'earn10': 'number',
    'phone_number': 'number',
    'alt_phone_number': 'number',
    'email_address': 'text',
    'aadhar_number': 'number',
    'attn_bonus': 'number'
  }
  for column_name, column_type in columns_and_types.items():
    print(column_name, column_type)
    if row[column_name] is None:
      print(row[column_name])
      default_value = get_default_value_for_type(column_type)
      row[column_name] = default_value

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

######## change employee #########
@anvil.server.callable
def emp_update_row(emp_code,emp_name,emp_hus_name,emp_dob,emp_doj,
            emp_sex,emp_type,emp_pf_contribution,emp_pf_number,
            emp_pf_uan,emp_esi_contribution,emp_esi_number, 
            emp_esi_dispensary,emp_pt_contribution,emp_it_contribution,
            emp_pan_number,emp_dept_code,emp_dept_name,emp_desi_code,
            emp_desi_name):
  row = app_tables.employee.get(emp_code=emp_code)
  row.update(emp_name=emp_name,
            emp_hus_name=emp_hus_name,
            emp_dob=emp_dob,
            emp_doj=emp_doj,
            emp_sex=emp_sex,
            emp_type=emp_type,
            emp_pf_contribution=emp_pf_contribution,
            emp_pf_number=emp_pf_number,
            emp_pf_uan=emp_pf_uan,
            emp_esi_contribution=emp_esi_contribution,
            emp_esi_number=emp_esi_number,
            emp_esi_dispensary=emp_esi_dispensary,
            emp_pt_contribution=emp_pt_contribution,
            emp_it_contribution=emp_it_contribution,
            emp_pan_number=emp_pan_number,
            emp_dept_code=emp_dept_code,
            emp_dept_name=emp_dept_name,
            emp_desi_code=emp_desi_code,
            emp_desi_name=emp_desi_name)


####### concatenating emp name and code #########
@anvil.server.callable
def emp_name_and_code():
  emp_details = []
  for r in app_tables.employee.search(tables.order_by("emp_code")):
    emp_details.append(r['emp_code'] + " | "  +r['emp_name'])
  return emp_details


@anvil.server.callable
def emp_get_details(empcode):
  row = app_tables.employee.get(emp_code=empcode)
  return row


################ update emp earning #################
@anvil.server.callable
def emp_update_earn(empcode, earn1,earn2,earn3,earn4,earn5,earn6,earn7,earn8,earn9,earn10):
  row = app_tables.employee.get(emp_code=empcode)
  row.update(earn1=earn1,earn2=earn2,earn3=earn3,earn4=earn4,earn5=earn5,
            earn6=earn6,earn7=earn7,earn8=earn8,earn9=earn9,earn10=earn10)

############# update emp misc1 ################
@anvil.server.callable
def emp_update_misc1(empcode,phone_number,alt_phone_number,email_address,aadhar_number,
                    attn_bonus):
  row = app_tables.employee.get(emp_code=empcode)
  row.update(phone_number=phone_number,alt_phone_number=alt_phone_number,
            email_address=email_address,
            aadhar_number=aadhar_number,
            attn_bonus=attn_bonus)


############# update emp misc2 ################
@anvil.server.callable
def emp_update_misc2(empcode,emp_photo):
  row = app_tables.employee.get(emp_code=empcode)
  row.update(emp_photo = emp_photo)
