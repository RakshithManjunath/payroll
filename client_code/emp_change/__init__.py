from ._anvil_designer import emp_changeTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class emp_change(emp_changeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

    self.drop_down_1.items = anvil.server.call('emp_name_and_code')

  def drop_down_1_change(self, **event_args):
    """This method is called when an item is selected"""
    split_list_emp = self.drop_down_1.selected_value.split("|")
    split_list_emp = [ele.strip() for ele in split_list_emp] 
    self.emp_code,self.emp_name = split_list_emp[0],split_list_emp[1]

    row = anvil.server.call('emp_get_details',self.emp_code)
    
    self.text_box_1.text = self.emp_name
    self.text_box_2.text = row['emp_hus_name']
    emp_sex = row['emp_sex']
    if emp_sex == "Male":
      self.radio_button_1.selected = True
      self.radio_button_2.selected = False
    else:
      self.radio_button_2.selected = True
      self.radio_button_1.selected = False

    self.date_picker_1.date = row['emp_dob']
    self.date_picker_2.date = row['emp_doj']

    emp_type = row['emp_type']
    if emp_type == "Staff":
      self.radio_button_3.selected = True
      self.radio_button_4.selected = False
    else:
      self.radio_button_4.selected = True
      self.radio_button_3.selected = False

    self.text_box_3.text = row['emp_dept_name']
    self.drop_down_2.items = anvil.server.call('dept_change_name_and_code')
    self.text_box_4.text = row['emp_desi_name']
    self.drop_down_3.items = anvil.server.call('desi_change_name_and_code')

    emp_pfc = row['emp_pf_contribution']
    if emp_pfc == "Yes":
      self.custom_1.radio_button_1.selected = True
      self.custom_1.radio_button_2.selected = False
    else:
      self.custom_1.radio_button_2.selected = True
      self.custom_1.radio_button_1.selected = False

    self.custom_1.text_box_1.text = row['emp_pf_number']
    self.custom_1.text_box_2.text = row['emp_pf_uan']
    

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('emp_update_row', self.emp_code, 
                                       self.text_box_1.text)
    
    Notification(self.text_box_1.text + " data modified successfully").show()

  def date_picker_2_change(self, **event_args):
    """This method is called when the selected date changes"""
    pass

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