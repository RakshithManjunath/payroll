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
    self.label_4.text = self.row['emp_sex']
    self.label_5.text = self.row['emp_type']
    self.label_6.text = "Date of birth - "+ self.row['emp_dob'].strftime("%d/%m/%Y")
    self.label_7.text = "Date of Joining - "+ self.row['emp_doj'].strftime("%d/%m/%Y")
    self.label_8.text = self.row['emp_dept_name']
    self.label_9.text = self.row['emp_desi_name']    

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





