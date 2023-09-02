from ._anvil_designer import emp_more1Template
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class emp_more1(emp_more1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.drop_down_1.items = anvil.server.call('emp_name_and_code')
   

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.custom_1.visible = not self.custom_1.visible
    self.custom_2.visible = False

  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.custom_2.visible = not self.custom_2.visible
    self.custom_1.visible = False

  def drop_down_1_change(self, **event_args):
    """This method is called when an item is selected"""
    split_list_emp = self.drop_down_1.selected_value.split("|")
    split_list_emp = [ele.strip() for ele in split_list_emp] 
    self.emp_code,self.emp_name = split_list_emp[0],split_list_emp[1]

    self.row = anvil.server.call('emp_get_details',self.emp_code)
    self.label_2.text = "Father / Husband name - "+self.row['emp_hus_name']
    self.label_3.text = self.row['emp_sex']
    self.label_4.text = self.row['emp_type']
    self.label_5.text = "Date of birth - "+ self.row['emp_dob'].strftime("%d/%m/%Y")
    self.label_6.text = "Date of Joining - "+ self.row['emp_doj'].strftime("%d/%m/%Y")
    self.label_7.text = self.row['emp_dept_name']
    self.label_8.text = self.row['emp_desi_name']    
    
    self.custom_1.text_box_1.text = self.row['earn1']
    self.custom_1.text_box_2.text = self.row['earn2']
    self.custom_1.text_box_3.text = self.row['earn3']
    self.custom_1.text_box_4.text = self.row['earn4']
    self.custom_1.text_box_5.text = self.row['earn5']
    self.custom_1.text_box_6.text = self.row['earn6']
    self.custom_1.text_box_7.text = self.row['earn7']
    self.custom_1.text_box_8.text = self.row['earn8']
    self.custom_1.text_box_9.text = self.row['earn9']
    self.custom_1.text_box_10.text = self.row['earn10']

    self.custom_2.text_box_1.text = self.row['phone_number']
    self.custom_2.text_box_2.text = self.row['alt_phone_number']
    self.custom_2.text_box_3.text = self.row['email_address']
    self.custom_2.text_box_4.text = self.row['aadhar_number']
    self.custom_2.text_box_5.text = self.row['attn_bonus']

  def outlined_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('menu')

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('emp_more1')

