import anvil.files
from anvil.files import data_files
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
def statutary_update_esi(comp_code,comp_esi_sal_lt,
                         comp_pts1_from, comp_pts1_to, comp_pts1_pt,
                        comp_pts2_from, comp_pts2_to, comp_pts2_pt,
                        comp_pts3_from, comp_pts3_to, comp_pts3_pt):
  row = app_tables.company.get(comp_code=comp_code)
  row.update(comp_esi_sal_lt=comp_esi_sal_lt,
            comp_pts1_from=comp_pts1_from, comp_pts1_to=comp_pts1_to, comp_pts1_pt=comp_pts1_pt,
            comp_pts2_from=comp_pts2_from, comp_pts2_to=comp_pts2_to, comp_pts2_pt=comp_pts2_pt,
            comp_pts3_from=comp_pts3_from,comp_pts3_to=comp_pts3_to,comp_pts3_pt=comp_pts3_pt)

####### statutary update ded ########
@anvil.server.callable
def statutary_update_ded(comp_code, comp_ded1,comp_ded2,comp_ded3,comp_ded4):
  row = app_tables.company.get(comp_code=comp_code)
  row.update(comp_ded1=comp_ded1,
            comp_ded2=comp_ded2,
            comp_ded3=comp_ded3,
            comp_ded4=comp_ded4)


####### company more earnhead  update ########
@anvil.server.callable
def comp_more_update_earnhead(comp_code,comp_earnhead1,comp_earnhead2,comp_earnhead3,comp_earnhead4,
                             comp_earnhead5,comp_earnhead6,comp_earnhead7,comp_earnhead8,
                             comp_earnhead9,comp_earnhead10):
  row = app_tables.company.get(comp_code=comp_code)
  row.update(comp_earn_head1=comp_earnhead1,
            comp_earn_head2=comp_earnhead2,
            comp_earn_head3=comp_earnhead3,
            comp_earn_head4=comp_earnhead4,
            comp_earn_head5=comp_earnhead5,
            comp_earn_head6=comp_earnhead6,
            comp_earn_head7=comp_earnhead7,
            comp_earn_head8=comp_earnhead8,
            comp_earn_head9=comp_earnhead9,
            comp_earn_head10=comp_earnhead10
            )
                               

