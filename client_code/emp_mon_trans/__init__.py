from ._anvil_designer import emp_mon_transTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class emp_mon_trans(emp_mon_transTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.drop_down_1.items = anvil.server.call('trans_empcode_name')

  def outlined_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('menu')

  def drop_down_1_change(self, **event_args):
    """This method is called when an item is selected"""
    split_list_emp = self.drop_down_1.selected_value.split("|")
    split_list_emp = [ele.strip() for ele in split_list_emp] 
    self.emp_code,self.emp_name = split_list_emp[0],split_list_emp[1]

    self.row = anvil.server.call('emp_get_details',self.emp_code)
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
    transid = anvil.server.call('trans_get_next_string_value')
    date = anvil.server.call('cur_trans_date')
    anvil.server.call('emp_to_trans_transfer', transid, date[0], 
                      self.emp_code,self.emp_name,self.fat_has_na,
                      self.emp_sex,self.empdob,self.empdoj,self.emptype,
                     self.deptcode,self.deptname,self.desicode,self.desiname,
                     self.emppfc,self.emppfno,self.emppfuan,self.empesic,
                     self.empesino,self.empdisp,self.empptc,self.empitc,
                     self.emppan,self.phno,self.alt_phno,self.email,self.aadhar_no,self.attn_bonus,
                     self.earn1,self.earn2,self.earn3,self.earn4,self.earn5,
                     self.earn6,self.earn7,self.earn8,self.earn9,self.earn10)






