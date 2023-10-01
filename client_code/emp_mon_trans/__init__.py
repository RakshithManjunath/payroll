from ._anvil_designer import emp_mon_transTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import gvarb

class emp_mon_trans(emp_mon_transTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.label_10.text = gvarb.g_comname+' '+gvarb.g_mode
    self.drop_down_1.items = anvil.server.call('comp_wise_emp_code_and_name', gvarb.g_comcode)
    
    # self.drop_down_1.items = anvil.server.call('trans_empcode_name')
    # anvil.server.call('trans_earn_earn_calculation', gvarb.g_comcode)

  def outlined_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('menu')

  def drop_down_1_change(self, **event_args):
    """This method is called when an item is selected"""
    split_list_emp = self.drop_down_1.selected_value.split("|")
    split_list_emp = [ele.strip() for ele in split_list_emp] 
    self.emp_code,self.emp_name = split_list_emp[0],split_list_emp[1]

    self.row = anvil.server.call('emp_get_details',self.emp_code,gvarb.g_comcode)
    self.label_3.text = "Father / Husband name - "+self.row['emp_hus_name']
    self.fat_has_na = self.row['emp_hus_name']
    self.label_4.text = self.row['emp_sex']
    self.emp_sex = self.row['emp_sex']
    self.label_5.text = self.row['emp_type']
    self.emptype = self.row['emp_type']
    self.label_6.text = "Date of birth - "+ self.row['emp_dob'].strftime("%d/%m/%Y")
    self.empdob = self.row['emp_dob']
    self.label_7.text = "Date of Joining - "+ self.row['emp_doj'].strftime("%d/%m/%Y")
    self.empdoj = self.row['emp_doj']
    self.label_8.text = self.row['emp_dept_name']
    self.deptcode = self.row['emp_dept_code']
    self.deptname = self.row['emp_dept_name']
    self.label_9.text = self.row['emp_desi_name']
    self.desicode = self.row['emp_desi_code']
    self.desiname = self.row['emp_desi_name']
    self.emppfc = self.row['emp_pf_contribution']
    self.emppfno = self.row['emp_pf_number']
    self.emppfuan = self.row['emp_pf_uan']
    self.empesic = self.row['emp_esi_contribution']
    self.empesino = self.row['emp_esi_number']
    self.empdisp = self.row['emp_esi_dispensary']
    self.empptc = self.row['emp_pt_contribution']
    self.empitc = self.row['emp_it_contribution']
    self.emppan = self.row['emp_pan_number']

    self.phno = self.row['phone_number']
    self.alt_phno = self.row['alt_phone_number']
    self.email = self.row['email_address']
    self.aadhar_no = self.row['aadhar_number']
    self.attn_bonus = self.row['attn_bonus']
    

    self.earn1 = self.row['earn1']
    self.earn2 = self.row['earn2']
    self.earn3 = self.row['earn3']
    self.earn4 = self.row['earn4']
    self.earn5 = self.row['earn5']
    self.earn6 = self.row['earn6']
    self.earn7 = self.row['earn7']
    self.earn8 = self.row['earn8']
    self.earn9 = self.row['earn9']
    self.earn10 = self.row['earn10']

    self.link_1.visible = True
    self.link_2.visible = True
    self.link_3.visible = True

    comp_details = anvil.server.call('comp_get_details', gvarb.g_comcode)
    self.custom_1.label_6.text = comp_details['comp_leave_head1']
    self.custom_1.label_7.text = comp_details['comp_leave_head2']
    self.custom_1.label_8.text = comp_details['comp_leave_head3']

    self.custom_2.label_1.text = comp_details['comp_ded1']
    self.custom_2.label_2.text = comp_details['comp_ded2']
    self.custom_2.label_3.text = comp_details['comp_ded3']
    self.custom_2.label_4.text = comp_details['comp_ded4']
    self.custom_2.label_5.text = comp_details['comp_loan_head1']
    self.custom_2.label_6.text = comp_details['comp_loan_head2']
      
  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.custom_1.visible = not self.custom_1.visible
    self.custom_2.visible = False
    self.custom_3.visible = False

  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.custom_1.visible = False
    self.custom_2.visible = not self.custom_2.visible
    self.custom_3.visible = False

  def link_3_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.custom_1.visible = False
    self.custom_2.visible = False
    self.custom_3.visible = not self.custom_3.visible

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.transid = anvil.server.call('trans_get_next_string_value')
    date = anvil.server.call('cur_trans_date')
    # master to trans 
    row = anvil.server.call('emp_to_trans_transfer', self.transid, date[0], 
                      self.emp_code,self.emp_name,self.fat_has_na,
                      self.emp_sex,self.empdob,self.empdoj,self.emptype,
                     self.deptcode,self.deptname,self.desicode,self.desiname,
                     self.emppfc,self.emppfno,self.emppfuan,self.empesic,
                     self.empesino,self.empdisp,self.empptc,self.empitc,
                     self.emppan,self.phno,self.alt_phno,self.email,self.aadhar_no,self.attn_bonus,
                     self.earn1,self.earn2,self.earn3,self.earn4,self.earn5,
                     self.earn6,self.earn7,self.earn8,self.earn9,self.earn10,
                     self.custom_1.text_box_1.text,self.custom_1.text_box_2.text,self.custom_1.text_box_3.text,
                     self.custom_1.text_box_4.text,self.custom_1.text_box_5.text,self.custom_1.text_box_6.text,
                     self.custom_1.text_box_7.text,self.custom_1.text_box_8.text,self.custom_1.text_box_9.text,
                     self.custom_1.text_box_10.text,
                     self.custom_2.text_box_1.text,self.custom_2.text_box_2.text,self.custom_2.text_box_3.text,
                     self.custom_2.text_box_4.text,self.custom_2.text_box_5.text,self.custom_2.text_box_6.text,
                     self.custom_2.text_box_7.text,self.custom_2.text_box_8.text,self.custom_2.text_box_9.text,
                     self.custom_2.text_box_10.text,
                     self.custom_3.text_box_1.text,self.custom_3.text_box_2.text,
                     self.custom_1.text_box_11.text,gvarb.g_comcode)

    # default values for transaction
    anvil.server.call('trans_default_values',row)

    # trans to trans
    
    earn1,earn2,earn3,earn4,earn5,earn6,earn7,earn8,earn9,earn10 = anvil.server.call('earn_cal',gvarb.g_comcode,self.emp_code)
    anvil.server.call('update_earn',gvarb.g_comcode,self.emp_code,earn1,
                     earn2,earn3,earn4,earn5,earn6,earn7,earn8,earn9,earn10)
    
    eattn_bonus = anvil.server.call('attn_bonus',gvarb.g_comcode,self.emp_code)
    anvil.server.call('update_earn_att_bonus',gvarb.g_comcode,self.emp_code,eattn_bonus)
 
    pfsal = anvil.server.call('pf_calculaton',gvarb.g_comcode,self.emp_code)
    anvil.server.call('update_pfsalary',gvarb.g_comcode,self.emp_code,pfsal)

    esisal = anvil.server.call('esi_calculaton',gvarb.g_comcode,self.emp_code)
    anvil.server.call('update_esisalary',gvarb.g_comcode,self.emp_code,esisal)

    ptsal = anvil.server.call('pt_calculaton',gvarb.g_comcode,self.emp_code)
    anvil.server.call('update_ptsalary',gvarb.g_comcode,self.emp_code,ptsal) 

    otsal = anvil.server.call('ot_calculaton',gvarb.g_comcode,self.emp_code)
    anvil.server.call('update_otsalary',gvarb.g_comcode,self.emp_code,otsal) 

    itsal = anvil.server.call('ot_calculaton',gvarb.g_comcode,self.emp_code)
    anvil.server.call('update_itsalary',gvarb.g_comcode,self.emp_code,itsal) 

    bns_sal = anvil.server.call('bonus_calculaton',gvarb.g_comcode,self.emp_code)
    anvil.server.call('update_bonus_salary',gvarb.g_comcode,self.emp_code,bns_sal)
    
    Notification(self.emp_name + " transaction data added successfully").show()

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('emp_mon_trans')


  