####### company earnhead1 ########
@anvil.server.callable
def comp_earnhead1(comp_code,comp_earnhead1_pf,comp_earnhead2_pf,comp_earnhead3_pf,comp_earnhead4_pf,comp_earnhead5_pf,
                  comp_earnhead6_pf,comp_earnhead7_pf,comp_earnhead8_pf,comp_earnhead9_pf,comp_earnhead10_pf,
                  comp_earnhead1_esi,comp_earnhead2_esi,comp_earnhead3_esi,comp_earnhead4_esi,comp_earnhead5_esi,
                  comp_earnhead6_esi,comp_earnhead7_esi,comp_earnhead8_esi,comp_earnhead9_esi,comp_earnhead10_esi,
                  comp_earnhead1_pt,comp_earnhead2_pt,comp_earnhead3_pt,comp_earnhead4_pt,comp_earnhead5_pt,
                  comp_earnhead6_pt,comp_earnhead7_pt,comp_earnhead8_pt,comp_earnhead9_pt,comp_earnhead10_pt,
                  comp_earnhead1_ot,comp_earnhead2_ot,comp_earnhead3_ot,comp_earnhead4_ot,comp_earnhead5_ot,
                  comp_earnhead6_ot,comp_earnhead7_ot,comp_earnhead8_ot,comp_earnhead9_ot,comp_earnhead10_ot,
                  comp_earnhead1_it,comp_earnhead2_it,comp_earnhead3_it,comp_earnhead4_it,comp_earnhead5_it,
                  comp_earnhead6_it,comp_earnhead7_it,comp_earnhead8_it,comp_earnhead9_it,comp_earnhead10_it,
                  comp_earnhead1_bonus,comp_earnhead2_bonus,comp_earnhead3_bonus,comp_earnhead4_bonus,comp_earnhead5_bonus,
                  comp_earnhead6_bonus,comp_earnhead7_bonus,comp_earnhead8_bonus,comp_earnhead9_bonus,comp_earnhead10_bonus):
  row = app_tables.company.get(comp_code=comp_code)
  row.update(comp_earnhead1_pf=comp_earnhead1_pf,
            comp_earnhead2_pf=comp_earnhead2_pf,
            comp_earnhead3_pf=comp_earnhead3_pf,
            comp_earnhead4_pf=comp_earnhead4_pf,
            comp_earnhead5_pf=comp_earnhead5_pf,
            comp_earnhead6_pf=comp_earnhead6_pf,
            comp_earnhead7_pf=comp_earnhead7_pf,
            comp_earnhead8_pf=comp_earnhead8_pf,
            comp_earnhead9_pf=comp_earnhead9_pf,
            comp_earnhead10_pf=comp_earnhead10_pf,
            comp_earnhead1_esi=comp_earnhead1_esi,
            comp_earnhead2_esi=comp_earnhead2_esi,
            comp_earnhead3_esi=comp_earnhead3_esi,
            comp_earnhead4_esi=comp_earnhead4_esi,
            comp_earnhead5_esi=comp_earnhead5_esi,
            comp_earnhead6_esi=comp_earnhead6_esi,
            comp_earnhead7_esi=comp_earnhead7_esi,
            comp_earnhead8_esi=comp_earnhead8_esi,
            comp_earnhead9_esi=comp_earnhead9_esi,
            comp_earnhead10_esi=comp_earnhead10_esi,
            comp_earnhead1_pt=comp_earnhead1_pt,
            comp_earnhead2_pt=comp_earnhead2_pt,
            comp_earnhead3_pt=comp_earnhead3_pt,
            comp_earnhead4_pt=comp_earnhead4_pt,
            comp_earnhead5_pt=comp_earnhead5_pt,
            comp_earnhead6_pt=comp_earnhead6_pt,
            comp_earnhead7_pt=comp_earnhead7_pt,
            comp_earnhead8_pt=comp_earnhead8_pt,
            comp_earnhead9_pt=comp_earnhead9_pt,
            comp_earnhead10_pt=comp_earnhead10_pt,
            comp_earnhead1_ot=comp_earnhead1_ot,
            comp_earnhead2_ot=comp_earnhead2_ot,
            comp_earnhead3_ot=comp_earnhead3_ot,
            comp_earnhead4_ot=comp_earnhead4_ot,
            comp_earnhead5_ot=comp_earnhead5_ot,
            comp_earnhead6_ot=comp_earnhead6_ot,
            comp_earnhead7_ot=comp_earnhead7_ot,
            comp_earnhead8_ot=comp_earnhead8_ot,
            comp_earnhead9_ot=comp_earnhead9_ot,
            comp_earnhead10_ot=comp_earnhead10_ot,
            comp_earnhead1_it=comp_earnhead1_it,
            comp_earnhead2_it=comp_earnhead2_it,
            comp_earnhead3_it=comp_earnhead3_it,
            comp_earnhead4_it=comp_earnhead4_it,
            comp_earnhead5_it=comp_earnhead5_it,
            comp_earnhead6_it=comp_earnhead6_it,
            comp_earnhead7_it=comp_earnhead7_it,
            comp_earnhead8_it=comp_earnhead8_it,
            comp_earnhead9_it=comp_earnhead9_it,
            comp_earnhead10_it=comp_earnhead10_it,
            comp_earnhead1_bonus=comp_earnhead1_bonus,
            comp_earnhead2_bonus=comp_earnhead2_bonus,
            comp_earnhead3_bonus=comp_earnhead3_bonus,
            comp_earnhead4_bonus=comp_earnhead4_bonus,
            comp_earnhead5_bonus=comp_earnhead5_bonus,
            comp_earnhead6_bonus=comp_earnhead6_bonus,
            comp_earnhead7_bonus=comp_earnhead7_bonus,
            comp_earnhead8_bonus=comp_earnhead8_bonus,
            comp_earnhead9_bonus=comp_earnhead9_bonus,
            comp_earnhead10_bonus=comp_earnhead10_bonus)

####### company Misc ########
@anvil.server.callable
def comp_misc_leave_loan_update(comp_code, comp_leave_head1,comp_leave_head2,comp_leave_head3,
                               comp_loan_head1,comp_loan_head2,comp_pay_date):
  row = app_tables.company.get(comp_code=comp_code)
  row.update(comp_leave_head1=comp_leave_head1,
            comp_leave_head2=comp_leave_head2,
            comp_leave_head3=comp_leave_head3,
            comp_loan_head1=comp_loan_head1,
            comp_loan_head2=comp_loan_head2,
            comp_pay_date=comp_pay_date)

####### stat bonus update #######
@anvil.server.callable
def stat_bonus_update(comp_code, comp_bonus_from, comp_bonus_to, comp_bonus_percentage, comp_bonus_limit, comp_bonus_pt_included):
  row = app_tables.company.get(comp_code=comp_code)
  row.update(comp_bonus_from=comp_bonus_from,
            comp_bonus_to=comp_bonus_to,
            comp_bonus_percentage=comp_bonus_percentage,
            comp_bonus_limit=comp_bonus_limit,
            comp_bonus_pt_included=comp_bonus_pt_included)