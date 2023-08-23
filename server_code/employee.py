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
            emp_desi_name):
  app_tables.employee.add_row(id=id,
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
                              emp_desi_name=emp_desi_name
                             )

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