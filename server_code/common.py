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
  transaction.add_row(
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