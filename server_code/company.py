import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

############### Add Company ############
######### auto increment 'comp_id' column ###########
@anvil.server.callable
def comp_get_next_string_value():
  # Get the last row of the data table
  next_value = '0000000001'
  try:
    comp_id_list = [(r["comp_id"]) for r in app_tables.company.search()]
    last_row = comp_id_list[-1]
    last_string_value = last_row
    next_value = str(int(last_string_value) + 1).zfill(10)
  except IndexError:
    next_value == '0000000001'
  return next_value

@anvil.server.callable
def next_comp_id_value():
  # Get the last row of the data table
  next_value = '001'
  try:
    comp_code_list = [(r["comp_code"]) for r in app_tables.company.search()]
    last_row = comp_code_list[-1]
    last_string_value = last_row
    next_value = str(int(last_string_value) + 1).zfill(3)
  except IndexError:
    next_value == '001'
  return next_value

@anvil.server.callable
def comp_add(comp_id,compcode,compname,compaddr1,compaddr2,compaddr3,comppfno,compesino,comppto):
  app_tables.company.add_row(comp_id=comp_id,
                             comp_code=compcode,
                             comp_name=compname,
                             comp_addr1=compaddr1,
                             comp_addr2=compaddr2,
                             comp_addr3=compaddr3,
                             comp_pf_number=comppfno,
                             comp_esi_number=compesino,
                             comp_pto_circle=comppto,
                             )

#################### Company Change #################################
@anvil.server.callable
def comp_change_name_and_code():
  comp_details = []
  for r in app_tables.company.search(tables.order_by("comp_code")):
    comp_details.append(r['comp_code'] + " | "  +r['comp_name'])
  return comp_details

@anvil.server.callable
def comp_get_details(compcode):
  row = app_tables.company.get(comp_code=compcode)
  return row

@anvil.server.callable
def comp_update(comp_code, comp_addr1,comp_addr2,comp_addr3,comppfno,compesino,comppto,comp_name):
  row = app_tables.company.get(comp_code=comp_code)
  row.update(comp_addr1=comp_addr1,
             comp_addr2=comp_addr2,
             comp_addr3=comp_addr3,
             comp_pf_number=comppfno,
             comp_esi_number=compesino,
             comp_pto_circle=comppto,
             comp_name=comp_name)

####### company select ########
@anvil.server.callable
def company_select_code_and_name():
  company_details = [row['comp_code'] + " | "  +row['comp_name'] for row in app_tables.company.search(tables.order_by("comp_code"))]
  return company_details


####### statutary update pf ########
@anvil.server.callable
def statutary_update_pf(comp_code,comp_emp_pfrate,comp_empr_fpfrate,comp_pf_admin,comp_pf_edli,
                    comp_mgmt_pf_lt,comp_mgmt_fpf_lt):
  row = app_tables.company.get(comp_code=comp_code)
  row.update(comp_emp_pfrate=comp_emp_pfrate,
            comp_empr_fpfrate=comp_empr_fpfrate,
            comp_pf_admin=comp_pf_admin,
            comp_pf_edli=comp_pf_edli,
            comp_mgmt_pf_lt=comp_mgmt_pf_lt,
            comp_mgmt_fpf_lt=comp_mgmt_fpf_lt
            )

####### statutary update esi ########
@anvil.server.callable
def statutary_update_esi(comp_code,comp_esi_sal_lt):
  row = app_tables.company.get(comp_code=comp_code)
  row.update(comp_esi_sal_lt=comp_esi_sal_lt)

####### statutary update ded ########
@anvil.server.callable
def statutary_update_ded(comp_code, comp_ded1,comp_ded2,comp_ded3,comp_ded4):
  row = app_tables.company.get(comp_code=comp_code)
  row.update(comp_ded1=comp_ded1,
            comp_ded2=comp_ded2,
            comp_ded3=comp_ded3,
            comp_ded4=comp_ded4)


####### company more earan head  update ########
@anvil.server.callable
def comp_more_update_earnhead(comp_code,comp_earnhead1,comp_earnhead2,comp_earnhead3,comp_earnhead4,
                             comp_earnhead5,comp_earnhead6):
  row = app_tables.company.get(comp_code=comp_code)
  row.update(comp_earn_head1=comp_earnhead1)
  row.update(comp_earn_head2=comp_earnhead2)
  row.update(comp_earn_head3=comp_earnhead3)
  row.update(comp_earn_head4=comp_earnhead4)
  row.update(comp_earn_head5=comp_earnhead5)
  row.update(comp_earn_head6=comp_earnhead6)                               
