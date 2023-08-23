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

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    split_list_emp = self.drop_down_1.selected_value.split("|")
    split_list_emp = [ele.strip() for ele in split_list_emp] 
    emp_code,emp_name = split_list_emp[0],split_list_emp[1]
    anvil.server.call('emp_update_earn',emp_code,self.custom_1.text_box_1.text,
                     self.custom_1.text_box_2.text,self.custom_1.text_box_3.text,
                     self.custom_1.text_box_4.text,
                     self.custom_2.text_box_1.text,self.custom_2.text_box_2.text,
                     self.custom_2.text_box_3.text,self.custom_2.text_box_4.text)

  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.custom_2.visible = not self.custom_2.visible
    self.custom_1.visible = False



